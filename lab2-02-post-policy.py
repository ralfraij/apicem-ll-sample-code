import json
import requests
import random
import string
from apicem_config import * # APIC-EM IP is assigned in apicem_config.py                                   
requests.packages.urllib3.disable_warnings() # Remove this line if not using Python 3  

# To get a list of host IP address

get_host_url = "https://"+apicem_ip+"/api/v0/host/"
ip_list = []
api_response = requests.get(get_host_url, verify=False)
response_json = api_response.json()
for item in response_json["response"]:
    ip_list.append(item["hostIp"])
ip_list.sort()

# Host IP is getting from ip_list
# Rest of input(policy name, application ...etc) is hard coded to simplify the example

# Post policy code starting here, "host" is the host IP user picked
host = ""
json_obj = {
  "policyOwner": "Admin",
  "networkUser": {"userIdentifiers":[host],"applications":[{"raw":"12345;UDP"}]},
  "actions": [ "DENY"],
  "policyName": ""
 }

# For example, user picked the third IP(index 2) on the list and make sure it's not NULL '''
if ip_list[2] != "":
    json_obj["networkUser"]["userIdentifiers"][0] = ip_list[2]

# Since this is a learning lab, to prevent a conflict policy we generate a random name here
# You can use your own unique policy name by assigning the name to json_obj[policyName"]
# Please check the output and write down the policy name we will use it for deleting policy

json_obj["policyName"] = 'NoAccess_'+''.join(random.choice(string.ascii_uppercase + string.digits) for n in range(4))

print ("******* This is the policy name that will be used to create policy ********")
print (json_obj["policyName"])
print ("***************************************************************************")

# For POST we need to provide content type which is JSON that APIC-EM is using
headers = {'content-type': 'application/json'}
post_policy_url = "https://"+apicem_ip+"/api/v0/policy/"
r = requests.post(post_policy_url, json.dumps(json_obj), headers=headers,verify=False)
print ("status: ",r.status_code)
print (r.text)
