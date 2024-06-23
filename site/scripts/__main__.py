'''
Run scripts before SvelteKit builds.
'''

print(">>> Python / executing scripts...")

from pathlib import Path


ROOT = Path(__file__).parents[2].absolute()


__import__("load-content")
__import__("load-issues")
__import__("load-assets")

# NOTE only runs on local
try:
  __import__("render-covers")
except:
  pass

__import__("config-scss")
__import__("config-fonts")


print("           / done!")
