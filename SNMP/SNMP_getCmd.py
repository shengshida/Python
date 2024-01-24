from pysnmp.hlapi import *

def snmp_get(ip, oid):
    #设备没有配snmp的认证 这里就不需要
    # userData = UsmUserData(  # SNMP用户信息
    #     'admin',#snmp用户名
    #     '123',#认证密码
    #     '123',#加密密码
    #     authProtocol=usmHMACSHAAuthProtocol,#配置认证算法
    #     privProtocol=usmAesCfb128Protocol)#配置加密算法
    # 实现snmpget
    g = getCmd(SnmpEngine(),  # 创建SNMP引擎
               CommunityData("SNMP_READ"),  # 团体属性
               # userData,交换机没有配认证，这里就不需要
               UdpTransportTarget((ip, 161), timeout=1, retries=0),  # 创建被管理设备信息 包含IP和端口号 超时1秒 不重试
               ContextData(),  # 创建SNMP上下文信息
               ObjectType(ObjectIdentity(oid))  # 创建MIB节点对象 #要跟参数 否则会报错
               )
    errorIndication, errorStatus, errorIndex, varBinds = next(g)  # 发送Get请求，获取sysName
    print(errorIndication)
    print(errorStatus)
    print(errorIndex)
    print(varBinds[0])
    return(str(varBinds[0]))
print(snmp_get('10.255.255.254', '1.3.6.1.2.1.1.5.0'))