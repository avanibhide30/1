import csv

# Remote server functions
def processData(x):
    return x * 2

def calculateLoad(x):
    return x + 100

# Server method dispatcher
methods = {
    "processData": processData,
    "calculateLoad": calculateLoad
}

with open("rpc.csv", "r") as f:
    data = csv.DictReader(f)

    for row in data:
        client = row["client_name"]
        method = row["method_name"]
        value = int(row["param_value"])

        print("\n[DISPATCH]", client, "invoking", method)

        print("[SERVER EXECUTION] Processing:", value)

        if method in methods:
            result = methods[method](value)
            print("[RETURN] Result:", result)
        else:
            print("Method not found")