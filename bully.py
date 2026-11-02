import csv

nodes = []

with open("bully.csv", "r") as f:
    data = csv.DictReader(f)

    for row in data:
        nodes.append({
            "id": int(row["node_id"]),
            "alive": row["is_alive"] == "TRUE"
        })

# Initiating node
initiator = 2

higher = [
    n for n in nodes
    if n["id"] > initiator and n["alive"]
]

print("Node", initiator, "initiates ELECTION")

if higher:
    for n in higher:
        print("ELECTION sent to", n["id"])
        print("OK received from", n["id"])

    leader = max(n["id"] for n in nodes if n["alive"])

else:
    leader = initiator

print("\nHighest alive node:", leader)
print("COORDINATOR message broadcast")