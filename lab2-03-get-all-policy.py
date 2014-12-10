import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module
from apicem_config import *    # APIC-EM IP is assigned in apicem_config.py

requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3

url = "https://"+apicem_ip+"/api/v0/policy/count"   # API base url
resp= requests.get(url,verify=False)     # The response (result) from "GET /policy/count" query
response_json = resp.json() # Get the json-encoded content from response 
count = response_json["response"]    #  Total count of policy

if count > 0:
    url = "https://"+apicem_ip+"/api/v0/policy/1/"+str(count)  # API base url, convert 'count' to string
    resp= requests.get(url,verify=False) # The response (result) from "GET /policy/{startIndex}/{recordsToReturn}" query
    response_json = resp.json() # Get the json-encoded content from response
    print ("Status: ",resp.status_code) # This is the http request status
    print ("Response:\r",json.dumps(response_json,indent=4))    # This is the entire response from the query 
else:
    print ("No Policy Found!")
    
    
    
