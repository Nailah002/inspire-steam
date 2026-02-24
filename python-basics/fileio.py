#Name: Nailah Wanjiku
#Date: 24/2/2026
#Program to perform file operations

#create new file
new_file = open("student_data.txt", "r+")

#write to new file
new_file.write("{student name: Nailah Marie, ID: 204567347, email: marienailah218@gmail.com}")

#read from the file
new_file = open("student_data.txt", "r+")
data = new_file.read()
print(data)
new_file.close()

#Delete file
#use os module
import os
os.remove("remove.txt")

#Delete folder
os.rmdir("folder")