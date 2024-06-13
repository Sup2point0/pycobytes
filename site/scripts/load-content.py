'''
Transfer .md files from elsewhere in the repo to the site for SvelteKit to source content from during prerendering.
'''

print("           / collecting content...")

import json
from pathlib import Path

from __main__ import ROOT


SITE = ROOT / "site"


with open(ROOT / "site/content-config.json", "r") as source:
  routes = json.load(source)


for file, options in routes.items():
  with open(file, "r") as source:
    if "title" in options.get("strip", {}):
      source.readline()

    content = source.read()

    if "line-breaks" in options.get("strip", {}):
      content = content.replace("\n\n<br>\n\n", "")
  
  with open(SITE / options["dest"], "w") as dest:
    dest.write(content)
