'''
Transfer .md files from elsewhere in the repo to the site for SvelteKit to source content from during prerendering.
'''

print(">>> Python / collecting content...")

import json
from pathlib import Path


ROOT = Path(__file__).parents[2].absolute()


with open(ROOT / "site/content-config.json", "r") as source:
  routes = json.load(source)

for file, options in routes.items():
  with open(file, "r") as source:
    if "title" in options.get("strip", {}):
      source.readline()

    content = source.read()

    if "line-breaks" in options["strip"]:
      content.replace("\n<br>\n", "")
  
  with open(ROOT / options["dest"], "w") as dest:
    dest.write(content)
