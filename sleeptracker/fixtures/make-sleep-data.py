import json
import argparse
import random
from datetime import datetime
from datetime import date
from datetime import timedelta

parser = argparse.ArgumentParser(description="Generate random sleep data to test with")
parser.add_argument('-d', '--days', type=int, default=100)
args = parser.parse_args()

end = datetime(2011, 2, 23, 23)

states = []

for i in range(args.days):
    if i % 2 == 0:
        delta = 16 
        state = 1
    else:
        delta = 8 
        state = 0
    start = end - timedelta(hours=delta)
    states.append({
            "pk": i, 
            "model": "sleeptracker.sleepstate",
            "fields": {
                "user": 1,
                "state": state,
                "start": str(start),
                "end": str(end),
                },
            })
    end = start

states.reverse()
print json.dumps(states, indent=4)
