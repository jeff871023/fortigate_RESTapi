"""FortiGateAPI examples.

- Initialize FortiGateAPI with optional parameters scheme=`https`, port=443
- Create address in the Fortigate
- Get address by name (unique identifier)
- Update address data in the Fortigate
- Delete address from the Fortigate
- Check for absence of address in the Fortigate
- Initialize FortiGateAPI with token instead of username and password
- FortiGateAPI `with` statement
"""

import logging
import json
from fortigate_api import FortiGateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "172.16.13.200"
USERNAME = "jeff"
PASSWORD = "1qaz5tgb*()"
TOKEN = "GjnbcQ47Qpwtddckmkydmxt7tnG4q9"
PORT=50443

#要新增的物件
addObjName= "Jeff_test_Address"
#要加入的群組名稱
obj_group_name="jeffzone"
#要在群組刪除的物件
delete_name="Vlan19 address"

# Initialize FortiGateAPI with optional parameters scheme=`https`, port=443
api = FortiGateAPI(
    host=HOST,
    # username=USERNAME,
    # password=PASSWORD,
    token=TOKEN,
    # scheme="https",
    port=PORT,
    # logging_error=True,
)
api.login()  # login is optional


# ########Create address in the Fortigate
# data = {
#     #"name": "Jeff_test_Address",
#     "name": addObjName,
#     "obj-type": "ip",
#     "subnet": "111.111.111.111 255.255.255.255",
#     "type": "ipmask",
# }
# response = api.cmdb.firewall.address.create(data)
# print(f"address.create {response}")  # address.create <Response [200]>


# ########查詢物件
# items = api.cmdb.firewall.address.get(name="Jeff_test_Address")
# print(f"資訊:{items[0]}")
# print(f"addresses count={len(items)}")  # addresses count=1

# ########Update address data in the Fortigate
# data = {"name": "Jeff_test_Address", "subnet": "222.222.222.222 255.255.255.255"}
# response = api.cmdb.firewall.address.update(data)
# print(f"address.update {response}")  # address.update <Response [200]>


# ########查詢group所有物件名字
# items = api.cmdb.firewall.addrgrp.get(name=obj_group_name)
# objdate = []
# for item in items:
#     if "member" in item:
#         objdate.extend([member["name"] for member in item["member"]])
# print(f"群組所有物件:{objdate}")
# #print(f"資訊:{items[0]}")


# ########新增物件到group
# items = api.cmdb.firewall.addrgrp.get(name=obj_group_name)
# # 新增 member 到列表中
# new_member = {"name": addObjName}
# for item in items:
#     if "member" in item:  # 確保有 member 鍵
#         item["member"].append(new_member)
# data = {
#     "name": obj_group_name,
#     'member': item["member"]
# }
# response = api.cmdb.firewall.addrgrp.update(data)
# print(f"已新增並更新群組 {response}")  # address.update <Response [200]>


# ########刪除group的其中一個物件
# items = api.cmdb.firewall.addrgrp.get(name=obj_group_name)
# for item in items:
#     if "member" in item:  # 確保有 member 鍵
#         item["member"] = [m for m in item["member"] if m["name"] != delete_name]
# data = {
#     "name": obj_group_name,
#     'member': item["member"]
# } 
# response = api.cmdb.firewall.addrgrp.update(data)
# print(f"已刪除物件並更新群組 {response}")  # address.update <Response [200]>





# ########Delete address from the Fortigate
# response = api.cmdb.firewall.address.delete("Jeff_test_Address")
# print(f"address.delete {response}")  # address.delete <Response [200]>

# ########Check for absence of address in the Fortigate
# response = api.cmdb.firewall.address.is_exist("Jeff_test_Address")
# print(f"address.is_exist {response}")  # address.is_exist False

api.logout()

# ########Initialize FortiGateAPI with token instead of username and password
# api = FortiGateAPI(host=HOST, token=TOKEN)
# items = api.cmdb.firewall.address.get(name="APIaddAddress")
# print(f"addresses count={len(items)}")  # addresses count=1

# ########FortiGateAPI `with` statement
# with FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD) as api:
#     response = api.cmdb.firewall.address.is_exist("APIaddAddress")
#     print("address.is_exist", response)  # exist <Response [404]>
