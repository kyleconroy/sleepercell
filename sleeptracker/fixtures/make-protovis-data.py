import json
import argparse
import random
from datetime import datetime
from datetime import date
from datetime import timedelta

parser = argparse.ArgumentParser(description="Generate random sleep data to test with")
parser.add_argument('-d', '--days', type=int, default=100)
args = parser.parse_args()

end = datetime.now()

states = []

for i in range(args.days):
    if i % 2 == 0:
        # Awake
        delta = random.randrange(13, 40)
        end = end - timedelta(hours=delta)
    else:
        # Asleep
        delta = random.randrange(3, 10)
        start = end - timedelta(hours=delta)
        start_minutes = start.hour * 60 + start.minute
        end_minutes   = end.hour * 60 + end.minute
        if start.day == end.day:
            states.append({"x":i, "y":start_minutes, "z":end_minutes})
        else:
            states.append({"x":i, "y":0, "z":end_minutes})
            states.append({"x":i-1, "y":start_minutes, "z":1440})

states.reverse()
print json.dumps(states)
