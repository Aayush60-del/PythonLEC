print("today's topic is Strings in python")

# 😮‍💨 Multiple String -> ('''   ''')if a breif paragrhap is given->triple single commas


apple = ''' he said, 
hii sir
\ "hello"apple is a fruit" '''
print(apple)


st = '''  ChatGPT is an advanced AI chatbot developed by OpenAI, designed to assist users with a wide range of queries through natural language processing and conversational responses.
Overview of ChatGPT
ChatGPT is built on large language models and is capable of understanding and generating human-like text. It can assist with various tasks, including writing, brainstorming, learning, and problem-solving. Users can interact with ChatGPT through text or voice, making it versatile for different applications. 
OpenAI
+1
Key Features
Conversational AI: ChatGPT can engage in real-time conversations, providing answers and insights on a multitude of topics. 
2
Image Generation: Users can request the generation of images based on textual descriptions, thanks to integration with OpenAI's DALL-E mo
'''
print(st)


name1 = "Aayush"
# 😮‍💨 print((name1[6])) throws an error
print("we know lenght is : 6")
for i in range(6):  #if we know the length of the name -> 6
    print(name1[i]) #name[i] 0->1->2->3->4->5


print("here we don't know the lenght")
# 😮‍💨 If we don't know the length of the name->spaces/characteres/symbols in a string
name2 ="  iu s ne+gi" # in this string there is some space
for j in name2:
    print(j) #ouput: it will also print the space and signs


    # 😮‍💨  STRING SLICING 

    #string slicing is used to get a subset of characters from a string
# ayu is subset of ayush

#SYNTAX => VAR_NAME[STARTING POINT : ENDING POINT]

    naam = "ayush,negi"
    print(naam[0 : 5]) #output : ayu

    #To find length of a string -> len(var_name) : function
    print("length of the string " + naam + "is " , len(naam))
    fruit = "apple"
    print("apple is a fruit of length " + str(len(fruit)))
    print(fruit[0 : 3])
    print(fruit[:4]) #if we don't specify first point it will take 0 as default
    
    #😮‍💨 NEGATIVE SLICING 
    state = "Uttrakhand"
    print("lenght of state : " , len(state)) #lenght = 10
    print(state[-3 : -1]) #python-> 10 -3 : 10 -1 => print(state[7 : 9])


name = "bruno"
print(name[0 :3])

value1 = int(input("enter a value")) #input is a function which by default takes a string
value2 = int(input("enter a second value"))

print(value1 + value2) 

# 😮‍💨  STRING METHOD -> UPPER / LOWER CASE

# Strings are immutable and when we do upper/ lower case it creates a new string and returns it

car = "thar"
print(car.upper()) # -> THAR
print(car.lower()) # -> thar

#  😮‍💨 rstrip() -> method of string
# it removes the trailing spaces or symbols from the string-> var_name.rstrip("symbols" + "symbols")

fruit = "Pineapple!!!!!!!!"
print(fruit.rstrip("!"))

hero = "batman!!!!#!@@@"
print(hero.rstrip("!" + "@" + "#"))

# 😮‍💨  REPLACE METHOD-> var_name.replace("jsiko ", "jisse")
hero2 = "IRONMAN"
print(hero2.replace(("IRON") , "BAT")) # -> BATTMAN



#😮‍💨 if a string is give hello world and we print it by using list(string) method
# it will print each character of the string as a list item

str = "hello world"
print(list(str))

a = "ice" 
b = "blue"
print(tuple(a) + tuple(b))


# 😮‍💨 SPLIT METHOD -> IT WILL SPLIT THE WORDS ✅ (only valid if there is space btw words)
#eg -> there is a string of  "Hello World"
# print(str.split()) => ["Hello" , "World"]

a = "hello sir"
print(a.split())

# 😮‍💨 Capitalize Method -> it will capitalize the first letter of the string and make the rest of the string in lower case

a = "ayush neGI"
print(a.capitalize()) # -> Ayush
print(a.split())
print(list(a))

# 😮‍💨 CENTER METHOD -> 
a = "bruno"
print(a.capitalize())
print(a.center(20)) # -> Bruno  (it will add spaces on both sides to mak

# 😮‍💨 COUNT METHOD -> it will count the number of times a char/word is repeated in the string

name = "Ayush negi aaayush is not"
print(name.count("yush"))
print(name.count("y"))


# 😮‍💨 ENDSWITH() METHOD-> it will check if the string ends with the given word or character or symbol
#if yes return true else false

uni = "Chandigarh University."
print(uni.endswith("!")) # return false

print(uni.endswith(".")) # return true

# 😮‍💨 FIND() METHOD -> IT WILL FIND THE WORD IN THE STRING AND
#  RETURN THE FIRST PRIOR INDEX POSITION OF THAT WORD.
name = "hello my name is ayush"
print(name.find("name")) # return 9 -> name first prior index pos of n : 9