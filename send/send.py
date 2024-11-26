print(">>> python / cleaning up build...")

import re


FILE = "core.html"


with open(FILE, "r") as source:
  content = source.read()
# with open(FILE, "rb") as source:
  # content = source.read().decode("utf-8")

replacements = {
  '<em><strong>':
    '<strong><code style="font-family: monospace; color: #9090f1;">',
  '</strong></em>':
    '</code></strong>',
  'class="language-py" style="':
    'class="language-py" style="font-family: monospace;',
  'line-height: 140%':
    'line-height: normal',
  'line-height: 22.4px':
    'line-height: normal',
}

rereplacements = {
  "font-family: ?'Source Sans Pro', ?sans-serif;":
    "font-family: 'Source Sans Pro', 'Segoe UI', sans-serif;",
}

for old, new in replacements.items():
  content = content.replace(old, new)

for pattern, repl in rereplacements.items():
  content = re.sub(pattern, repl, content)

with open(FILE, "w") as dest:
  dest.write(content)


print(">>> python / done!")
