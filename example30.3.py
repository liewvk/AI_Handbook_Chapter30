from datetime import date
import csv

entry = {
    "date": date(2026, 11, 22).isoformat(),
    "topic": "Document retrieval",
    "result": "Compared 5 test questions",
    "next_step": "Improve missing-source handling",
}
filename = "ai_learning_journal.csv"
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=entry.keys())
    writer.writeheader()
    writer.writerow(entry)
print(f"Saved 1 entry to {filename}")

