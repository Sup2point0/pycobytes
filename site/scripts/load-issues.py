'''
Load issues from `./issues/` into `issues-config.js` for SvelteKit to use when building the site routes.
'''

import json
import os
import re
import shutil
from datetime import date
from pathlib import Path


print(">>> Python / collecting issues...")


ROOT = Path(__file__).parents[2].absolute()
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

  content = "".join(content[1:])
  content = re.sub(r"../assets/issues/[0-9]*/", "/", content)

  issues.append({
    "name": file.stem,
    **fields,
  })

  front = f'''---
  issueIndex: {fields["issueIndex"]}
  title: {fields["title"]}
  date: {fields.get("date", None)}
  topic: {fields.get("topic", None)}
---

<script>
  import {{ base }} from "$app/paths";
</script>
'''

  ROUTE = DEST / (str(int(file.stem)) + ".svx")
  shutil.copyfile(file, ROUTE)

  with open(ROUTE, "w") as source:
    source.seek(0)
    source.write(front + "\n" + content)


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
