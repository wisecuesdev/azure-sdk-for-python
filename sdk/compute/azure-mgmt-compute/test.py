from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from dotenv import load_dotenv
import os
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import DecodeError

load_dotenv()

client = ComputeManagementClient(credential=DefaultAzureCredential(), subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID"))
pager = client.usage.list(location="westus")
pager = client.operations.list()

# client = ResourceManagementClient(credential=DefaultAzureCredential(), subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID"))
# pager = client.resource_groups.list()

client = StorageManagementClient(credential=DefaultAzureCredential(), subscription_id=os.getenv("AZURE_SUBSCRIPTION_ID"))
pager = client.operations.list()


try:
    result = list(pager)

    for item in result:
        print(item.serialize())
except DecodeError as e:
    with open("safe_private_file.txt", "a+") as file:
        # file.write(f"error header: {e.response.headers}\n")
        file.write(f"error content: {e.response.body()}\n")
        # print(e.response.body())