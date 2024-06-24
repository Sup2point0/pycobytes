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

    for field, key in FIELDS.items():
      if field in line:
        *_, value = line.partition("= ")
        value = value.strip()

        if field == "date":
          try:
            fields["unix"] = datetime.strptime(value, "%d %B %Y")
          except:
            return
            # NOTE non-dates will be filtered and removed
        elif field == "topics":
          value = value.split(" / ")
        
        fields[key] = value
  
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
    "displayIndex": file.stem,
    **meta,
  })

  front = f'''---
{"\n".join(f"{key}: {val}" for key, val in meta.items())}
---
'''

  ROUTE = DEST / (file.stem + ".svx")
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
issues = [each for each in issues if each["unix"]]
issues.sort(key = lambda each: each["unix"])
for i, issue in enumerate(issues):
  issue.pop("unix", None)
  issue["orderIndex"] = i


with open(SRC / "issues-config.ts", "r") as source:
  content = source.read()

content = re.sub(
  pattern = r"(Last auto-generated: ).*",
  repl = r"\1" + date.today().strftime("%b %d"),
  string = content
)

data = ",\n".join(json.dumps(each, indent = 2) for each in issues)
content = re.sub(
  pattern = r"(#PYCO target! \*/ \[).*(\];)",
  repl = r"\1" + data + r"\2",
  string = content,
  flags = re.DOTALL
)
content = re.sub(
  pattern = r"\"(.*)\":",
  repl = r"\1:",
  string = content
)

with open(SRC / "issues-config.ts", "w") as dest:
  dest.write(content)


with open(SRC / "issues-config.json", "w") as dest:
  json.dump(issues, dest, indent = 2)
