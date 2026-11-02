import csv
import threading
import time

lock = threading.Lock()
completed = []

def process_task(row):

    task = row["task_id"]
    worker = row["thread_name"]
    burst = int(row["burst_ms"])

    print(worker, "waiting for lock")

    with lock:
        print(worker, "acquired lock")
        print("Processing", task)

        time.sleep(burst / 1000)

        completed.append(task)

        print(worker, "released lock")

threads = []

with open("tasks.csv", "r") as f:
    data = csv.DictReader(f)

    for row in data:
        t = threading.Thread(
            target=process_task,
            args=(row,)
        )

        threads.append(t)
        t.start()

# Wait for all threads
for t in threads:
    t.join()

print("\nCompleted Tasks:", completed)