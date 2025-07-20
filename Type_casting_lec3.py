print("today's topic is type casting")

# type casting

    # Method 1

a = "1" # string
b ="2" #string

a = 1  #int
b = 2  #int

a = "harry"
b = "coder"
print(a + b) #output: harrycoder

#Method 2 
#In python there are different types of methods or functions
# int() / float() / str() / hex() / oct() / list() 
# tuple() / dict() / set() / bool() / complex()


#EXPLICT TYPE CASTING
a = "3" # a and b are string
b = "5"
print(a + b) # -> 35
print(int(a) + int(b)) # phele a ko int mai convert krega aur phir b ko int mai
print(list(a) + list(b)) # closed bracket
print(str(a) + str(b)) 
print(tuple(a) + tuple(b)) #open bracket
print(complex(a + b) + complex(b + a)) #complex number

C = 4.5 #float
D = 4
print(int(C) + D) # c(4.5) -> integer(4)







#USER__INPUT

# Syntax : Var_name = data_type(input("write"))

name = str(input("Enter your name")) 
print("your name is",name) #output: your name is harry 
print("hello " , name) # (+) and (,) both are valid

x = input("enter first number") #input is always takes string
y = input("enter second number")
print(x + y) #output: xy -> concatenate the string


# Syntax : Var_name = data_type(input("write"))
m = int(input("enter first number")) 
n = int(input("enter second number"))
print(m+n)

