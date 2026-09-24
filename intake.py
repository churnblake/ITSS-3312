"""Week 2 practice: clean five raw case records and print a report."""

RAW_CASES = """  CARTER, DEMARCUS | m | 36 | 2018-03-22 | 412 larkmoor lane | beat 352 | OPEN  
reyes, miguel|M|32|2018-05-17| 3308 DELAFORD STREET |Beat 347|open
  OKAFOR, SAMUEL J | M | 55 | 2018-07-09 | 1519 westhollow avenue | beat 341 | OPEN
Nguyen, Daniel | m | 17 | 2018-04-03 | 2846 QUAIL RIDGE ROAD | beat 537 | Open  
  BOOKER, TERRENCE | M | 41 | 2018-11-08 | 907 n. calloway drive | Beat 442 | OPEN"""

REPORT_YEAR = 2026  # The lecture's example computes years through 2026.

print(f"{'CASE':<27}{'AGE':>5}{'YEARS UNSOLVED':>18}  {'DATE':<12} {'ADDRESS':<28} {'BEAT':<8} STATUS")

for record in RAW_CASES.splitlines():
    # Split on the pipe itself: record 2 has no spaces around its pipes.
    fields = [field.strip() for field in record.split("|")]
    name = fields[0].title()
    sex = fields[1].upper()
    age = int(fields[2])
    date = fields[3]
    case_year = int(date[:4])
    address = fields[4].title()
    beat = fields[5].title()
    status = fields[6].upper()
    years_unsolved = REPORT_YEAR - case_year

    case = f"{name} ({sex})"
    print(f"{case:<27}{age:>5}{years_unsolved:>18}  {date:<12} {address:<28} {beat:<8} {status}")
