n = int(input("Enter number of chemicals: "))
rules = {"acid": 50, "base": 40, "solvent": 30}
stored, invalid = [], []
for i in range(n):
    name, cat, qty = input("Name category quantity: ").split()
    qty = int(qty)
    if cat not in rules or qty > rules.get(cat, 0) or (cat == "acid" and "base" in stored):
        invalid.append(name)
    else:
        stored.append(cat)
print("Valid chemicals:", stored)
print("Invalid chemicals:", invalid)
