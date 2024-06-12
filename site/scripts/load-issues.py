'''
Load issues from `./issues/` into `issues-config.js` for SvelteKit to use when building the site routes.
'''

print(">>> Python / collecting issues...")

import json
import os
import shutil
from datetime import date
from pathlib import Path


ROOT = Path(__file__).parents[2].absolute()
SRC = ROOT / "site/src"


## Load
files = (ROOT / "issues").glob("[0-9][0-9].md")

DEST = SRC / "exported"
if not os.path.exists(DEST):
  os.mkdir(DEST)

issues = []
FIELDS = ["index", "title", "date", "topic"]


for file in files:
  with open(file, "r") as source:
    content = source.readlines()

  if not any(("#PYCO live!" in line) for line in content[:4]):
    continue

  meta = False
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
    continue

  issues.append({
    "name": file.stem,
    **fields,
  })

  index = fields["issueIndex"]

  front = f'''---
  issueIndex: {index}
  title: {fields["title"]}
  date: {fields.get("date", None)}
  topic: {fields.get("topic", None)}
---
'''

  with open(file, "r") as source:
    throwaway = source.readline()
    content = source.read()

  ROUTE = DEST / (index + ".svx")
  shutil.copyfile(file, ROUTE)

  with open(ROUTE, "w") as dest:
    dest.seek(0)
    dest.write(front + "\n" + content)

  # FIXME copy to _Content.svx for static routing
  ISSUES = SRC / "routes/issues"
  ROUTE = ISSUES / index

  if not os.path.exists(ROUTE):
    os.mkdir(ROUTE)

  with open(ISSUES / "-page.txt", "r") as source:
    script_tag = source.readline()
    content = source.read()

  shutil.copyfile(file, ROUTE / "_Content.svx")

  with open(ROUTE / "_Content.svx", "w") as dest:
    dest.seek(0)
    dest.write(front + "\n" + content)

  front = f'''import Content from "../{index}/_Content.svx";
const issue = ISSUES[{int(index) - 1}]
'''

  with open(ROUTE / "+page.svelte", "w+") as dest:
    dest.seek(0)
    dest.readline()
    dest.write("\n".join([script_tag, front, content]))


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
