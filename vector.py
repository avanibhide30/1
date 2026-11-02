import csv

processes = ["P1", "P2", "P3"]

clock = {
    p: [0, 0, 0] for p in processes
}

messages = {}
events = {}

with open("vector.csv", "r") as f:
    data = csv.DictReader(f)

    for row in data:

        eid = row["event_id"]
        p = row["process_id"]
        action = row["event_action"]
        target = row["target_process"]

        i = processes.index(p)

        if action == "SEND":

            clock[p][i] += 1

            messages[(p, target)] = clock[p].copy()

        elif action == "RECEIVE":

            received = messages[(target, p)]

            clock[p] = [
                max(a, b)
                for a, b in zip(clock[p], received)
            ]

            clock[p][i] += 1

        else:
            clock[p][i] += 1

        events[eid] = clock[p].copy()

        print(eid, ":", clock[p])

# Compare events
def compare(a, b):

    less = all(x <= y for x, y in zip(a, b))
    strict = any(x < y for x, y in zip(a, b))

    if less and strict:
        return "CAUSALLY PRECEDES"

    if a == b:
        return "SAME TIME"

    return "CONCURRENT"

print("\nEvent Comparisons:")

ids = list(events)

for i in range(len(ids)):
    for j in range(i + 1, len(ids)):

        a, b = ids[i], ids[j]

        print(a, b, ":", compare(events[a], events[b]))