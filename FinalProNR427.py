'''
NR427 Final Pro
Ella Bump
'''

import requests, zipfile, os, urllib

munincipal_dataurl = r"http://maps.cityofloveland.org/Data/MunicipalBoundary.zip"
lovelandGDB_url = r"http://maps.cityofloveland.org/Data/LovelandColoradoData.gdb.zip"


mydata = requests.get(munincipal_dataurl)

save_to = r"N:\MyFiles\NR427"
myzip = os.path.join(save_to, "LovelandColoradoData.gdb.zip")

with closing(request.urlopen(lovelandGDB_url)) as r:
    with open(myzip, 'wb') as f:
        shutil.copyfileobj(r, f)

print("\nUnzipping File...")
zip = zipfile.ZipFile(myzip, 'r')

if zipfile.is_zipfile(zip):
    print("Yes, {0} is a Zip.".format(zip))
else:
    print("Sorry, not a zip!")

