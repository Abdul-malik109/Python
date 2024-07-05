import os, shutil
path = "C:/Users/abdma/Documents/py tut/"
filename = os.listdir(path)
foldername=['csv files', 'image files', 'text files']
for loop in range(0,3):
    if not os.path.exists(path + foldername[loop]):
        print(path + foldername[loop])
        os.makedirs(path + foldername[loop])
for file in filename:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
