import random
import json
from datetime import date, timedelta

# These are fictional test records, not real aircraft records.

TASKS = [
    "Fictional wiring inspection",
    "Training connector check",
    "Sample instrument observation",
    "Practice electrical continuity check",
]

def generate_log():
    start_date = date(2026, 1, 1)
    random_days = random.randint(0, 300)
    log_date = start_date + timedelta(days=random_days)

    record = {
        "record_id": f"TEST-{random.randint(1000, 9999)}",
        "date": log_date.isoformat(),
        "task": random.choice(TASKS),
        "technician_id": f"TRAINEE-{random.randint(1, 20):03}",
        "fictional_test_data": True,
    }

    # Occasionally remove a field so we can test our validator.
    if random.random() < 0.3:
        field_to_remove = random.choice(
            ["task", "technician_id"]
        )
        record.pop(field_to_remove)

    return record


def generate_dataset(number_of_records=20):
    return [
        generate_log()
        for _ in range(number_of_records)
    ]


if __name__ == "__main__":
    records = generate_dataset()

    with open("sample_logs.json", "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)

    print(f"Generated {len(records)} fictional test records.")
    print("Saved them to sample_logs.json")
