'''
Load issues data from `./issues/` for SvelteKit to use when building.
'''

print("           / collecting issues...")

import json
import os
import re
import shutil
from datetime import date, datetime
from pathlib import Path

from __main__ import ROOT


class routes:
  src = ROOT / "site/src"
  export = src / "exported"
  issues = src / "routes/issues"



if not os.path.exists(routes.export):
  os.mkdir(routes.export)


FIELDS = {
  "index": "issueIndex",
  "title": "titleText",
  "date": "releaseDate",
  "topics": "topicTags",
}


def find_files() -> list[Path]:
  globbed = (ROOT / "issues").glob("[0-9][0-9].md")
  return list(globbed)


def extract_data(filepath: Path) -> dict | None:
  with open(file, "r") as source:
    content = source.readlines()

  if not any(("#PYCO live!" in line) for line in content[:3]):
    return

  meta = {
    "displayIndex": filepath.stem,
  }

  for line in content[:7]:
    if "-->" in line:
      break

    for field, key in FIELDS.items():
      if field in line:
        *_, value = line.partition("= ")
        value = value.strip()

        if field == "date":
          try:
            meta["unix"] = datetime.strptime(value, "%d %B %Y")
          except:
            return
        elif field == "topics":
          value = value.split(" / ")
        
        meta[key] = value

  content = render_svx(content, meta)
  
  return {
    "content": content,
    "meta": meta,
  }


def render_svx(content: list[str], meta: dict) -> str:
  content = "".join(content[1:])
  content = content.replace("\n\n<br>\n\n", "")
  content = content.replace("../assets/issues/", "/")

  front = f'''---
{"\n".join(f"{key}: {val}" for key, val in meta.items())}
---
'''
  
  return front + content


def sort_issues(issues: list) -> list:
  # issues = [each for each in issues if each["meta"]["unix"]]
  issues.sort(key = lambda each: each["meta"]["unix"])

  for i, issue in enumerate(issues):
    issue["meta"].pop("unix", None)
    issue["meta"]["orderIndex"] = i

  return issues


def save_svx(issue: dict):
  filename = issue["meta"]["displayIndex"] + ".svx"

  with open(routes.export / filename, "w") as dest:
    dest.write(issue["content"])


def save_static(issue: dict):
  ## _Content.svx
  route = routes.issues / issue["meta"]["issueIndex"]

  if not os.path.exists(route):
    os.mkdir(route)

  with open(route / "_Content.svx", "w") as dest:
    dest.write(issue["content"])

  ## +page.svelte
  with open(routes.issues / "-page.txt", "r") as source:
    content = source.read()

  content = re.sub(
    pattern = r"#{issueIndex}",
    repl = issue["meta"]["issueIndex"],
    string = content
  )
  content = re.sub(
    pattern = r"#{orderIndex}",
    repl = str(issue["meta"]["orderIndex"]),
    string = content
  )

  with open(route / "+page.svelte", "w") as dest:
    dest.write(content)


def save_json(data: dict):
  with open(routes.src / "issues-config.json", "w") as dest:
    json.dump(data, dest, indent = 2)


def save_js(data: dict):
  with open(routes.src / "issues-config.ts", "r") as source:
    content = source.read()

  load = json.dumps(data, indent = 2)

  content = re.sub(
    pattern = r"(#PYCO target! \*/ )\[.*\](;)",
    repl = r"\1" + "###" + r"\2",
    string = content,
    flags = re.DOTALL
  )
  content = content.replace("###", load)
  content = re.sub(
    pattern = r"\"(.*)\":",
    repl = r"\1:",
    string = content
  )

  content = re.sub(
    pattern = r"(Last auto-generated: ).*",
    repl = r"\1" + date.today().strftime("%b %d"),
    string = content
  )
  with open(routes.src / "issues-config.ts", "w") as source:
    source.write(content)


## Load
files = find_files()
issues = []

for file in files:
  data = extract_data(file)
  if data:
    issues.append(data)

## Save
issues = sort_issues(issues)

for issue in issues:
  save_svx(issue)
  save_static(issue)

## Config
data = [issue["meta"] for issue in issues]

save_json(data)
save_js(data)
