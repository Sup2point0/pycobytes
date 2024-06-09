'''
Collect SCSS files that should be applied globally into `scss-config.js` for Svelte when preprocessing.
'''

import os
import shutil
from datetime import date
from itertools import chain as ichain
from pathlib import Path


print(">>> Python / pre-preprocessing SCSS...")


ROOT = Path(__file__).parents[2].absolute()
SRC = ROOT / "site/src"


## Load
files = ichain(
  SRC.glob("styles/_*.scss"),
  SRC.glob("mixins/_*.scss"),
)

config = []

for file in files:
  with open(file, "r") as source:
    for i in range(4):
      line = source.readline()
      if "[#pyconfig global]" in line.casefold():
        break
    else:
      continue

  config.append(file)


## Save
update = date.today().strftime("%b %d")
uses = (
  f"@use './src/{file.parent.stem}/{file.stem}' as *;"
  for file in config
)

content = f'''/// SCSS Globals
/// last auto-generated: {update}

const scssConfig = `{"\n".join(uses)}`;

export default scssConfig;
'''

DEST = ROOT / "site/scss-config.js"
with open(DEST, "w") as dest:
  dest.write(content)
