import time
import os

# Make sure the directory exists
os.makedirs("logs", exist_ok=True)

with open("logs/output.log", "a") as f:
    for i in range(5):
        f.write(f"Log entry {i} at {time.ctime()}\n")
        time.sleep(1)
