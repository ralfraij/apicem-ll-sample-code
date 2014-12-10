import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module
from operator import itemgetter
from apicem_config import *    # APIC-EM IP is assigned in apicem_config.py

requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3

l_list = []

url = "https://"+apicem_ip+"/api/v0/location"
resp= requests.get(url,verify=False)
response_json = resp.json()

for item in response_json["response"]:
    l_list.append({"location_id":item["id"],"location_name":item["locationName"]})
# Sorting the list of dictionary
location_list = sorted(l_list, key=itemgetter('location_name'))
                
# Assuming the first id in list is used

print ("Query location: ",location_list[4]["location_name"])
try:
    url = "https://"+apicem_ip+"/api/v0/location/"+location_list[4]["location_id"]+"/network-device/"
    r= requests.get(url,verify=False)
    response_json = r.json()
    print ("Status: ",r.status_code)
    print (json.dumps(response_json["response"],indent = 4))
except:
    print ("Something is fishy !")
