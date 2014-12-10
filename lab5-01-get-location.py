import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module
from apicem_config import *    # APIC-EM IP is assigned in apicem_config.py

requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3

url = "https://"+apicem_ip+"/api/v0/network-device/location"

resp= requests.get(url,verify=False)
response_json = resp.json()

print ("Status: ",resp.status_code)
print (json.dumps(response_json["response"],indent = 4))
