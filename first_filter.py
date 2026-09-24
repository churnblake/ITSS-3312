"""Week 3 practice: filter the raw cases and count the results."""

CURRENT_YEAR = 2026
STALE_YEARS = 5

# Put wk03_data_raw_cases_50.txt inside a data folder beside this script.
DATA_FILE = "data/wk03_data_raw_cases_50.txt"

total_records = 0
open_count = 0
stale_count = 0
juvenile_open_count = 0
oldest_open_year = CURRENT_YEAR
oldest_open_name = ""

print("FLAGGED OPEN CASES")
print(f"{'CASE':<28}{'AGE':>4}{'YEARS UNSOLVED':>17}  FLAG")

with open(DATA_FILE, encoding="utf-8") as case_file:
    for line in case_file:
        if line.strip() == "":
            continue  # Empty lines are not records.

        fields = [field.strip() for field in line.split("|")]
        if len(fields) != 7:
            continue  # Skip an incomplete or oddly formatted line.

        total_records += 1
        name = fields[0].title()
        sex = fields[1].upper()
        age = int(fields[2])
        year = int(fields[3][:4])
        status = fields[6].upper()
        years_unsolved = CURRENT_YEAR - year

        if status == "OPEN":
            open_count += 1
            if age < 18:
                juvenile_open_count += 1
            if year < oldest_open_year:
                oldest_open_year = year
                oldest_open_name = name
            if years_unsolved >= STALE_YEARS:
                stale_count += 1
                case = f"{name} ({sex})"
                print(f"{case:<28}{age:>4}{years_unsolved:>17}  *** STALE ***")

print()
print(f"Total records:        {total_records}")
print(f"Open cases:           {open_count}")
print(f"Stale (>= 5 yrs):     {stale_count}")
print(f"Juvenile open cases:  {juvenile_open_count}")
print(f"Oldest open case:     {oldest_open_name} ({oldest_open_year})")
