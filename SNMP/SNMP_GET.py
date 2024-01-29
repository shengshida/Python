from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
        CommunityData("SNMP_READ"),
        UdpTransportTarget(("192.168.1.1", 161)),
        ContextData(),
        ObjectType(ObjectIdentity("1.3.6.1.2.1.31.1.5.0"))
    )
)

print(errorIndication)
print(errorStatus)
print(errorIndex)
print(varBinds)
#for i in varBinds :
#    print(i)
#    print(type(i))
print(str(varBinds[0]))