from pysnmp.hlapi import *
import time

def snmp_bulkget(ip, oid, n=0):
    # 实现snmpbulk
    iterator = bulkCmd(SnmpEngine(),
                   CommunityData('SNMP_READ'),
                   UdpTransportTarget((ip, 161)),
                   ContextData(),
                   0,50,
                   ObjectType(ObjectIdentity(oid)),
                   lexicographicMode=False)
    result = []
    for (errorIndication, errorStatus, errorIndex, varBinds) in iterator:
        if not errorIndication and not errorStatus:
            oid_value = []
            for varBind in varBinds:
                # result = ','.join([x.prettyPrint() for x in varBind])
                oid_value = [x.prettyPrint() for x in varBind]
                result.append(oid_value)
        else:
            if n < 3:
                n += 1
                time.sleep(0.5)
                print(ip, oid, '重试snmp_bulkget')
                return snmp_bulkget(ip, oid, n)
    return result
#
print(snmp_bulkget('192.168.1.1','1.3.6.1.2.1.5.29.1'))