import os
import shutil


#os.system("date")
#os.mkdir("test")
#os.getcwd(


path = "C:/Users/LENOVO/Documents/whiteHat.jr/Python/C-99 Backup Files/python.py"
#isExist = os.path.exists(path)
#print(isExist)


#route = os.path.splitext(path)
#print(route[0])
#print(route[1])


#os.listdir(path)


source = input("Enter The Source Folder Name")
destination = input("Enter Your Folder Destination Name")
source = source + "/"
destination = destination + "/"
listoffiles = os.listdir(source)
for file in listoffiles:
    shutil.move((source + file),destination)