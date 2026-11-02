import csv

nodes = []

with open("berkeley.csv", "r") as f:
    data = csv.DictReader(f)

    for row in data:
        nodes.append({
            "id": row["node_id"],
            "time": float(row["clock_time_sec"]),
            "faulty": row["is_faulty"] == "TRUE"
        })

# Remove faulty nodes
valid = [n for n in nodes if not n["faulty"]]

print("Polled clock times:")

for n in nodes:
    print(n["id"], n["time"])

# Calculate average
avg = sum(n["time"] for n in valid) / len(valid)

print("\nAverage clock:", avg)

# Calculate adjustment
for n in valid:
    adjustment = avg - n["time"]

    print(
        n["id"],
        "Adjustment:",
        adjustment,
        "seconds"
    )