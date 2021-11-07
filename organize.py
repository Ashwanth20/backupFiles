import os
import shutil

path = input("Enter The Path")
listoffiles = os.listdir(path)
for file in listoffiles:
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == "":
        continue
    if os.path.exists(path + "/" + ext):
        shutil.move(path + "/" + file, path + "/" + ext + "/" + file)
    else:
        shutil.move(path + "/" + file, path + "/" + ext + "/" + file)
        os.mkdir(path + "/" + ext)
