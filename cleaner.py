# this file fetchs for file in a storage area and deletes them

#i have a directory with files
# this python script will filter for text files and delete them

import os

#path to the files location
path='C:/Users/kelvin/Desktop/tecno'
files=[file for file in os.listdir(path)]

#this function fetches all files in that location and displays them 

def display():
    print("This are the files available before delete operation!.\n")
    for file in files:
        return file
        
print(display())


#After seeing files in the directory , filter for txt files and delete the

def delete():
    for file in files:
        if ".txt" in file:
            os.system(f"del {file}")
            print(f"{file} deleted succesfully!")
        else:
             pass
             
delete()

#Let's confirm whether the files were deleted

def after_delete():
    print("This are the files left:\n")
    for file in files:
        return file
        
print(after_delete())