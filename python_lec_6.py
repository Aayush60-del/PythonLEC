# Function with *args (tuple)
def sum_(*num):  # single * -> tuple (0,1,2,3,4,5)
    total = 0
    print(num)
    for i in num:
        print(i, end=" ")
        total += i
    print("\nsum is:", total)

sum_(5, 9, 2, 3, 7)

# Function with **kwargs (dictionary)
def naam(**name):  # double ** -> dictionary
    print("hello " + name["fname"] + " " + name["lname"])

naam(fname="ius", lname="negi")

# Function with regular arguments
def name(fname, mname, lname):
    print(fname, mname, lname)

name("ius", "singh", "negi")


input_string = "Hello, World!"
list(input_string)
print(list)

x = lambda a ,b : a+b                                                          
print(x(5,5))

