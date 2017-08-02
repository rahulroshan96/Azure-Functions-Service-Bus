"""
    Azure Functions HTTP Example Code for Python

    Created by Anthony Eden
    http://MediaRealm.com.au/
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib')))

import json
from AzureHTTPHelper import HTTPHelper
from azure.servicebus import 
# This is a little class used to abstract away some basic HTTP functionality
http = HTTPHelper()
from azure.servicebus import ServiceBusService
from azure.servicebus import Message
# All these print statements get sent to the Azure Functions live log
print "--- GET ---"
print http.get
print

print "--- POST ---"
print http.post
print

key_name = 'RootManageSharedAccessKey' # SharedAccessKeyName from Azure portal
key_value = '4My+blZDLkuXYCnqWNlx35V5wA+9XiBZvxwccRNG7bg=' # SharedAccessKey from Azure portal
sbs = ServiceBusService('mynamespace0', shared_access_key_name=key_name, shared_access_key_value=key_value)
msg = Message(http.post)
sbs.send_queue_message('t', msg)
print "##########Message sent##############"

print "--- HEADERS ---"
print http.headers
print

print "--- OTHER ENVIRONMENTAL VARIABLES ---"
for x in http.env:
    print x
print


# All data to be returned to the client gets put into this dict
returnData = {
    # HTTP Status Code:
    "status": 200,

    # Response Body:
    "body": "<h1>Azure Works :)</h1>",

    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "text/html",
        "X-Awesome-Header": "YesItIs"
    }
}

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))
