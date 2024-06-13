'''
Load issues from `./issues/` into `issues-config.js` for SvelteKit to use when building the site routes.
'''

print("           / collecting issues...")

import json
import os
import re
import shutil
from datetime import date
from pathlib import Path

from __main__ import ROOT


SRC = ROOT / "site/src"


## Load
files = (ROOT / "issues").glob("[0-9][0-9].md")

DEST = SRC / "exported"
if not os.path.exists(DEST):
  os.mkdir(DEST)

issues = []
FIELDS = ["index", "title", "date", "topic"]


def process_file(file) -> dict | None:
  with open(file, "r") as source:
    content = source.readlines()

  if not any(("#PYCO live!" in line) for line in content[:4]):
    return

  live = False
  fields = {}

  for line in content[:5]:
    if "-->" in line:
      break

    if not live:
      if "#PYCO live!" in line:
        live = True

    for field in FIELDS:
      if field in line:
        *_, value = line.partition("= ")
        if field == "index":
          field = "issueIndex"  # NOTE conversion to avoid conflicts
        fields[field] = value.strip()
  
  if not live:
    return
  
  return {
    "content": content,
    "meta": fields,
  }


for file in files:
  data = process_file(file)

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
update = date.today().strftime("%b %d")

content = f'''/// Issues Index
/// last auto-generated: {update}

const ISSUES = [{",\n".join(
  json.dumps(each, indent = 2)
  for each in issues
)}];
export default ISSUES;
'''

DEST = SRC / "issues-config.js"
with open(DEST, "w") as dest:
  dest.write(content)
