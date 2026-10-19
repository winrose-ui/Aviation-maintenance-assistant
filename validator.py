import json

REQUIRED_FIELDS = [
    "record_id",
    "date",
    "task",
    "technician_id",
]

def validate_record(record):
    issues = []

    for field in REQUIRED_FIELDS:
        if not record.get(field):
            issues.append(f"Missing required field: {field}")

    if record.get("fictional_test_data") is not True:
        issues.append("Record is not clearly marked as fictional test data")

    return {
        "record_id": record.get("record_id", "UNKNOWN"),
        "status": "FLAGGED" if issues else "PASS",
        "issues": issues,
    }

def validate_dataset(filename="sample_logs.json"):
    with open(filename, "r", encoding="utf-8") as file:
        records = json.load(file)

    results = [validate_record(record) for record in records]

    for result in results:
        print(f'{result["record_id"]}: {result["status"]}')
        for issue in result["issues"]:
            print(f"  - {issue}")

    return results


if __name__ == "__main__":
    validate_dataset()
