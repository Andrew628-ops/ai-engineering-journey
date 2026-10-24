import tracemalloc

tracemalloc.start()

data = [bytearray(1_000) for _ in range(1_000)]

snapshot = tracemalloc.take_snapshot()
for entry in snapshot.statistics("lineno")[:3]:
    print(entry)