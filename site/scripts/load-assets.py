'''
Copy project assets from `./assets` to `static/` for SvelteKit to use when building the site.
'''

print("           / collecting assets...")

import os
import shutil
from itertools import chain as ichain
from pathlib import Path

from __main__ import ROOT



## Load
SOURCE = ROOT / "assets"

assets = ichain(
  SOURCE.glob("**/*.png"),
  SOURCE.glob("**/*.jpg"),
  SOURCE.glob("**/*.jpeg"),
  SOURCE.glob("**/*.svg"),
)


## Save
DEST = ROOT / "site/static"

if os.path.exists(DEST):
  shutil.rmtree(DEST)

if not os.path.exists(DEST):
  os.mkdir(DEST)

for file in assets:
  shutil.copyfile(file, DEST / file.name)
