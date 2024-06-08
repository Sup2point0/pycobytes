'''
Transfer .md files from elsewhere in the repo to the site for SvelteKit to source content from during prerendering.
'''

print(">>> Python / collecting content...")

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).parents[2].absolute()


with open(ROOT / "site/content-config.json", "r") as source:
  routes = json.load(source)

for source, dest in routes.items():
  shutil.copy(ROOT / source, ROOT / dest)
