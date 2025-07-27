

# Methods in list

# ✅ 1. list.append() METHOD => to insert new element to the end of the list

print("append method")
list1 = [4,2,8,1,3,6,7]
print(list1)
list1.append(5)
print(list1) 

print()

#2 ✅. list.insert() method=> to add element to the specific position

print("insert method")
list2 = [4,8,6,2,1,5,9]
print(list2) # [4, 8, 6, 2, 1, 5, 9]
list2.insert(2,1) #list2.insert(position , number_to_insert)
print(list2) # [4, 8, 1, 6, 2, 1, 5, 9]  

print()

#3 ✅. list.sort() method

print("sort method")
list3 =[2,4,6,1,3,9,7]
print(list3)
list3.sort()
print(list3)

#reverse = true (list.sort() in decending order)

print()

print("list in decending order")
list3.sort(reverse = True)
print(list3)

print()

# 4 ✅. list.reverse() method => to reverse the original list

print("Print the list in revese order")
name = ["ius" , "deol" , "chetan" ,"aniket" ,"pukhraj"]
print("original : " , name)
name.reverse()
print("Reverse : " , name)

# 5 ✅.  list.index() -> method : This method returns the index of element form the list

colours = ["violet" , "green" , "blue" ,"pink", "yellow" ,"orange"]
print(colours)
print("index position of yellow ",colours.index("yellow"))

print()

# we can also use it for string

Name = "Ayushnegi"
# ❌  Name.append("m")   # we can't append in string
print(Name)
print("index pos of n: " , Name.index("n"))

print()

#6 ✅. list.count() method => it will count the number of elements / character / word

para = '''arren Jason Watkins Jr. (born January 21, 2005), known online as IShowSpeed or simply Speed, is an American YouTuber, online personality, and online streamer. He is known for his dramatic and energetic behavior showcased in his variety live streams, as well as his in-real-life (IRL) streams in worldwide locations. He has been viewed as a cultural ambassador as his visits to countries often showcase their cultures and inventions to both domestic and international audiences.[2]

Registering his YouTube channel in 2016, Watkins first posted gaming content. He started gaining online attention in 2021, due to his provocative and energetic behavior such as barking and raging while gaming. He became a millionaire at age 16 and his first major purchase was a house for his mother.[3] In 2022, he began shifting focus towards soccer-related content, becoming an avid supporter of Cristiano Ronaldo, commonly revolving his content around his support for the player.[4][5]

Watkins has also pursued a rapping career. He signed with Warner Records to release his 2022 single "World Cup", which charted in several countries. He was named Breakout Streamer of the Year at the 12th Streamy Awards in 2022,[6][7] and Streamer of the Year at the 2024 Streamer Awards.[8][9] Watkins is considered one of the most popular online streamers and Internet personalities in the world '''



print("and appears : " , para.count("and"))
print("the appears : " , para.count("the"))
print("is appears : " , para.count("is"))

print()

# 7 ✅. list.copy() method -> it will copy the list

a = [1,2,3,4,5,6,7,8]
print(a)

b = a.copy()
print(b)
b[0] = 9
print("b : " ,b)
print("a : " , a)

print()

# 8. list_1.extend(list_2) method -> add 2 list

list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]
list_1.extend(list_2)
print(list_1)