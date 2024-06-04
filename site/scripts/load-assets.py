'''
Copy project assets from `./assets` to `static/` for SvelteKit to use when building the site.
'''

import os
import shutil
from itertools import chain as ichain
from pathlib import Path


print(">>> Python / collecting assets...")


ROOT = Path(__file__).parents[2].absolute()


## Load
SOURCE = ROOT / "assets"

assets = ichain(
  SOURCE.glob("**/*.png"),
  SOURCE.glob("**/*.jpg"),
  SOURCE.glob("**/*.jpeg"),
)


## Save
DEST = ROOT / "site/static"
if not os.path.exists(DEST):
   os.mkdir(DEST)

for file in assets:
  shutil.copyfile(file, DEST / file.name)
