# this program takes first  name and last name  from a user and saves them as full name to a text file
#Then after saving the name in the text file , he/she can confirm whether the name is saved succesfull by reading from the names.txt file

def menu():
    print("**********activities available***********\n1:Add your name to the txt file.\n2:Read from the names file.\n*****************************")
menu()

 

# bellow function writes to the names.txt file 
#actually the function appends to the names.txt file

def add_name():
      first_name=input(" Enter your first name...\n")
      laast_name=input("Enter your last name...\n")

      if len(first_name)<=0 or len(laast_name)<=0:
             print("first name or last name can't be null ...\n")
      else:
             full_name=f"{first_name} {laast_name}"
             #lets now open the names.txt file and save names in items
    
             with open("names.txt",'a') as names:
                 names.write(f"{full_name}")
                 names.close()
                 print("name recorded succesfully!!!")
# bellow function reads from the names.txt file
                 
def read():
        print("Here is a list of names in the file ......\n")
        
        with open("names.txt",'r') as names_file:
            names=names_file.readlines()
            #to print all the names we have to loop through the list of names
            
            for name in names:
               print(name)
               
               
#Bellow function takes users choice on what he/she want to do to the file              
def user_choice():
    choice=int(input("Enter your choice please..\n"))
    if choice==1:
          add_name()
    elif choice==2:
         read()
    else: print("Invalid choice....")   
    
    
#calling the user_choice funcction

user_choice()