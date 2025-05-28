from method_forti import *

# 使用示例
if __name__ == "__main__":
    HOST = "172.16.13.200"
    TOKEN = "GjnbcQ47Qpwtddckmkydmxt7tnG4q9"
    PORT = 50443
    addObjName = ""
    addObjIP=""
    obj_group_name = ""
    delete_name = ""

    # 创建 method_fori_api 实例
    forti_api = method_fori_api(
        host=HOST,
        token=TOKEN,
        port=PORT,
        addObjName=addObjName,
        addObjIP=addObjIP,
        obj_group_name=obj_group_name,
        delete_name=delete_name
    )

    # # 调用方法（会自动处理登录和登出）
    # #新增物件
    forti_api.addAddress(addObjName="Jeff_test_Address",addObjIP="111.111.111.111 255.255.255.255")
    #查詢物件
    # forti_api.getAddressInfo(addObjName="Jeff_test_Address")
    # #物件更新
    # forti_api.updateAddress(addObjName="Jeff_test_Address",addObjIP="222.222.222.222 255.255.255.255")
    # #取得群組位置
    # forti_api.getGroupAddress(obj_group_name="jeffzone")
    # #新增物件到群組
    # forti_api.addGroupAddress(obj_group_name="jeffzone",addObjName="Jeff_test_Address")