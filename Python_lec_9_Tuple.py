
print("TUPLE") # they are immutable in nature.

tup = (5,2,4,3,9,7)
print(type(tup) , tup)
print("index pos of 4 : " , tup.index(4) )
# tup.reverse()
# print("Reverse order :" , tup)
# tup.sort()
# print(tup)

print()

# We can change tuple in list format.

tup = list(tup)
print(tup)

print("sorting of a tuple in list format") # sorting of a tuple in list format
tup.sort()
print(tup)

print()

# We can also print all elements by using for loop.

tup1 = (1,2,3,4,5,6)
for i in tup1:
    print(i , end =" ")

# We can't change elements of tuple by assiging a value to it.
# tup2 = (1,7,2,4,8,8)
# tup2[2] = 9
# print(tup2)

# Output: TypeError: 'tuple' object does not support item assignment
# tup3 = (1,2,3,4,5,6)
# tup3.appends(7)
# print(tup3)

print() 
# Slice Method => Tuple
tup4 = [1,2,3,4,5,6,7,8,9]
print(tup4[2:5])

print()

tup5 = tup4[3:7]
print(tup5)

 #Jump method indexing =>Tuple 
print()
print(tup4[1:7:2])

num = (1,2,3,4,5,6,7,8,9)
print(len(num))

count = 0
for i in num:
    count +=1
print(count)    


#Operation on tuple:
countries = ("India" , "America" , "Spain" , "Canada" , "UK" ,"France")

countries = list(countries)

countries.append("Russia")
countries.pop(3)
countries[4] = "Africa"

countries = tuple(countries)
print(countries)


tup6 = (1,2,3,59,7,45,33,4,3,46,4,)
res = tup.index(3,0,5)
print(res)