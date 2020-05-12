#NR 427 Lesson 3 - Basics of working with zip files
#For more help, check out these references:
# https://docs.python.org/3/library/zipfile.html?highlight=zipfile#module-zipfile
# https://www.datacamp.com/community/tutorials/zip-file#PW2ZF

print("***Starting zip file basics script.......\n")
import zipfile, os, sys

myzip = r"C:\Users\MapGirl\Documents\NR426-427\NR427\RMNPDataTEST.zip"

zip = zipfile.ZipFile(myzip, 'a') #Open in r, w, or a mode for read, write, append

#Test if the input file is even a zipfile:
if zipfile.is_zipfile(myzip):
    print ("Yes, {0} is a valid zipfile, carry on with your extracting".format(myzip))
else:
    print ("Sorry, {0} is not a valid zip file, please choose another one".format(myzip))
    sys.exit()

#Report the contents of the zipfile:
print("These are the contents of that zip file, poorly formatted:")
print(zip.namelist())

print("These are the contents of that zip file, in a nice list:")
for z in zip.namelist():
    print (z)

#Use printdir to get a tabified report of the zip file's contents:
print ("\nThese are the contents of that zip file, very nicely formatted:")
print(zip.printdir())
print()

#Add a new file into the zip file:
newfile = r"C:\Users\MapGirl\Documents\NR426-427\NR427\CSUlocations.csv"
#zip.write(newfile)
#However, it adds it with a bunch of subfolders, let's figure that out

#Read files in the zip file without extracting:
print ("Reading the contents of just one file...")
print (zip.read("RMNPData/RMNP_Lakes.prj")) #This could be a txt or csv, then used directly in other operations

#Extract all the files from the zip file. Will go into the current working directory
# So let's set the cwd first:
print ("Creating a new folder for the extracted files and setting CWD to it...")
newcwd =r"C:\Users\MapGirl\Documents\NR426-427\NR427\Lesson3Scratch"

#If that folder doesn't already exist, create it here:
if not os.path.exists(newcwd):
    os.mkdir(newcwd)
    print ("Created the new folder")

#Change the current working directory to that new folder:
os.chdir(newcwd)

#Finally, extract all the files from the zip file:
print ("Extracting the files from {0} to {1}".format(myzip,newcwd))
try:
    zip.extractall()
except:
    print("Couldn't extract it")


#Be sure to close the zip file at the end:
zip.close()

print ("Zip file basics script completed...")
