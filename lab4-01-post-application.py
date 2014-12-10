import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module
import sys
from apicem_config import * # APIC-EM IP is assigned in apicem_config.py
                                    
requests.packages.urllib3.disable_warnings()  # remove this line if not using Python 3 
app_name = "Unsafe_app"

r_json = {
    "category": "internet-security", 
    "appProtocol": "udp", 
    "helpString": "potential attack", 
    "udpPorts": "12345-12346", 
    "applicationGroup": "other", 
    "name": app_name
}

if app_name == "":
   print ("Have you assigned an application name to be created ?")
   sys.exit(1)
# remember to use your own app name

post_url = "https://"+apicem_ip+"/api/v0/application"
headers = {'content-type': 'application/json'}
r = requests.post(post_url, json.dumps(r_json), headers=headers,verify=False)
print ("Status: ",r.status_code)
print (r.text)
