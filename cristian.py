import csv

with open("cristian.csv", "r") as f:
    data = csv.DictReader(f)

    for row in data:

        client = row["client_id"]

        t0 = float(row["t0_send_ms"])
        ts = float(row["t_server_ms"])
        t1 = float(row["t1_recv_ms"])

        # Round Trip Time
        rtt = t1 - t0

        # Estimated server time
        estimated = ts + (rtt / 2)

        # Clock offset
        offset = estimated - t1

        print("\nClient:", client)
        print("RTT:", rtt, "ms")
        print("Estimated Server Time:", estimated)
        print("Clock Offset:", offset)

        print("Adjusted Clock:", t1 + offset)