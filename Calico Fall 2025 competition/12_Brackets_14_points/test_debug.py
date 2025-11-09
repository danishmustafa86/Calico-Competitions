n = int(input())
events = []

for _ in range(n):
    name = input().strip()
    date = input().strip()
    year, month, day = map(int, date.split())
    events.append((name, year, month, day))

print(f"DEBUG: Read {len(events)} events", file=__import__("sys").stderr)

gta6_date = None
gta6_eve_date = None

for name, year, month, day in events:
    if "gta6" in name.lower() and "eve" not in name.lower():
        gta6_date = (year, month, day)
        print(f"DEBUG: Found gta6 at {gta6_date}", file=__import__("sys").stderr)
        break
    elif "gta6 eve" in name.lower():
        gta6_eve_date = (year, month, day)
        print(f"DEBUG: Found gta6 eve at {gta6_eve_date}", file=__import__("sys").stderr)

if not gta6_date and gta6_eve_date:
    year, month, day = gta6_eve_date
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
    print(f"DEBUG: Calculated gta6 date as {gta6_date}", file=__import__("sys").stderr)

print(f"DEBUG: Final gta6_date = {gta6_date}", file=__import__("sys").stderr)

if gta6_date:
    for name, year, month, day in events:
        print(f"DEBUG: Processing {name}", file=__import__("sys").stderr)
        if "gta6" in name.lower() and "eve" not in name.lower():
            print(f"DEBUG: Skipping {name}", file=__import__("sys").stderr)
            continue
        
        event_date = (year, month, day)
        
        if event_date < gta6_date:
            print(f"we got {name} before gta6")
        elif event_date > gta6_date:
            print(f"we got gta6 before {name}")
