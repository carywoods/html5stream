#!/usr/bin/env python3
import time
import json

print("Content-Type: application/json\n")
print(json.dumps({"serverTime": int(time.time())}))
