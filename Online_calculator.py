


def car(**car_name):
    
 print(type(car_name))
print("this is " , car_name["car1"] , car_name["car2"])

car_name(car1 = "BMW" , CAR2 = "MERCEDIES")







print("Welcome ! Online Calculator")





i =0
user_time = 1
while i<= user_time:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication ")
    print("4. Division")
    print("5. Modulus")

    a = int(input("enter choice:"))
    if(a == 1):
        print("Addition")
        print("Sum is: ", num1 + num2)
        print("do you want to continue? yes(1) or no(0)")
        continue_choice = int(input())
        if continue_choice == 0:
            print("Thank you for using the calculator!")
            break
        else:
            i -= 1

    elif(a == 2):
        print("Substraction")
        print("Difference is: ", num1 - num2)
        print("do you want to continue? yes(1) or no(0)")
        continue_choice = int(input())
        if continue_choice == 0:
            print("Thank you for using the calculator!")
            break
        else:
            i -= 1
    elif(a == 3):
        print("Multiplication")
        print("Product is: ", num1 * num2)  
        print("do you want to continue? yes(1) or no(0)")
        continue_choice = int(input())
        if continue_choice == 0:
            print("Thank you for using the calculator!")
            break
        else:
            i -= 1
    elif(a == 4):
        print("Division")
        if num2 != 0:
            print("Quotient is: ", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
            print("do you want to continue? yes(1) or no(0)")
        continue_choice = int(input())
        if continue_choice == 0:
            print("Thank you for using the calculator!")
            break
        else:
            i -= 1
    elif(a == 5):
        print("Modulus")
        if num2 != 0:
            print("Remainder is: ", num1 % num2)
        else:
            print("Error: Division by zero is not allowed.")
            print("do you want to continue? yes(1) or no(0)")
        continue_choice = int(input())
        if continue_choice == 0:
            print("Thank you for using the calculator!")
            break
        else:
            i -= 1

            

