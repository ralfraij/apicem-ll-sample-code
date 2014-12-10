import requests
import json
from apicem_config import * # APIC-EM IP is assigned in apicem_config.py

# remove this line if not using Python 3                                     
requests.packages.urllib3.disable_warnings()

# Prepare network device list
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

# find out network device id for network device with IP 10.10.40.253
id = ""
for item in device_list:
    if item[2] == "10.10.40.253":
        id = item[3]   
# index 2 is for IP and index 3 is for id 
# get interface detail for  network device with IP 10.10.40.253
url =  "https://"+apicem_ip+"/api/v0/interface/network-device/"+id
resp= requests.get(url,verify=False)
response_json = resp.json()
print ("Status: ",resp.status_code)
print (json.dumps(response_json["response"],indent = 4))

