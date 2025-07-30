# Lists in Python => Mutable in Nature

name = "Ius Negi"
print(list(name)) 
print(list[name])
print(name.split())

marks = [3,5,6, "Harry" , True]
n = len(marks) + 1
print("length : " , n)
print(marks[0])
print(marks[1]) # marks[1] = 5
print(marks[2])
print(marks[3]) # marks[3] = ""
print(marks[4]) # marks[4] = True
marks[1] = 4 # List is mutable : initially marks[1] = 5 => marks[1] = 4
print(marks)

# IF a element is present in a list or not
def found_(find , *fruits):
   
    for i in fruits:
        if find == i:
           return 1
    return -1
        
result = found_("b" , ("a" , "b" , "c" , "d" , "e"))
if result == 1:
    print("Element is present in the list")
else:
    print("Element is not present in the list")
        

    # Python LIST Method => 

    # 1.FIND

    #FIND IN LIST
    mark = [1, 2,3,4,"5",6,7,8]

    if 5 in mark:
        print("yes")
    else:
        print("No")        

    names = ["IUS" ,"DEOL" , "CHETAN" , "PRABHAT" , "PUKHRAJ"]
    
    if "DEOL" in names:
        print("yes")
    else:
        print("NO")    

#same thing can be apply for string 
    if "ush" in "ayush":
        print("yes it is ")
    else:
        print("No it is not ")     

# 2. PRINT ALL ELEMENTS OF STRING

dog = "Bruno Negi"
print(list(dog)) # -> ['B', 'r', 'u', 'n', 'o']
print(list[dog]) # list['Bruno Negi']
print(dog.split()) # ['Bruno', 'Negi']
print(dog[:]) # Bruno Negi
print(dog[1:7:2]) # we can also use bound index position in string

#3. PRINT ALL ELEMENTS OF LIST(MUTABLE)
 
name3 = ["ius" , " deol" , "verma"]
print(name3) # ['ius', ' deol', 'verma']   
print(name3[1:]) # [' deol', 'verma']
name3[1] = "sukh"
print(name3)

# 4. JUMP INDEX METHOD => LIST 
num = [1,2,3,4,5,6,7,8,9]
print(num)
print(num[1:8])
print(num[1:8:2]) # [2 , 3->4(print) ,5->6(print) , 7->8(print)] => [2 , 4 , 6 ,8]
print(num[-8 : -1 : 2])

# 5. LIST COMPREHENSION => we can create a lsit on the fly
# In list comprehension I can also give some conditions.
lst = [i for i in range(5)] # [0, 1, 2, 3, 4]
print(lst) # [0, 1, 2, 3, 4]

lst = [i for i in range(10) if (i%2== 0 and i/2 ==1 or i%3==0 and i/3 == 1 or i%5==0 and i/5 == 1 or i%7 ==0 and i/7==1 and i%2 !=0 and i%3 !=0 and i%4 != 0 and i%5 !=0 and i%6 !=0 and i%7 != 0 and i%8 !=0 and i%9 != 0 and i%10 != 0 )] # [0, 3, 6, 9] 
print(lst)

list_ = [i*i for i in  range(5)] # [0*0 -> 1*1 -> 2*2 -> 3*3 -> 4*4]
print(list_) 





upto = 1
a = 1 
while a <= 5:
    b  = 1
    while b <= upto:
        print("*" , end = "")
        b += 1
print()     
upto += 1        
a += 1
