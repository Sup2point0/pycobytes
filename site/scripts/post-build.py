'''
Cleanup and configuration after SvelteKit finishes building.
'''

import os
from pathlib import Path


print(">>> Python / cleaning up...")


ROOT = Path(__file__).parents[2].absolute()
BUILD = ROOT / "site/build"

os.rename(BUILD / "fallback.html", BUILD / "404.html")


print(">>> Python / done!")
