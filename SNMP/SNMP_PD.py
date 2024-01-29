from pysnmp.hlapi import *
import time
import pandas
import re

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
    for i in iterator :
        result.append(str(i[3][0]))
        #print(str(i[3][0]))

    return result

ip = "192.168.1.1"

oid = "1.3.6.1.4.1.2011.5.25.41.1.2.3.1"
oid_data = snmp_bulkget(ip, oid)
snmp_pd = pandas.DataFrame()

for i in oid_data :
    match_object = re.match( r'^SNMP.+?(\d+).(\d+.\d+.\d+.\d+.\d+) = (.+)', i, re.I )
    if match_object != None :
        snmp_pd.at[ match_object[2], match_object[1]] = match_object[3]

print(snmp_pd)

