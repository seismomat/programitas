# import the requests library
import requests
from zipfile import ZipFile

url = 'http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip'
 
# download the file contents in binary format
r = requests.get(url)
 
with open("myzip.zip", "wb") as zip:
    zip.write(r.content)


with ZipFile('myzip.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
