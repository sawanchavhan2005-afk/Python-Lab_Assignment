# Practical No: 9
# Lab Assignment-1:
# Create a class Employee inherits it into another class Manager. Add methods to get input & print information of employees. Consider the attributes name, age, salary, address etc. process the information of 10 managers

class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0
        self.address = ""

    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    def show(self):
        print(self.name, self.age, self.salary, self.address)


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = ""

    def get_data(self):
        super().get_data()
        self.department = input("Enter department: ")

    def show(self):
        super().show()
        print(self.department)


managers = []
for i in range(10):
    m = Manager()
    m.get_data()
    managers.append(m)

for m in managers:
    m.show()








    # Practical No: 9
# Lab Assignment-2:
# Create a Library Management System with the following mechanisms:
# a) Design classes for Book, Member, and Library.
# b) Implement methods for adding books, lending books to members, returning books, and displaying book information.
# c) Create a menu-driven interface for the library management system.

class Book:
    def __init__(self, bid, title):
        self.bid = bid
        self.title = title
        self.issued = False


class Member:
    def __init__(self, mid, name):
        self.mid = mid
        self.name = name
        self.books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        bid = input("Book id: ")
        title = input("Title: ")
        self.books.append(Book(bid, title))

    def add_member(self):
        mid = input("Member id: ")
        name = input("Name: ")
        self.members.append(Member(mid, name))

    def lend(self):
        bid = input("Book id: ")
        mid = input("Member id: ")
        for b in self.books:
            if b.bid == bid and not b.issued:
                for m in self.members:
                    if m.mid == mid:
                        b.issued = True
                        m.books.append(b)
                        print("issued")
                        return
        print("not possible")

    def ret(self):
        bid = input("Book id: ")
        for m in self.members:
            for b in m.books:
                if b.bid == bid:
                    b.issued = False
                    m.books.remove(b)
                    print("returned")
                    return
        print("not found")

    def show_books(self):
        for b in self.books:
            print(b.bid, b.title, b.issued)


lib = Library()

while True:
    print("1 add book 2 add member 3 lend 4 return 5 show 6 exit")
    ch = input("enter choice: ")

    if ch == "1":
        lib.add_book()
    elif ch == "2":
        lib.add_member()
    elif ch == "3":
        lib.lend()
    elif ch == "4":
        lib.ret()
    elif ch == "5":
        lib.show_books()
    elif ch == "6":
        break
    else:
        print("invalid")