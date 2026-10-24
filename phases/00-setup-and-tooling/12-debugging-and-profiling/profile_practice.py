import time


def load_data():
    time.sleep(0.3)
    return [10, 20, 30]


def calculate(values):
    return sum(values) / len(values)


values = load_data()
print(calculate(values))