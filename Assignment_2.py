name = input("Enter vendor name: ")
year = input("Enter year of association: ")
contact = input("Enter contact number: ")
email = input("Enter email ID: ")

total = 0
for i in range(12):
    amt = float(input("Enter monthly purchase amount: "))
    total = total + amt

print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact:", contact)
print("Email:", email)
print("Annual Purchase:", total)
