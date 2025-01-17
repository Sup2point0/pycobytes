'''
We keep forgetting these, so now we’ll check before every issue is sent.
'''

import sys


def check(text: str):
  if not input(text):
    sys.exit()


check("Have we set the header links?")
check("Have we set the email preview text?")
check("Have we cc-d?")
