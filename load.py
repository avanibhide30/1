import csv

workers = ["W1", "W2", "W3"]
load = {w: 0 for w in workers}

with open("workload.csv", "r") as f:
    data = csv.DictReader(f)

    for i, row in enumerate(data):

        job = row["job_id"]
        units = int(row["compute_units"])

        # Round Robin allocation
        worker = workers[i % len(workers)]

        load[worker] += units

        print(
            job,
            "assigned to",
            worker,
            "| Units:",
            units
        )

print("\nFinal Worker Loads:")

for w, value in load.items():
    print(w, ":", value)