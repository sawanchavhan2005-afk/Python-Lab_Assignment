name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
dept = input("Enter department: ")
basic = float(input("Enter basic salary: "))

da = basic * 0.92
hra = basic * 0.58
ta = basic * 0.30
lic = 500

gross = basic + da + hra + ta
net = gross - lic

print("Name:", name)
print("ID:", emp_id)
print("Department:", dept)
print("Net Salary:", net)