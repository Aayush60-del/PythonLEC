#   Q1  FACTORIAL
def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)

result = fact(5)
print("factorial :" , result)

#Q2 FIBO
def fib(n):
    if(n == 0):
        return 0
    elif(n==1):
        return 1
    return fib(n-1) + fib(n-2)
 
list_fibo = []
for i in range(7):
   sol = fib(i)
   list_fibo.append(sol)
print(list_fibo)   

#Q3
def fibom(n):
    if(n==1):
        return 1
    elif(n==2):
        return 2
    elif(n==3):
        return 3
    elif(n==0):
        return 0
    
    return fibom(n-1) + fibom(n-2) + fibom(n-3)

list_ = []

for i in range(1 , 7):
  ans = fibom(i)
  list_.append(ans)

print(list_)

