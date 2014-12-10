import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module
from operator import itemgetter
from apicem_config import * # APIC-EM IP is assigned in apicem_config.py
  
requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3

device_list = []

# create device id list
url = "https://"+apicem_ip+"/api/v0/network-device/count"   # API base url
resp= requests.get(url,verify=False)     # The response (result) from "GET /network-device/count" query
response_json = resp.json() # Get the json-encoded content from response with "response_json = resp.json()
count = response_json["response"]    # Total count of network-device and convert it to string

if count > 0 :
    device_list = []
    url = "https://"+apicem_ip+"/api/v0/network-device/1/"+str(count)  # API base url, convert 'count' to string
    resp= requests.get(url,verify=False) # The response (result) from "GET /network-device/{startIndex}/{recordsToReturn}" query
    response_json = resp.json() # Get the json-encoded content from response
    for item in response_json["response"]:
        device_list.append([item["hostname"],item["type"],item["managementIpAddress"],item["id"]])
    device_list.sort()
else:
    print ("No network device found !")

# Assuming the first network device in list is used
# First find out if this network device has been assigned a location
print ("Assuming the first network device in list is used:",device_list[3][3])
url = "https://"+apicem_ip+"/api/v0/network-device/"+device_list[3][3]+"/location"
r= requests.get(url,verify=False)
response_json = r.json()

# Find out location detail if this network device has been assigned a location
if r.status_code == 200:
    l_id = response_json["response"]["location"]
    print ("This is the location id of this network device:",l_id)
    print( "Now we query the detail of this location by this id")
    url = "https://"+apicem_ip+"/api/v0/location/"+l_id
    r2= requests.get(url,verify=False)
    r2_json = r2.json()      
    print ("Location by id query status: ",r2.status_code)
    print (json.dumps(r2_json["response"],indent = 4))
else :
    print ("Network-device-id-location query status:",r.status_code)
    print (response_json)
    print ("No location has been assigned to this network device")


    
