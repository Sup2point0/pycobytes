print(">>> Python / cleaning up build...")

import re


FILE = "core.html"


with open(FILE, "r") as source:
  content = source.read()

replacements = {
  "<em><strong>":
    "<code style=\"font-family: monospace\">",
  "</strong></em>":
    "</code>",
  "class=\"language-py\" style=\"":
    "class=\"language-py\" style=\"font-family: monospace;",
  "line-height: 140%":
    "line-height: normal",
  "line-height: 22.4px":
    "line-height: normal",
  # ";height: 100%;":
  #   ";",
  # "line-height: 1.5;":
  #   "line-height: auto;",
  # "line-height: 22.4px;":
  #   "line-height: auto;",
}

rereplacements = {
  "font-family: ?'Source Sans Pro', ?sans-serif;":
    "font-family: 'Source Sans Pro', 'Segoe UI', sans-serif;",
  "font-family: ?'Rubik', ?sans-serif;":
    "font-family: 'Source Sans Pro', 'Segoe UI Semibold', sans-serif;",
}

for old, new in replacements.items():
  content = content.replace(old, new)

for pattern, repl in rereplacements.items():
  content = re.sub(pattern, repl, content)

with open(FILE, "w") as dest:
  dest.write(content)


print(">>> Python / done!")
