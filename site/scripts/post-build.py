'''
Cleanup and configuration after SvelteKit finishes building.
'''

print(">>> Python / cleaning up...")

import os
from pathlib import Path


ROOT = Path(__file__).parents[2].absolute()
BUILD = ROOT / "site/build"

os.rename(BUILD / "fallback.html", BUILD / "404.html")


print("           / done!")
