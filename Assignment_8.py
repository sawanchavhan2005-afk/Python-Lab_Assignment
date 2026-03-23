#Lab Assignment 1
source_file = "input.txt"
destination_file = "uppercase_output.txt"

with open(source_file, "r") as f:
    content = f.read()

upper_content = content.upper()

with open(destination_file, "w") as f:
    f.write(upper_content)

print("File converted to uppercase successfully.")

#Lab Assignment
src = input("Enter the source python file name (with .py): ")
dst = input("Enter the destination file name (with .py): ")

with open(src, "r") as f1, open(dst, "w") as f2:
    for line in f1:
        if not line.strip().startswith("#"):
            f2.write(line)

print("\n--- Content of Source File ---")
with open(src, "r") as f1:
    print(f1.read())

print("\n--- Content of Destination File (No Comments) ---")
with open(dst, "r") as f2:
    print(f2.read())

