import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module
from apicem_config import * # APIC-EM IP is assigned in apicem_config.py
 
requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3       

url = "https://"+apicem_ip+"/api/v0/host"   # API base url
resp= requests.get(url,verify=False)    # The response (result) from "GET /host" query
response_json = resp.json() # Get the json-encoded content from response
print ("Status: ",resp.status_code)  # This is the http request status
print (json.dumps(response_json,indent=4)) # Convert "response_json" object to a JSON formatted string and print it out    
