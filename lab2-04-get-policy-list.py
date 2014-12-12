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

    policy_list= []

    for item in response_json["response"]:
        s_user = ""
        d_user = ""
        s_app = ""
        d_app = ""
        try:       
            s_user = item["networkUser"]["userIdentifiers"][0]
        except:
            pass
        try:
            s_app = item["networkUser"]["applications"][0]["raw"]
        except:
            pass
        try:       
            d_user = item["resource"]["userIdentifiers"][0]
        except:
            pass
        try:
            s_app = item["resource"]["applications"][0]["raw"]
        except:
            pass 
        policy_list.append([item["policyName"],s_user,s_app,d_user,d_app,item["id"]])
    policy_list.sort()
    print (policy_list)

else:
    print ("No Policy Found!")


