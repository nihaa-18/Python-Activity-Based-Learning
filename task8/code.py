n = int(input("Enter number of classes: "))
schedule, conflicts = [], []
for i in range(n):
    c, d, s, e, r = input("Course day start end room: ").split()
    for x in schedule:
        if d == x[1] and (s < x[3] and e > x[2] or r == x[4] and s < x[3] and e > x[2]):
            conflicts.append(c)
    schedule.append((c, d, s, e, r))
print("Conflicts:", conflicts)
print("Timetable:", "Invalid" if conflicts else "Valid")
