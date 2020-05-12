# Author: Scott Dickmeyer  NR 427 Short Project
# November 13, 2019

## Sample code to show using an FTP site, as opposed to an HTTP site to download data
# Download, unzip, and save spatial parcel data from the Larimer County GIS website.  Check to see that the geodatabase was downloaded and extracted corectly.

print("*_* Start Script *_*\n")

# Import Modules
import arcpy, os, shutil, zipfile, datetime
import urllib.request as request # Must use urllib.request because link is a ftp instead of http
from contextlib import closing

arcpy.env.overwriteOutput = True

# Download Data
# Set URL from Larimer County's GIS Website and create variables
url = r"ftp://ftp.larimer.org/GISData/GIS_ParcelOwnerGDB.zip"
path = r"C:\NR 427\Midterm Project"  # Future location will be work Geodatabase folder
myzip = os.path.join(path, "GIS_ParcelOwnerGDB.zip")

print("Retrieving Data from {0}".format(url))

# Access data and copy to myzip variable location
with closing(request.urlopen(url)) as r:
    with open(myzip, 'wb') as f:
        shutil.copyfileobj(r, f) # Copy the zipfile from the ftp server to the name/location on the target directory.

print("Data Retrieved!")

# Unzip File: Set Variables
print("\nUnzipping File...")
zip = zipfile.ZipFile(myzip, 'r')


# Unzip File: Make a new folder.
print("\nCreating new folder to unzip file into...")
expath = os.path.join(path, "Larimer Parcels")     # Joins the current path with the new folder.
if not os.path.exists(expath):
    os.mkdir(expath)      # Creates the new folder if it does not exist.
    print("New Folder Created named: " + expath)
else:
    print("Folder" + expath + " already exists.  Did not create new folder.\n")

# Unzip zip file
try:
    print("\nExtracting Zip...")
    zip.extractall(expath)  # Extract files to the expath variable location.
    print("Zipfile Extracted!")
except Exception as e:
    print(str(e))

# Verify that the zip file unzipped
print("\nVerifying Data Exists...")
gdbfile = os.path.join(expath, "GIS_ParcelOwner.gdb")
if arcpy.Exists(gdbfile):      # Checks to ensure the geodatabase exists.  This name is hard coded because it should not change.
    print("The Geodatabase uzipped correctly.")
else:
    print("An error occured, the geodatabase does not exist.")

# Create Readme
print("\nCreating readme.txt")
try:
    readme = open(os.path.join(expath, "readme.txt"), "w+") # Create text file and open it to write to.
    readme.write(myzip +" was downloaded from " + url + " on " + str(datetime.datetime.today()))  # Saved the current date/time to the readme file.
except Exception as e:
    print(str(e))

print("readme.txt has been successfully created!")

#Check Contents of the Geodatabase
print("\nChecking contents of Geodatabase...")
arcpy.env.workspace = gdbfile  # Set the workspace to the extracted geodatabase
# Iterate through the feature classes in the geodatabase to make sure they downloaded and unzipped correctly (In this case there is only suppose to be one)
fclist = arcpy.ListFeatureClasses()
print("\nThe geodatabase contains the following feature classes:")
for fc in fclist:
    dsc = arcpy.Describe(fc)
    print(dsc.name + ", which is a " + dsc.shapetype + " type and uses the Spatial Reference: " + dsc.spatialreference.name)


print("\n*_* Script Finished *_*")