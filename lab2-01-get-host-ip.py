import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module
from apicem_config import * # APIC-EM IP is assigned in apicem_config.py
                                 
requests.packages.urllib3.disable_warnings()  # Remove this line if not using Python 3    

get_host_url = "https://"+apicem_ip+"/api/v0/host/"
ip_list = []
api_response = requests.get(get_host_url, verify=False)
response_json = api_response.json()
for item in response_json["response"]:
    ip_list.append(item["hostIp"])
ip_list.sort()  
# print (ip_list)
