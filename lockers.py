"""Week 4 practice: deduplicate cases, profile ages, and rank beats."""

DATA_FILE = "data/wk04_data_raw_cases_dupes.txt"

normalized_records = []

with open(DATA_FILE, encoding="utf-8") as case_file:
    for line in case_file:
        if line.strip() == "":
            continue

        # Standardize case and spaces around every pipe before deduplicating.
        fields = line.strip().upper().split("|")
        clean_fields = []
        for field in fields:
            clean_fields.append(field.strip())
        normalized_records.append("|".join(clean_fields))

unique_records = set(normalized_records)
ages = []
per_beat = {}

# Sorting the set keeps processing order consistent between runs.
for record in sorted(unique_records):
    fields = record.split("|")
    age = int(fields[2])
    beat = fields[5].replace("BEAT", "").strip()
    status = fields[6]

    # Age statistics include every unique case, both open and closed.
    ages.append(age)

    if status == "OPEN":
        if beat in per_beat:
            per_beat[beat] += 1
        else:
            per_beat[beat] = 1

print(f"Lines in file:      {len(normalized_records)}")
print(f"Unique records:     {len(unique_records)}")
print(f"Duplicates removed: {len(normalized_records) - len(unique_records)}")
print(f"Youngest {min(ages)} / Oldest {max(ages)} / Average {sum(ages) / len(ages):.1f}")
print()
print("OPEN CASES PER BEAT")

# Begin with beat order so equal counts appear in ascending beat order.
ranked_beats = sorted(sorted(per_beat), key=per_beat.get, reverse=True)
for beat in ranked_beats:
    count = per_beat[beat]
    bar = "#" * count
    print(f"Beat {beat:<6}{count:>3}  {bar}")
