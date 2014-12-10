import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module
from apicem_config import *    # APIC-EM IP is assigned in apicem_config.py

requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3

r_json = {
    "description": "Demo Create Loaction",
    "locationName": "Building123",
    "civicAddress": "123 Lucky Drive MILPITAS, CALIFORNIA 95035",
    "geographicalAddress": "Latitude: 37.422039, Longitude: -121.81659 degrees"
} 

post_url = "https://"+apicem_ip+"/api/v0/location"
headers = {'content-type': 'application/json'}
r = requests.post(post_url, json.dumps(r_json), headers=headers,verify=False)
print ("Status: ",r.status_code)
print (r.text)
