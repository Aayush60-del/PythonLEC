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
   
   



   
     

        
x =int(input())
y = int(input())
z = int(input())
n = int(input())

list1 = [(i , j , k) for i in range(x)  for j in range(y) for k in range(z) if(i + j + k) != n]   
print(list1)

    
    