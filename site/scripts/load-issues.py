'''
Load issues from `./issues/` into `issues.config.js` for SvelteKit to use when building the site routes.
'''

import os
import shutil
from datetime import date
from pathlib import Path


print(">>> Python / collecting issues...")


ROOT = Path(__file__).parent.parent.absolute()
SRC = ROOT / "site/src"


## Load
files = (ROOT / "issues").glob("[0-9][0-9].md")
issues = []

ROUTE = SRC / "exported"

if not os.path.exists(ROUTE):
  os.mkdir(ROUTE)

DEST = SRC / "exported"
FIELDS = ["index", "title", "date", "topic"]

for file in files:
  name = str(int(file.stem))
  issues.append(name)

  ## PARSE
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
          fields[field] = value

  if not live:
    continue

  front = f'''---
    index: {fields["index"]}
    title: {fields["title"]}
    date: {fields.get("date", None)}
    topic: {fields.get("topic", None)}
---
'''

  with open(file, "w") as source:
    source.seek(0)
    source.write(front)

  shutil.copyfile(file, DEST / (name + ".svx"))


## Save
update = date.today().strftime("%b %d")

content = f'''/// Issues Index
/// last auto-generated: {update}

export const ISSUES = [{",\n".join(issues)}];
'''

DEST = SRC / "issues.config.js"
with open(DEST, "w") as dest:
  dest.write(content)
  # A little scuffed, but it works well
