#Methods in Dictionaries

ep1 ={87 : 75 , 88 : 80 , 89 : 85 , 90 : 90 }
ep2 = {75 : 94 , 10 : 60 , 33 : 78}

#1. Update Method => Add new key-value pair to dictionary
print("1. Update Method")
ep1.update(ep2)
print(ep1)

print()


#2. Clear Method => Remove all key-value pairs from dictionary
print("2. Clear Method")
ep3 ={ 1 : 2 , 3 : 4 , 5 : 6 }
ep3.clear()
print(ep3)

print()

#3. Copy Method: it will copy all the key-value pairs from the dictionary
print("3. Copy Method")
ep4 = ep1.copy()
print(ep4)

print()

#4. Pop Method : it remove the key-value pair from the dictionary.
# dict_name.pop(key_name) : it will remove the assign key-value pair.
print("4. Pop Method")
print(ep4)
ep4.pop(87)
print(ep4)

print()

#5. Popitem Method : it will delete the last key-value pair from the dictionary.
print("5. Popitem Method")
print(ep1)
ep1.popitem()
print(ep1)

print()

#6. del Method : it will also delete a assign key-value pair from the dictionary.
print("6. del Method")
print(ep4)
del ep4[88]
print(ep4)

l = {"Harry": 37.21,"Berry" : 37.21,"Tina":37.2, "Akriti" : 41 , "Harsh" : 39}
print("original : ",l)
list_ = list(l.values())
list_.sort()
print(list_)

l1 = {
    "Hina":
20,
"Shina":
20.1,
"Mina":
20.01,
"Tina":
20.001,
}
print(l1)
list1_ = list(l1.values())
list1_.sort(reverse = False)
print(list1_)
list2_ = list(l1.keys())
list2_.sort(reverse = True)
print(list2_[0])

 
M = [['A', 25.0], ['B', 10.0], ['C', 15.0]]
N = []
for i in range(len(M)):
    N.append(M[i][1])
print(N)
N.sort()
print(N)





        


    
        
     
    



