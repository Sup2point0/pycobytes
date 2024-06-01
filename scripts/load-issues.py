'''
Load issues from `./issues/` into `issues.config.js` for SvelteKit to use when building the site routes.
'''

import os
import shutil
from datetime import date
from pathlib import Path


print(">>> Python / collecting issues...")


ROOT = Path(__file__).parent.parent.absolute()
LIB = ROOT / "site/src/lib"


## Load
files = (ROOT / "issues").glob("[0-9][0-9].md")
issues = []

ROUTE = LIB / "exported"
if not os.path.exists(ROUTE):
  os.mkdir(ROUTE)

DEST = ROOT / "site/src/lib/exported"
for file in files:
  name = str(int(file.stem))
  issues.append(name)

  shutil.copyfile(file, DEST / (name + ".md"))


## Save
update = date.today().strftime("%b %d")

content = f'''/// Issues Index
/// last auto-generated: {update}

export const ISSUES = [{",\n".join(issues)}];
'''

DEST = LIB / "issues.config.js"
with open(DEST, "w") as dest:
  dest.write(content)
  # A little scuffed, but it works well
