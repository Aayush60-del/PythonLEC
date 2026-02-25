
#Map : is used to conver data_types || list -> tuple | tuple -> list

list1 = [1,2,3]
#numbers inside list => string
a_ = list(map(str,list1))
print(a_)

list2 = ["1" , "2" , "3"]
b_ = list((map(int,list2)))
print(b_)

list3 = [1,2,3]
c_ = list(map(lambda x:x**2,list3))
print(c_)

#input().split() => 1. inputs are in one line 2.print(list4) => it will give the values in split
# list4 = input().split()
# print(list4)

# list5 = input().split()
# loc= list5[0]

n = int(input())
result = tuple(map(int,input().split()))
print(hash(result))

# 3713081631934410656
