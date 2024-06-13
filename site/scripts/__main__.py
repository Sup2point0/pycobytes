'''
Run scripts before SvelteKit builds.
'''

print(">>> Python / executing scripts...")

from pathlib import Path


ROOT = Path(__file__).parents[2].absolute()


__import__("load-content")
__import__("load-issues")
__import__("load-assets")
__import__("config-scss")
__import__("config-fonts")


print("           / done!")