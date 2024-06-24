'''
Load issues from `./issues/` into `issues-config.js` for SvelteKit to use when building the site routes.
'''

print("           / collecting issues...")

import json
import os
import re
import shutil
from datetime import date, datetime
from pathlib import Path

from __main__ import ROOT


SRC = ROOT / "site/src"


## Load
files = (ROOT / "issues").glob("[0-9][0-9].md")

DEST = SRC / "exported"
if not os.path.exists(DEST):
  os.mkdir(DEST)

issues = []
FIELDS = {
  "index": "issueIndex",
  "title": "titleText",
  "date": "releaseDate",
  "topics": "topicTags",
}


def process_file(file) -> dict | None:
  with open(file, "r") as source:
    content = source.readlines()

  if not any(("#PYCO live!" in line) for line in content[:4]):
    return

  live = False
  fields = {}

  for line in content[:7]:
    if "-->" in line:
      break

    if not live:
      if "#PYCO live!" in line:
        live = True

    for field in FIELDS.keys():
      if field in line:
        *_, value = line.partition("= ")
        value = value.strip()

        if field == "index":
          field = "issueIndex"
          # NOTE conversion to avoid conflicts
        elif field == "date":
          try:
            fields["datetime"] = datetime.strptime(value, "%d %B %Y")
          except:
            return
            # NOTE non-dates will be filtered and removed
        elif field == "topics":
          value = value.split(" / ")
        
        fields[field] = value
  
  return {
    "content": content,
    "meta": fields,
  } if live else None


for file in files:
  data = process_file(file)
  if not data:
    continue

  content = data["content"]
  meta = data["meta"]
  index = meta["issueIndex"]

  content = "".join(content[1:])
  content = re.sub(r"../assets/issues/[0-9]*/", "/", content)

  issues.append({
    "name": file.stem,
    **meta,
  })

  front = f'''---
  issueIndex: {index}
  title: {meta["title"]}
  date: {meta.get("date", None)}
  topic: {meta.get("topic", None)}
---
'''

  ROUTE = DEST / (index + ".svx")
  shutil.copyfile(file, ROUTE)

  with open(ROUTE, "w") as dest:
    dest.seek(0)
    dest.write(front + "\n" + content)

  ## FIXME copy to _Content.svx for static routing

  # _Content.svx
  ISSUES = SRC / "routes/issues"
  ROUTE = ISSUES / index

  if not os.path.exists(ROUTE):
    os.mkdir(ROUTE)

  shutil.copyfile(file, ROUTE / "_Content.svx")

  with open(ROUTE / "_Content.svx", "w") as dest:
    dest.write(front + "\n" + content)

  # +page.svelte
  with open(ISSUES / "-page.txt", "r") as source:
    source.readline()
    content = source.read()

  front = f'''
import ISSUES from "#src/issues-config";
const issue = ISSUES[{int(index) - 1}];

import Content from "../{index}/_Content.svx";
'''

  with open(ROUTE / "+page.svelte", "w+") as dest:
    dest.write("\n".join(["<script>", front, content]))


## Save - a little scuffed, but it works well
issues = [each for each in issues if each["datetime"]]
issues.sort(key = lambda issue: issue["datetime"])
for issue in issues:
  issue.pop("datetime", None)

update = date.today().strftime("%b %d")

content = f'''/// Issues Index
/// last auto-generated: {update}

const ISSUES = [{",\n".join(
  json.dumps(each, indent = 2)
  for each in issues
)}];
export default ISSUES;
'''

with open(SRC / "issues-config.js", "w") as dest:
  dest.write(content)

## FIXME standardise config format
with open(SRC / "issues-config.json", "w") as dest:
  dest.write(json.dumps(issues, indent = 2))
