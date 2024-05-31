'''
Load issues from `./issues/` into `issues.config.js` for SvelteKit to use when building the site routes.
'''

import json
from datetime import date
from pathlib import Path


print(">>> Python / collecting issues")


ROOT = Path(__file__).parent.parent.absolute()
ROUTE = ROOT / "site/src/lib/issues.config.js"


## Load
files = (ROOT / "issues").glob("[0-9][0-9].md")
issues = []

for file in files:
  name = str(int(file.stem))
  issues.append(name)

  with open(file, "r") as source:
    content = source.read()
  
  with open(ROOT / "site/src/export" / file.name, "w") as dest:
    dest.write(content)


## Save
update = date.today().strftime("%b %d")

content = f'''/// Issues Index
/// last auto-generated: {update}

export const ISSUES = [{",\n".join(issues)}];
'''

with open(ROUTE, "w") as dest:
  dest.write(content)
  # A little scuffed, but it works well


print(">>> python / done!")
