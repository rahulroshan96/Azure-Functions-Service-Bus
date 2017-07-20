from azure.servicebus import ServiceBusService
from azure.servicebus import ServiceBusSASAuthentication
from azure.servicebus import Message
import pdb
import inspect

print inspect.getmodule(ServiceBusSASAuthentication)
key_name = 'RootManageSharedAccessKey' # SharedAccessKeyName from Azure portal
key_value = 'aeXw8zWy67Of1SDeVrGP/R67VhnPWqKmWVb1kdgS7QE=' # SharedAccessKey from Azure portal
auth = ServiceBusSASAuthentication(key_name, key_value)
pdb.set_trace()
print auth
#sbs = ServiceBusService('rahulr', shared_access_key_name=key_name, shared_access_key_value=key_value)
#sbs.create_queue('t')
#msg = Message('Hello Azure!!')
#sbs.send_queue_message('t', msg)
#msg = sbs.receive_queue_message('rahul-queue')
#print msg.body
