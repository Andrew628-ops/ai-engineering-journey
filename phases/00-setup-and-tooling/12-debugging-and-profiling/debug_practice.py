def average(values):
    if not values:
        raise ValueError("Cannot average an empty list")
    total = sum(values)
    count = len(values)
    return total / count


print(average([10, 20, 30]))
print(average([]))
