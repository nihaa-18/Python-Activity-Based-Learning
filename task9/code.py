w = float(input("Enter parcel weight: "))
d = int(input("Enter distance zone (1-3): "))
u = input("Enter urgency (normal/express): ")
r = input("Restricted parcel? (yes/no): ")
services = {"Speed": 50 + w*10*d, "Standard": 30 + w*8*d}
if r == "yes" or w > 20: services = {}
if u == "express": services.pop("Standard")
if services:
    best = min(services, key=services.get)
    print("Selected:", best, "Charge: Rs.", services[best])
else: print("No eligible courier service")
