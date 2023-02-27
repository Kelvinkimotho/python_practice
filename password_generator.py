import random

def generator():
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    numbers="1234567890"
    symbols="@$%&"
    password_combination=uppercase+lowercase+numbers+symbols
    # let's prompt the user to input his prefered password length
    #password length must range 6<=passlength<=10
    password_length=int(input("Enter your prefered password length \n"))
    if password_length<6:
        print("password too short..\n")
    else:
        password="".join(random.sample(password_combination,password_length))

        return password
print(f"Your password is: {generator()}")