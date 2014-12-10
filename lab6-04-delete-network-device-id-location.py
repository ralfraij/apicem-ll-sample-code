import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module
import sys
from operator import itemgetter
from apicem_config import *    # APIC-EM IP is assigned in apicem_config.py

requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3


# *****************************************
# IP of the network device that we want to remove the location
# You need to assigned ip here
to_delete = "10.10.40.66"
# *****************************************

if to_delete == "":
   print ("Have you assigned a application name to be deleted ?")
   sys.exit(1)
   
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
        if "locationName" in item:
            pass
        else:
            item["locationName"] = ''
        device_list.append([item["hostname"],item["type"],item["managementIpAddress"],item["id"],item["locationName"]])
    device_list.sort()                         
else:
    print ("No network device found !")
    sys.exit(1)

# Check if selected network device has been assigned a location. Proceed if yes, do nothing if no
# item[2] id the IP,item[3] is the network device id and item[4] is the locationName
for item in device_list:
    if item[2] == to_delete:
        if item[4] != '':
            id = item[3]
            print ("Location %s will be deleted from this network device" % (item[4]))
            url = "https://"+apicem_ip+"/api/v0/network-device/"+id+"/location"
            resp= requests.delete(url,verify=False)
            print ("Status:",resp.status_code)
            print (resp.text)           
        else:      
            print ("No location is assigned to this network device, nothing to delete !")
        sys.exit(1)
print ("Cannot find network device with this IP: ",to_delete)
