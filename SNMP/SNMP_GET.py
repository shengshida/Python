from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
        CommunityData("SNMP_READ"),
        UdpTransportTarget(("192.168.1.1", 161)),
        ContextData(),
        ObjectType(ObjectIdentity("1.3.6.1.4.1.2011.5.25.42.3.1.1.1.1.2"))
    )
)

print(errorIndication)
print(errorStatus)
print(errorIndex)
print(varBinds)
for i in varBinds :
    print(i)