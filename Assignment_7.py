# Lab Assignment 1
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2

def mod(n1, n2):
    return n1 % n2

while True:
    print("\n--- CALC MENU ---")
    print("a) Addition")
    print("b) Subtraction")
    print("c) Multiplication")
    print("d) Division")
    print("e) Modulus")
    print("f) Exit")
    
    choice = input("Enter your choice: ").lower()
    
    if choice == 'f':
        break
        
    if choice in ['a', 'b', 'c', 'd', 'e']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == 'a':
            print("Result:", add(num1, num2))
        elif choice == 'b':
            print("Result:", sub(num1, num2))
        elif choice == 'c':
            print("Result:", mul(num1, num2))
        elif choice == 'd':
            print("Result:", div(num1, num2))
        elif choice == 'e':
            print("Result:", mod(num1, num2))
    else:
        print("Invalid Choice!")


#Lab Assignment-2: Bank Account Details

balance = 0.0

def show_balance():
    print("Current Balance: ", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit Successful.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print("Withdrawal Successful.")

while True:
    print("\n--- BANK ACCOUNT MENU ---")
    print("a) Display Balance")
    print("b) Deposit")
    print("c) Withdraw")
    print("d) Exit")
    
    choice = input("Select an option: ").lower()
    
    if choice == 'a':
        show_balance()
    elif choice == 'b':
        deposit()
    elif choice == 'c':
        withdraw()
    elif choice == 'd':
        break
    else:
        print("Invalid Option!")