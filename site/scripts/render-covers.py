'''
Render covers for each issue.
'''

print("           / rendering covers...")

import imgkit

from __main__ import ROOT


SRC = ROOT / "site/src"
DEST = ROOT / "assets/covers"

with open(SRC / "cover.html", "r") as source:
  content = source.read()


def render_cover(issue: dict):
  render = content.format(
    issueIndex = issue["issueIndex"],
    titleText = issue["title"],
    releaseDate = issue["date"],
  )
  
  imgkit.from_string(render, DEST / (issue["name"] + ".png"))


with open(SRC / "issues-config.json", "r") as source:
  issues = json.load(source)

for each in issues:
  render_cover(each)
