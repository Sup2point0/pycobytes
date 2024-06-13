'''
Inject required fonts into `app.html`.
'''

print("           / configuring fonts...")

import re
from pathlib import Path

from __main__ import ROOT


SRC = ROOT / "site/src"
ROUTE = SRC / "app.html"


FONTS = [
  "Source+Sans+Pro:ital,wght@0,200..900;1,200..900",
  "Overpass:ital,wght@0,100..900;1,100..900",
  "Sniglet:wght@400;800",
  "Fira+Code:wght@300..700",
  "Roboto+Mono:ital,wght@0,100..700;1,100..700",
]

with open(ROUTE, "r") as source:
  content = source.read()

fonts = "css2?" + "&".join("family=" + each for each in FONTS) + "&display=swap"
content = re.sub(r"css2.*display=swap", fonts, content, 1)

with open(ROUTE, "w") as dest:
  dest.write(content)
