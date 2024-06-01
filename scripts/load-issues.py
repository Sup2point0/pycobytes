'''
Load issues from `./issues/` into `issues.config.js` for SvelteKit to use when building the site routes.
'''

import os
import shutil
from datetime import date
from pathlib import Path


print(">>> Python / collecting issues")


ROOT = Path(__file__).parent.parent.absolute()
LIB = ROOT / "site/src/lib"
DEST = LIB / "issues.config.js"
ROUTE = LIB / "exported"


## Load
files = (ROOT / "issues").glob("[0-9][0-9].md")
issues = []

if not os.path.exists(ROUTE):
  os.mkdir(ROUTE)

for file in files:
  name = str(int(file.stem))
  issues.append(name)

  dest = ROOT / "site/src/lib/exported" / (name + ".md")
  shutil.copyfile(file, dest)


## Save
update = date.today().strftime("%b %d")

content = f'''/// Issues Index
/// last auto-generated: {update}

export const ISSUES = [{",\n".join(issues)}];
'''

with open(DEST, "w") as dest:
  dest.write(content)
  # A little scuffed, but it works well


print(">>> python / done!")
