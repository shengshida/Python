from pysnmp.hlapi import *
import time

def snmp_bulkget(ip, oid):
    # 实现snmpbulk
    iterator = bulkCmd(SnmpEngine(),
                   CommunityData('SNMP_READ'),
                   UdpTransportTarget((ip, 161)),
                   ContextData(),
                   0,50,
                   ObjectType(ObjectIdentity(oid)),
                   lexicographicMode=False)
    result = []
    for i in iterator:
        print(str(i[3][0]))

    return result

ip = input("输入IP:")
while True :
    oid = input("输入OID:")
    snmp_bulkget(ip, oid)
