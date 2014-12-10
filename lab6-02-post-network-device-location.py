import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module
import sys
from operator import itemgetter
from apicem_config import *    # APIC-EM IP is assigned in apicem_config.py

requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3

device_list = []
l_list = []

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
    device_list.sort
else:
    print ("No network device found !")
    sys.exit(1)

url = "https://"+apicem_ip+"/api/v0/location/count"   # API base url
resp= requests.get(url,verify=False)     # The response (result) from "GET /network-device/count" query
response_json = resp.json() # Get the json-encoded content from response with "response_json = resp.json()
lcount = response_json["response"]    # Total count of network-device and convert it to string

if lcount > 0:
    url = "https://"+apicem_ip+"/api/v0/location"
    resp= requests.get(url,verify=False)
    response_json = resp.json()
    for item in response_json["response"]:
        l_list.append({"location_id":item["id"],"location_name":item["locationName"]})
    # Sorting the list of dictionary
    location_list = sorted(l_list, key=itemgetter('location_name'))

    # Selected a network device and location in the list '''
    print ("Selected network device id is: ", device_list[3][3])
    print ("Selected location name : %s and location id : %s" % (location_list[0]["location_name"],location_list[0]["location_id"]))

    r_json = {
        "id": device_list[3][3], 
        "location": location_list[0]["location_id"]
    }

    post_url = "https://"+apicem_ip+"/api/v0/network-device/location"
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, json.dumps(r_json), headers=headers,verify=False)
    print ("Status: ",r.status_code)
    print (r.text)
else:
    print ("No location is created!")
