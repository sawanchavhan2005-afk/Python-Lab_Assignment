#Lab Assignment 1

n = int(input("Enter number of integers: "))

l = []
for i in range(n):
    x = int(input("Enter integer: "))
    l.append(x)

t = tuple(l)

print("Total items:", len(t))

print("Last item:", t[-1])

print("Reverse order:", t[::-1])

if 5 in t:
    print("Yes")
else:
    print("No")

t2 = t[1:-1]

t3 = tuple(sorted(t2))

print("After removing first and last and sorting:", t3)

#Lab Assignment 2

n = int(input("Enter number of items sold: "))

l = []
for i in range(n):
    price = float(input("Enter price: "))
    l.append(price)

t = tuple(l)

print("Total items sold:", len(t))

print("Cheapest item price:", min(t))

print("Costliest item price:", max(t))

print("Price list in ascending order:", tuple(sorted(t)))

count = 0
for i in t:
    if i > 1000:
        count += 1

print("Number of costly items sold:", count)

