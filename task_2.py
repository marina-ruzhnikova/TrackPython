import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f_1:
        lines = [line for line in csv.DictReader(f_1)]

    with open(OUTPUT_FILENAME, "w") as f_2:
        json.dump(lines, f_2, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
