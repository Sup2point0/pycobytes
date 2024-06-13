'''
Collect SCSS files that should be applied globally into `scss-config.js` for Svelte when preprocessing.
'''

print("           / pre-preprocessing SCSS...")

import os
import shutil
from datetime import date
from pathlib import Path

from __main__ import ROOT


SRC = ROOT / "site/src"


## Load
files = SRC.glob("styles/*.scss")
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
