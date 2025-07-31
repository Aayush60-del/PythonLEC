# TODAY WE TALK ABOUT F - STRING


application = "Hello ! , i'm {} and i'm from {}."

#IN STRING FORMATIING : we assign inputs to the {} in the string
#IN F - STRING METHOD ORDER OF INPUTS MATTERS

#1. Indirect way

print("originally : ",application)
name = " Ayush"
country = "India"
print("New : ",application.format(name,country))

print() 

#IN F - STRING METHOD ORDER OF INPUTS MATTERS
print(application.format(country , name)) # India Ayush

#2.Direct Way

print()
 
print(application.format("Deol" , "Patiala"))

print()

#3. In the curly brackets we can declare the variables:
txt = "I'm college student and per day i spend {money:.2f} ruppess on food"
print(txt.format(money = 100.099))

print()

# F - STRING METHOD =>
print("F - string method")
form = "My name is {} , I'm {} years old and I'm from {}."
print(form)
print(f"by using f-string : My name is {"AYUSH"} , I'm {20} years old and I'm from {"India"}.")
#double {{variable}} is used for displaying the => {name}
print(f"by using f-string : My name is {{'Ayush'}} I'm {{20}} years old and I'm from {{'India'}}.")



print()
# String formating method =>
print("This is String Formating method")
print(form.format("Chetan" , 22 , "Panipat"))

