import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module
from apicem_config import * # APIC-EM IP is assigned in apicem_config.py
                                    
requests.packages.urllib3.disable_warnings()  # remove this line if not using Python 3 

app_name = "Unsafe_app"
if app_name != "":
    url = "https://"+apicem_ip+"/api/v0/application/app-name/"+app_name
    resp= requests.get(url,verify=False)
    response_json = resp.json()
    print ("Status: ",resp.status_code)
    print (json.dumps(response_json["response"],indent = 4))
else:
    print ("Application name is empty")
