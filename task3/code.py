## 4. Source Code 

basic = float(input("Enter basic salary: "))
allow = basic * 0.20
overtime = float(input("Enter overtime amount: "))
incentive = float(input("Enter incentive: "))
gross = basic + allow + overtime + incentive
if gross <= 20000:
    deduction = gross * 0.05
else:
    deduction = 1000 + (gross-20000)*0.10
net = gross - deduction
print("Gross:", gross, "Deduction:", deduction, "Net Salary:", net)
