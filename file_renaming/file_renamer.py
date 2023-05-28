import os
files=[file for file in os.listdir('C:/Users/kelvin/Desktop/file_renaming')]
for file in files:
     if ".txt" in file:
         new_file_name=file.replace("txt","jpg")
         print(file)
         os.system(f"ren {file} {new_file_name}")
print("Hoping everything worked well!!")