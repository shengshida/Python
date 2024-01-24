from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
        CommunityData("SNMP_READ"),
        UdpTransportTarget(("10.255.255.254", 161)),
        ContextData(),
        ObjectType(ObjectIdentity("1.3.6.1.4.1.2011.5.25.19.1.2.1.1.2.0"))
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