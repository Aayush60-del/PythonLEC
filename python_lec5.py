print("conditional statements")

# 1.💀 if / if - else statement
#2. 💀elif() statement => similar to else if statement in other languages

print("logical operators")
# 1. and operator => python(and) / other languages(&&)
#2. or operator => python(or) / other languages(||)
#3. not operator => python(not) / other languages(!)


a = 10

if(a > 0 and a <20):
    print("a is greater than 0 and less than 20")
else:
    print("a is not greater than 0 and less than 20")


#💀Match-Case Statement similar to switch case

print("online calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

n = int(input("Enter your choice:"))
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

match n:
    
    case 1:
        print("Addition :" , a + b)
    case 2:
        print("Subtraction :" , a - b)

    case 3:
        print("Multiplication :" , a * b)
    case 4:
        if(b != 0):
            print("Division :" , a / b)
    case 5:
        if(b != 0):
            print("Modulus :" , a % b)
    case _:
        print("Invalid choice")
        
print("\n")

#LOOPS =>
# 1.💀 for loop 

for i in range(5):  # i = 0 -> i = 4 : check (i < 5)
    print(i)
    if (i == 5):
        break

print("\n")

    # 💀In for loop we use break so that the for loop stop executing and and next while loop starts.
    #if we don't use break then it will print all the values from 0 to 4 and also the while loop will be executing at the same time



# 2.💀 while loop
i = 1
while i <= 5:
        print(i)
        i = i + 1

print("\n")

# 💀 Continue Statement.
#it will skip the current iteratiion when the condition is true and continue with the next iteration

for i in range(10):
    if(i == 5):
        continue #  skip the current iteration (i == 5)
    print(i)


    # 💀 Functions/Methods =>  syntax : def fun_name(parameters):
def add(x, y):
    print("Addition is:", x + y)

    add(1, 2)  # <-- This line is wrongly indented (inside function)


def isgreater(a,b):
    if(a<b):
        print("a is less than b")
    elif(a>b):
        print("a is greater than b")    

isgreater(10, 20) 


#PASS # statement is used when we don't want
#  to write anything in the body of the loop or function
def name():
    pass  # -> pass and process to the next line of code

# end = " " is used to print the next output on the same line
for n in range(1, 6):
    print("hello", n, end=" ")

list = [1,2,3,4,5]

n = len.list()
print(n)
