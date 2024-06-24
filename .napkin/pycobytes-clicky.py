# Archived from <napkin.io>
# 24 June 2024

import json
import time

from napkin import (
    request as REQUEST,
    response as RESPONSE,
    store as STORE,
)


def process_request():
    try:
        process = METHODS[REQUEST.method]
        process()
    except:
        RESPONSE.status_code = 500
        raise
    else:
        RESPONSE.status_code = 200


def handle_get():
    '''Handle a GET request.'''

    RESPONSE.body = {
        "clickCount": STORE.get("clickCount")["data"],
        "lastClick": STORE.get("lastClick")["data"],
    }


def handle_post():
    '''Handle a POST request.'''

    current = STORE.get("clickCount")["data"]
    STORE.put("clickCount", current +1)
    now = round(time.time())
    STORE.put("lastClick", now)

    # Also send back updated data
    handle_get()

    if RESPONSE.body["clickCount"] != current +1:
        raise ValueError("Click didn't save")


METHODS = {
    "GET": handle_get,
    "POST": handle_post,
}


process_request()

print(json.dumps(STORE.get_all()))
