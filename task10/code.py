n = int(input("Enter number of households: "))
bills = []
for i in range(n):
    name = input("Household name: ")
    u = int(input("Enter water units: "))
    bill = min(u, 50)*2 + max(0, min(u-50, 50))*4 + max(0, u-100)*6
    bill += 50 + (100 if u > 100 else 0)
    bills.append((name, u, bill))
for name, u, b in bills:
    print(name, "Bill:", b, "Excessive" if u > 100 else "Normal")
print("Highest usage:", max(bills, key=lambda x: x[1])[0])
