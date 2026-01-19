import json

FILENAME = "input.json"


def task() -> float:
    with open(FILENAME) as f_1:
        python_obj = json.load(f_1)

    value = sum([i["score"] * i["weight"] for i in python_obj])
    return round(value, 3)

print(task())
