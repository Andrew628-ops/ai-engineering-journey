# grid = [[0, 0]] * 2
# grid[0][0] = 1

# print(grid)


# grid = [[0, 0] for _ in range(2)]
# grid[0][0] = 1

# print(grid)

# numbers = [1, 2, 3, 4]
# result = [number ** 2 for number in numbers if number > 2]

pairs = [("apple", 3), ("banana", 5), ("orange", 2)]

for name, count in pairs:
    print(f"{name}: {count}")


scores = [("Alice", 80), ("Bob", 90)]
for name, count in scores:
    print(f"{name} scored {count}")


def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print(add_item("apple"))
print(add_item("banana"))

def scale(value, factor=2):
    return value * factor


print(scale(3))
print(scale(3, factor=4))



def make_multiplier(factor):
    def times_ten(value):
        return value * factor
    return times_ten


times_ten = make_multiplier(4)
print(times_ten(10))