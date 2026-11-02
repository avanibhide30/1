import csv

nodes = {}

with open("ring.csv", "r") as f:
    data = csv.DictReader(f)

    for row in data:
        nid = int(row["node_id"])

        nodes[nid] = {
            "next": int(row["next_node_id"]),
            "active": row["is_active"] == "TRUE"
        }

# Start election
start = 1
current = start
participants = []

print("Coordinator failed. Election started.")

# Circulate around ring
while True:

    if nodes[current]["active"]:
        participants.append(current)
        print("Token passed through:", current)

    current = nodes[current]["next"]

    if current == start:
        break

# Elect highest ID
leader = max(participants)

print("\nElection participants:", participants)
print("New Coordinator:", leader)
print("COORDINATOR message broadcast")