# # question 1
# ask
# You are given a string .
# Your task is to find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.
# Input Format
# A single line of input containing the string .
# Constraints
# Output Format
# Print the first occurrence of the repeating character. If there are no repeating characters, print -1.
# Sample Input
# ..12345678910111213141516171820212223
# Sample Output
# 1


# name1 = "__commit__"
# name = name1.strip("!" +  "@" + "#" +"$" +"%" +"^" +"&" +"*"+"()"+"-"+"="+"_"+"+"+"[]"+"{}"+";"+"/"+","+"<"+">"+"|")
# for i in list(name):
#  print(i , ":" , list(name).count(i))  # count() returns the number of occurrences of the specified value.  #
#  max = list(name).count(i)                                                                                                                                                                                             

# for j in list(name):
#  if(list(name).count(j) >= max):
#   a = j
#   max = list(name).count(j)

# print(a)
   
   



   
     

        
# x =int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# list1 = [(i , j , k) for i in range(x)  for j in range(y) for k in range(z) if(i + j + k) != n]   
# print(list1)

    
    
# n = int(input())
# values  = []
# for i in range(n):
#     value  = int(input())
#     values.append(value)

# Question 2 :
# def score_(n):

#    values  = []
#    for i in range(n):
#     value  = int(input())
#     values.append(value)
#    print(values) 
#    values = list(values)
#    values.sort(reverse = True)
#    max = values[0]
#    for i in range(len(values)):
#       if (max > values[i]):
#          return values[i]
         
# n = int(input())
# result = score_(n)
# if(result != -10):
#    print(result)


# Question 3:

# def records(n):
#    list_ = []

#    for i in range(n):
#       name_student = input()
#       score = int(input())
#       list = [name_student , score]
#       list_.append(list)
# print(list_)      

# records(2)
# def records(n):
#     if(n>=2 and n<=5):
#        list_ = []
#        for i in range(n):
#         name_student = input()
#         score = int(input())
#         list = [name_student,score]
#         list_.append(list)
#        print(list_)
#        for i in list_:
#           max_score = score[0]
#           if(max_score == score[i]):
#              return score[i]
             


# n = int(input())  
# result = records(n)
# print(result)

# list = [["deol",90],["chetan",90],["aniket",50,]]
# for i in list:
#     for j in list():   
#         if list[i][1] == list[j][1]:
#             print(list[i][1])
    
    


# def check(n):   
#      num_st = n
#      re = []
#      N = []
#      if (2<=num_st and num_st<=5):
#         for i in range(num_st):
#            name = input()
#            score = float(input())
#            records =[name,score]
#            re.append(records)
#         for i in range(len(re)):
#             N.append(re[i][1])

#         for j in range(len(N)):
#           for k in range(1, len(N)):
#             if N[j] == N[k]:
#               print(N[j])


     

              
# n = int(input())
# check(n)


# a = 1
# n = 1
# while n <= 5:

#     for i in range(upto):
#         print("",a,end = "")
#     print()   
#     upto +=1
#     n += 1

# print()


# print(a)
# for i in range(5):
#     j = 0
#     while j<=upto:
#         if(j==0 or j == upto):
#             print(a,end = "")
#         else:
#             print("2",end = "")
#         j+=1
#     upto +=1
#     print()

list = []
a = 0 
b = 1
i = 0
num = 1
upto = 1
for i in range(num):
    while i<= upto:
       c = a + b
       if(i == 0 or i == upto):
          list.append([c])
print(list)    
    

    
