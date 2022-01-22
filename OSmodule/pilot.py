import os

print(os.getcwd())
print(os.listdir())
print(os.listdir("01_Variables"))
#os.mkdir("new directory")   #creates new dir in ced
#print(os.listdir("new directory"))
#os.rmdir("new directory/test")         #Make sure the directory is empty before removing directory
#os.rename("new directory","testFolder")
os.rename("OSmodule/pilot.py","OSmodule/basicFunctios.py")