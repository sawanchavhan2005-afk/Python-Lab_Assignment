#Lab Assignment 1

s = input("Enter a string: ")

v = 0
c = 0
sp = 0
low = 0

for ch in s:
    if ch in "aeiouAEIOU":
        v += 1
    elif ch.isalpha():
        c += 1
    if ch == " ":
        sp += 1
    if ch.islower():
        low += 1

print("Number of Vowels:", v)
print("Number of Consonants:", c)
print("Number of Spaces:", sp)
print("Number of Lowercase Letters:", low)

#Lab Assignment 2

lines = []

print("Enter lines (type END to stop):")

while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

for i in lines:
    print(i.upper())


