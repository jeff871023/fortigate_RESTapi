"""Quickstart FortiGate.

- Creates address in the Fortigate
- Get address by name (unique identifier)
- Updates address data in the Fortigate
- Delete address from the Fortigate
"""

from pprint import pprint

from fortigate_api import FortiGate

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = FortiGate(host=HOST, username=USERNAME, password=PASSWORD)

# Creates address in the Fortigate
data = {
    "name": "ADDRESS",
    "obj-type": "ip",
    "subnet": "127.0.0.100 255.255.255.252",
    "type": "ipmask",
}
response = fgt.post(url="api/v2/cmdb/firewall/address/", data=data)
print(f"POST {response}", )  # POST <Response [200]>

# Get address by name (unique identifier)
response = fgt.get(url="api/v2/cmdb/firewall/address/ADDRESS")
print(f"GET {response}", )  # POST <Response [200]>
result = response.json()["results"]
pprint(result)
#  [{"name": "ADDRESS",
#    "subnet": "127.0.0.100 255.255.255.252",
#    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
#    ...
#    }]

# Updates address data in the Fortigate
data = {"name": "ADDRESS", "subnet": "127.0.0.255 255.255.255.255"}
response = fgt.put(url="api/v2/cmdb/firewall/address/ADDRESS", data=data)
print(f"PUT {response}")  # PUT <Response [200]>

# Delete address from the Fortigate
response = fgt.delete(url="api/v2/cmdb/firewall/address/ADDRESS")
print(f"DELETE {response}", )  # DELETE <Response [200]>

fgt.logout()
