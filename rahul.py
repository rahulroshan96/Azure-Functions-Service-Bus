from azure.common.credentials import ServicePrincipalCredentials
from azure.common.credentials import UserPassCredentials
from azure.mgmt.monitor import MonitorManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from msrestazure.azure_exceptions import CloudError
import jsonpickle
import pdb
import pprint
import json


CLIENT_ID = 'bb2fe6f4-7cc5-4286-a759-4de185ef4649'
SECRET = '77D5CFtS3dQeBjLqHy8RSQrpNbHx4g1++v0OkIyCypQ='
TENANT = '1e210ad2-3b9a-4348-96b1-4be6f959b2a4'
subscription_id = '0eebbbed-14c0-462e-99e0-dfec1d42e0c9'
SUBNET_ID = '/subscriptions/0eebbbed-14c0-462e-99e0-dfec1d42e0c9/resourceGroups/AviUsers/providers/Microsoft.Network/virtualNetworks/AnuragAviNetCentral/subnets/subnet-2'


class LB_mgmt():
    """ Scale Set Details
    creating resource activity alerts
    get resource activity alerts
    """

    def __init__(self):
        self.credentials = ServicePrincipalCredentials(
            client_id=CLIENT_ID,
            secret=SECRET,
            tenant=TENANT,
        )


        self.cr = UserPassCredentials('rahulr@avinetworks.com', 'Roshan@123')
        self.monitor_client = MonitorManagementClient(self.cr, subscription_id)
        self.compute_client = ComputeManagementClient(self.cr, subscription_id)
        self.network_client = NetworkManagementClient(self.cr, subscription_id)
        self.resource_client = ResourceManagementClient(self.cr, subscription_id)


    def test_it(self):
        for alert in self.monitor_client.activity_log_alerts.list_by_subscription_id():
            print alert


obj = LB_mgmt()
obj.test_it()
