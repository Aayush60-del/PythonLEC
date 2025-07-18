

#Swapping of two numbers

a = 'h '
b = 7 
print("DATA TYPE OF A IS : " , type(a)) #console => str
print("DATA TYPE OF B IS : " , type(b)) #console => int
temp = a
a = b
b = temp

print("a :" , a )
print("b :" , b )
print(a,b)

# SEEING DATATYPE OF A VARIABLE -> syntax => type(var)
print("DATA TYPE OF A IS : " , type(a)) #console => int
print("DATA TYPE OF B IS : " , type(b)) #console => str

man = True
print("DATA TYPE OF MAN IS : " , man  , type(man)) #console => bool

com = complex(2 , 5)
print(com)
print("DATA TYPE OF COM IS : " , com , type(com))

#LIST -> list is collection of different data type which is seperated 
#by comma and enclosed in square bracket

#NOTE : LIST IS MUTABLE AND CAN BE MODIFIED AFTER CREATION

list1 = [5 , 2.3 , [4 , -6] , ["ius" , "chetan"]]
print(list1)

list2 = [4, -5 , "ius" , 9.4]
print("list -> " , list2)


#TUPLE ->  list is collection of different data type which is seperated 
#by comma and enclosed in PARENTHESIS

#NOTE : TUPLE IS IMMUTABLE AND CAN NOT BE MODIFIED AFTER CREATION

Tuple1 = (("peacock" , "hen") , ("tiger" , "lion"))
print("tuple -> " , Tuple1)
