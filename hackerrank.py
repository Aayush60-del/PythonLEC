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

name = "ius"
marks = 90
list = [[name , marks],["deol",90],["chetan",60],["aniket",45,"ima"] ,5]
print(list[0][0] , list[0][1])
print(list[1][0] , list[1][1])
print(list[2][0] , list[2][1])
print(list[3][0] , list[3][1] , list[3][2])
print(list[4])
