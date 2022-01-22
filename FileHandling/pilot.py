import traceback

#Python has built in functions for file handling

#If the file is in other directory you need to specify fully qualified path
#open function opens the file in the working directory and returns the file object and stores in variable f
#This file object 'f' will be used to perfoem file operations 
#By default the file is opened in read only mode
#To exclusively access the mode, pass second argument as: r - read, w - write, a - append  

#With open syntax is also an alternative for file handling
#it automatically closes the sile after the processing is done(no need to write finally block)

#with write mode, open function creates new file if the file is not present
#Overwrites the file content if already present.
#While in 'w' mode, it is in No readable mode, so you can't read simultaneosly
#Write operation
try:
    f = open("D:\GitProjects\Python Fundamentals\FileHandling\Friends.txt", "w")    #use '/' instead of '\'for fully qualified path
            
    f.write("Ankita is the best.")
    f.write("\nSo are Suchi and momo.")
    #print(f.read())    #This wont work for above mentioned reason
    
    
except :
    traceback.print_exc()       #To print traceback exception import traceback module

finally:
    f.close()
##################################################################################################################
#Append operation
try:
    f = open("D:\GitProjects\Python Fundamentals\FileHandling\Friends.txt", "a") 
    f.write("\nVaibhav is in the same league as they are")     #use \n for new line character
    f.write("\nAh! well, Padi sucks!!!")
    f.write("\nlike he said, \"You are never wrong!!!!\"")  #To induce "" in string use '\' before each doublequate

except:
    traceback.print_exc()

finally:
    print("Hola Amigos !!!!")
##################################################################################################################
#Read operation
with open("D:/GitProjects/Python Fundamentals/FileHandling/Friends.txt", "r") as f:     
    NewInfo = f.read(10)        #Read first 10 character only, of the file
    print(NewInfo)

    next_info = f.read(150)     #Read next 150 characters
    print(next_info)
    print("\n\n\n")
##################################################################################################################
#Change a string in File with readlines() and writelines() method
try:
    f = open("D:/GitProjects/Python Fundamentals/FileHandling/Friends.txt", "r") 
    
    linelist = f.readlines()
    
    
    #You can then iterate over this list and change accordingly
    count = 0
    for eachline in linelist:
        if eachline.__contains__("Ankita"):
            print(f"Here's She!!!! at index {count}")
            linelist[count] = linelist[count].replace("Ankita","Ankita Ma'am")
            print(linelist[count])
            break

        count+=1             

except:
    traceback.print_exc()

finally:
    f.close()

#Write the update content into the file 
try:
    f = open("D:\GitProjects\Python Fundamentals\FileHandling\Friends.txt", "w")    #use '/' instead of '\'for fully qualified path
            
    f.writelines(linelist)

except :
    traceback.print_exc()       

finally:
    f.close()
##################################################################################################################
#Change a string in File without readlines() and writelines() method
try:
    f = open("D:/GitProjects/Python Fundamentals/FileHandling/Friends.txt", "r") 
    
    newFileContent = ""
    for eachLine in f:
        stripeachLine = eachLine.strip()      #Remove spaces at the beginning and at the end of the string
        newLine = stripeachLine.replace("Suchi","Suchi Ma'am")
        newFileContent += newLine + "\n"                   

except:
    traceback.print_exc()

finally:
    f.close()

#Update the file 
try:
    f = open("D:\GitProjects\Python Fundamentals\FileHandling\Friends.txt", "w")    
            
    f.write(newFileContent)   
    
except :
    traceback.print_exc()       

finally:
    f.close() 