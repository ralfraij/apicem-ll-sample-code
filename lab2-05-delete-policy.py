import requests   # We use Python "requests" module to do HTTP GET query 
import json       # Import JSON encoder and decode module
import sys
from apicem_config import *    # APIC-EM IP is assigned in apicem_config.py
requests.packages.urllib3.disable_warnings()    # Remove this line if not using Python 3

# *****************************************
# Name of the Policy to be deleted
# You need to assigned name here
to_delete = ""
# *****************************************

if to_delete == "":
   print ("Have you assigned a policy name to be deleted ?")
   sys.exit(1)

# Preparing policy list for deleting policy 
url = "https://"+apicem_ip+"/api/v0/policy/"
resp= requests.get(url,verify=False)
response_json = resp.json()

policy_list= []

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
        # Seleting a policy ID
    id = ""
    for item in policy_list:
        if item[0] == to_delete:
           id = item[5]
    # 0 is the index of policy name, delete what we just created
    # 5 is the index of policy id '''

    # code  for deleting policy
    url = "https://"+apicem_ip+"/api/v0/policy/"+id
    resp= requests.delete(url,verify=False)
    print (resp.status_code)
    print (resp.text)
else:
    print ("No Policy Found!")
