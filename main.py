from tornado.gen import coroutine
import os.path as op
import json
from datetime import datetime
from pytz import timezone


@coroutine
def submit(handler):
    if op.isfile("data.json"):
        with open("data.json") as f:
            data = json.load(f)
    else:
        data = []
    payload = {'time': datetime.now(timezone('Asia/Kolkata')).isoformat()}
    payload.update({k: handler.get_argument(k) for k in handler.args})
    data.append(payload)
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)
    return {'status': 'success'}
