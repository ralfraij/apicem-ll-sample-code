import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module
import sys
from apicem_config import *    # APIC-EM IP is assigned in apicem_config.py
requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3


# *****************************************
# Name of the application to be deleted
# You need to assigned name here
to_delete = ""
# *****************************************

if to_delete == "":
   print ("Have you assigned a application name to be deleted ?")
   sys.exit(1)

url = "https://"+apicem_ip+"/api/v0/application/app-name/"+to_delete

resp= requests.get(url,verify=False)
response_json = resp.json()
app_id = response_json["response"]["id"]
if app_id != "":
    del_url = "https://"+apicem_ip+"/api/v0/application/"+app_id
    r = requests.delete(del_url,verify=False)
    print ("Status: ",r.status_code)
    print (r.text)
