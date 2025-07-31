# ✅sets : 1. A SET IS A COLLECTION OF WELL DEFINE OBJECTS +> WHERE DUPLICATION OBJECTS ARE RESTRICTED
# 2. declare in {CURLY BRACKETS}
# 3. SETS ARE IMUTABLE LIKE TUPLE 
# 4. SET CAN ACCESS DIFFERENT DATA TYPE
# 5. IN SET :  ORDER OF EXECUTION IS RANDOM
# 6. In set we cant use index position to get value of object at particular index.

#SYNTAX : VAR_NAME = {} 

s = {1,1,2,5,6,9,3,2,1} # HERE IS A SET 
print(s) # {1,2,3,5,6,9} -> AVOID DUPLICATION OF OBJECTS

s1 = {"ius" , "ius" , "deol" , "verma"}
# print(s1[0]) => IN SET WE CANT USE INDEX POSITION TO DEFINE AN OBJECT.
print(s1)

s2 = {"name" : "ius" , "age" : 15 , "department" : "CSE"}
print(s2)

#✅ USING FOR LOOP TO ACCESS ITMES IN SET
s8 = []
s7 = {1,9,2,4,6,7,8,3,1,2,5}
print("originally in set : " , s7)
for i in s7:
    s8.append(i)
print("new in list : " , s8)

# => IN SET : append(method) is restricted to use => we can't use append method in SET.
# s5 = {}
# for i in range(5):
#     value = int(input())
#     s5.append(value)
# print(s5)

#OUICK QUIZ : 

# IF THERE IS AN EMPTY SET AND I WANT TO KNOW ABOUT WHAT TYPE OF SET IS THIS :

ty = {} #EMPTY SET
print(type(ty))  #type => DICT

typ = set()
print(type(typ)) # type => SET

# 🙋‍♂️METHODS IN SETS(AVOID DUPLICATION OF OBJECTS) => 

s1 = {1,2,1,3,4,5,6,7,9}
s2 = {6,6,7,8,7,9,10,9}

#1.Union method 
print("s1 U s2 : " ,s1.union(s2))

#2.Intersection method
print("s1 intersection s2 : " , s1.intersection(s2))

#3. Difference method
print("A-B: " , s1-s2)
print("A.difference(B) ; ", s1.difference(s2) )

print("B-A : " , s2-s1)

#4. isdisjoint() method => when 2 set A and B don't have any common element
# no_common_element => True if common element is present => False

print(s1.isdisjoint(s2)) # FALSE


#5 issuperset() Method => when set A is superset of set B =>TRUE
print(s1.issuperset(s2)) # FALSE

#6. issubset() method

s3 = {1,2,3}
s4 = {1,2,3,4,5,6} 
print(s3.issubset(s4)) # TRUE

# 7. add method()

s3.add(11)
print(s3) # {11, 1, 2, 3}

#8. update method() =>add one set to another set.
s3.update(s4)
print(s3) # {1, 2, 3, 4, 5, 6, 11}

#9. remove method() / discard method() => remove an element from set.
s3.remove(11)
print(s3) # {1, 2, 3, 4, 5, 6} 

#10 POP method()
# AS WE KNBOW THAT SETS EXECUTION IS RANDOM SO USING POP METHOD WILL REMOVE LAST ELEMET N FROM SET
s3.pop()
print(s3) # {1, 2, 3, 4, 5,}
s3.pop()
print(s3)