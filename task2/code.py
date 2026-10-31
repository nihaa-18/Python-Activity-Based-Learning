n = int(input("Enter months: "))
b = []
for i in range(n):
    u = int(input("Enter units: "))
    c = u*2 if u<=100 else 200+(u-100)*3 if u<=200 else 500+(u-200)*5
    bill = (c+50)*1.05
    if u < 100: bill *= 0.95
    b.append(bill)
    print("Bill:", round(bill, 2))
for i in range(1,n):
    p = (b[i]-b[i-1])/b[i-1]*100
    print("Unusual increase!" if p>20 else "Normal bill")
