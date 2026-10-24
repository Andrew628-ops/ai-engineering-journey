import csv
import json
from dataclasses import dataclass


@dataclass
class Record:
    text: str
    label: int



with open("reviews.json", "w", encoding="utf-8") as file:
    json.dump([{"text": "Great movie", "label": 1}], file)


with open("reviews.json", "r", encoding="utf-8") as file:
    rows = json.load(file)


records = [Record(text=row["text"], label=row["label"]) for row in rows]
for record in records:
    print(record.text, record.label)




with open("reviews.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["text", "label"])
    writer.writeheader()
    writer.writerows(rows)
