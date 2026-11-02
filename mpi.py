
import csv
import threading

with open("matrix_149.csv", "r") as f:
    data = list(csv.DictReader(f))

A = []
for row in data:
    A.append([
        int(row["col_0"]),
        int(row["col_1"]),
        int(row["col_2"]),
        int(row["col_3"])
    ])

B = list(zip(*A))
C = [None] * len(A)

def multiply(i):
    C[i] = [sum(x*y for x, y in zip(A[i], col)) for col in B]
    print("Worker", i, "completed")

print("MASTER: Scattering rows")

threads = []

for i in range(len(A)):
    t = threading.Thread(target=multiply, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nMASTER: Gathering results")
for row in C:
    print(*row)
