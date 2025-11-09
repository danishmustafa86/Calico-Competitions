n = int(input())
events = []

for i in range(n):
    name = input().strip()
    date = input().strip()
    year, month, day = map(int, date.split())
    events.append((name, year, month, day))

gta6_date = None

# First pass: look for direct gta6 event or gta6 eve
for name, year, month, day in events:
    name_lower = name.lower()
    if "eve" in name_lower and ("gta" in name_lower or "6" in name_lower):
        # This is gta6 eve - calculate next day
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            days_in_month[1] = 29
        
        if day == days_in_month[month - 1]:
            if month == 12:
                gta6_date = (year + 1, 1, 1)
            else:
                gta6_date = (year, month + 1, 1)
        else:
            gta6_date = (year, month, day + 1)
        break
    elif "gta" in name_lower and "6" in name_lower:
        # This is gta6 itself
        gta6_date = (year, month, day)
        break

# Compare all events with gta6
if gta6_date:
    for name, year, month, day in events:
        name_lower = name.lower()
        # Skip gta6 itself (but not gta6 eve)
        if "gta" in name_lower and "6" in name_lower and "eve" not in name_lower:
            continue
        
        event_date = (year, month, day)
        
        if event_date < gta6_date:
            print(f"we got {name} before gta6")
        elif event_date > gta6_date:
            print(f"we got gta6 before {name}")
