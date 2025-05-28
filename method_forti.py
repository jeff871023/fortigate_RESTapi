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
from fortigate_api import FortiGateAPI


class method_fori_api:
    def __init__(self, host, token, port, addObjName=None,addObjIP=None, obj_group_name=None, delete_name=None):
        """
        初始化 FortiAPI 方法类
        
        参数:
            host (str): FortiGate 主机地址
            token (str): 访问令牌
            port (int): 端口号
            addObjName (str, optional): 要新增的物件名称
            obj_group_name (str, optional): 要加入的群組名稱
            delete_name (str, optional): 要在群組刪除的物件名稱
        """
        self.host = host
        self.token = token
        self.port = port
        self.addObjName = addObjName
        self.addObkIP=addObjIP
        self.obj_group_name = obj_group_name
        self.delete_name = delete_name
        
        # 初始化 FortiGateAPI
        self.api = FortiGateAPI(
            host=self.host,
            token=self.token,
            port=self.port,
        )

    def login_required(func):
        """裝飾器：確保方法執行前登入，執行後登出"""
        def wrapper(self, *args, **kwargs):
            try:
                # 執行前登入
                logging.debug("正在登入 FortiGate...")
                self.api.login()
                
                # 執行被裝飾的方法
                result = func(self, *args, **kwargs)
                
                return result
            except Exception as e:
                logging.error(f"執行方法 {func.__name__} 時發生錯誤: {e}")
                raise
            finally:
                # 確保無論如何都執行登出
                logging.debug("正在登出 FortiGate...")
                self.api.logout()
        return wrapper
    
    ######新增物件######
    @login_required
    def addAddress(self,addObjName,addObjIP):
        data = {
            "name": addObjName,
            "obj-type": "ip",
            "subnet": addObjIP,
            "type": "ipmask",
        }
        response = self.api.cmdb.firewall.address.create(data)  
        print(f"物件新增回報 {response}")  # address.create <Response [200]>

    ######取得物件資訊######
    @login_required
    def getAddressInfo(self,addObjName):
        items = self.api.cmdb.firewall.address.get(name=addObjName)
        print(f"資訊:{items}")
        #print(f"addresses count={len(items)}")  # addresses count=1

    ######更新物件######
    @login_required
    def updateAddress(self,addObjName,addObjIP):
        data = {"name": addObjName, "subnet": addObjIP}
        response = self.api.cmdb.firewall.address.update(data)
        print(f"物件更新回報: {response}")  # address.update <Response [200]>


    ######取得群組物件資訊######
    @login_required
    def getGroupAddress(self,obj_group_name):
        items = self.api.cmdb.firewall.addrgrp.get(name=obj_group_name)
        objdate = []
        for item in items:
            if "member" in item:
                objdate.extend([member["name"] for member in item["member"]])
        print(f"群組所有物件:{objdate}")
        #print(f"資訊:{items[0]}")   


    ######新增物件到群組######
    @login_required
    def addGroupAddress(self,obj_group_name,addObjName):
        items = self.api.cmdb.firewall.addrgrp.get(name=obj_group_name)
        # 新增 member 到列表中
        new_member = {"name": addObjName}
        for item in items:
            if "member" in item:  # 確保有 member 鍵
                item["member"].append(new_member)
        data = {
            "name": obj_group_name,
            'member': item["member"]
        }
        response = self.api.cmdb.firewall.addrgrp.update(data)
        print(f"已新增並更新群組 {response}")  # address.update <Response [200]>    

    ######刪除群族其中一個物件######
    @login_required
    def deleGroupAddress(self,obj_group_name,delete_name):
        items = self.api.cmdb.firewall.addrgrp.get(name=obj_group_name)
        for item in items:
            if "member" in item:  # 確保有 member 鍵
                item["member"] = [m for m in item["member"] if m["name"] != delete_name]
        data = {
            "name": obj_group_name,
            'member': item["member"]
        } 
        response = self.api.cmdb.firewall.addrgrp.update(data)
        print(f"已刪除物件並更新群組 {response}")  # address.update <Response [200]>

