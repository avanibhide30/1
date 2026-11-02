import csv

processes = ["P1", "P2", "P3"]

clock = {p: 0 for p in processes}
messages = {}
events = {}

with open("lamport.csv", "r") as f:
    data = csv.DictReader(f)

    for row in data:

        eid = row["event_id"]
        p = row["process_id"]
        action = row["event_type"]
        target = row["message_to"]

        if action == "SEND":

            clock[p] += 1
            messages[(p, target)] = clock[p]

        elif action == "RECEIVE":

            received = messages[(target, p)]

            clock[p] = max(clock[p], received) + 1

        else:
            clock[p] += 1

        events[eid] = clock[p]

        print(eid, p, "Clock:", clock[p])

# Sort events by logical timestamps
print("\nFinal Causal Order:")

ordered = sorted(
    events.items(),
    key=lambda x: (x[1], x[0])
)

for event, timestamp in ordered:
    print(event, ":", timestamp)