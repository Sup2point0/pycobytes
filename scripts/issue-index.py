'''
Index issues into `issues.config.js` for SvelteKit to use when building the site routes.
'''

from datetime import date
from pathlib import Path


print(">>> python: running `issue-index.py`")


ROOT = Path(__file__).parent.parent.absolute()
ROUTE = ROOT / "site/src/lib/issues.config.js"


files = (ROOT / "issues").glob("[0-9][0-9].md")
issues = [str(int(file.stem)) for file in files]

update = date.today().strftime("%b %d")

content = f'''/// Issues Index
/// last auto-generated: {update}

export default ISSUES;
const ISSUES = [{",\n".join(issues)}];
'''

with open(ROUTE, "w") as source:
  source.write(content)
  # A little scuffed, but it works well


print(">>> python: done!")
