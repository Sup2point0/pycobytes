# Archived from <napkin.io>
# 4 June 2024

from time import time

from napkin import (
    request as REQUEST,
    response as RESPONSE,
    store
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
        "clicks": store.get("clicks")["data"],
        "last-click": store.get("last-click")["data"],
    }


def handle_post():
    '''Handle a POST request.'''

    current = store.get("clicks")
    store.put("clicks", current +1)
    now = round(time.time())
    store.put("last-click", now)

    # Also send back updated data
    handle_get()

    if RESPONSE.body["clicks"] != current +1:
        raise ValueError("Click didn't save")


METHODS = {
    "GET": handle_get,
    "POST": handle_post,
}


process_request()
