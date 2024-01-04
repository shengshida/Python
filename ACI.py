import cobra.mit.access 
import cobra.mit.session 
import cobra.mit.request 
import cobra.model.fv 
import cobra.model.pol

# APIC 登录(测试时，请删除注释。下同) 
ls = cobra.mit.session.LoginSession('apic的ip地址', '用户名', '口令') 
md = cobra.mit.access.MoDirectory(ls) 
md.login()

# 该代码将要操作的顶级MO，注意红色粗体代码(引用关系和动作效果) 
topMo = cobra.model.pol.Uni('')

# 使用ACI Cobra模块格式语言，创建Tenant、APP、EPG、BD、绑定EPG到特定交换机端口 
fvTenant = cobra.model.fv.Tenant(topMo, ownerKey=u'', name=u'chungewa-tenant', descr=u'', ownerTag=u'')

fvBD2 = cobra.model.fv.BD(fvTenant, ownerKey=u'', name=u'BD2', descr=u'', unkMacUcastAct=u'proxy', arpFlood=u'no', unicastRoute=u'yes', ownerTag=u'', unkMcastAct=u'flood') 
fvAp2 = cobra.model.fv.Ap(fvTenant, ownerKey=u'', prio=u'unspecified', name=u'app2', descr=u'', ownerTag=u'') 
fvAEPg2 = cobra.model.fv.AEPg(fvAp2, prio=u'unspecified', matchT=u'AtleastOne', name=u'EPG2', descr=u'') 
fvRsPathAtt2 = cobra.model.fv.RsPathAtt(fvAEPg2, instrImedcy=u'lazy', mode=u'regular', encap=u'vlan-2', tDn=u'topology/pod-1/paths-103/pathep-[eth1/42]') 
fvRsBd2 = cobra.model.fv.RsBd(fvAEPg2, tnFvBDName=u'BD2')

# 以下是一个循环，创建同一个Tenant的另一组APP/EPG/BD，如果创建的数量较多，可以用循环语句代替。此处为了便于大家看代码、看Mo之间的逻辑引用关系 
fvBD3 = cobra.model.fv.BD(fvTenant, ownerKey=u'', name=u'BD3', descr=u'', unkMacUcastAct=u'proxy', arpFlood=u'no', unicastRoute=u'yes', ownerTag=u'', unkMcastAct=u'flood') 
fvAp3 = cobra.model.fv.Ap(fvTenant, ownerKey=u'', prio=u'unspecified', name=u'app3', descr=u'', ownerTag=u'') 
fvAEPg3 = cobra.model.fv.AEPg(fvAp3, prio=u'unspecified', matchT=u'AtleastOne', name=u'EPG3', descr=u'') 
fvRsPathAtt3 = cobra.model.fv.RsPathAtt(fvAEPg3, instrImedcy=u'lazy', mode=u'regular', encap=u'vlan-3', tDn=u'topology/pod-1/paths-103/pathep-[eth1/42]') 
fvRsBd3 = cobra.model.fv.RsBd(fvAEPg3, tnFvBDName=u'BD3')

# 向APIC commmit这些配置 
c = cobra.mit.request.ConfigRequest() 
c.addMo(fvTenant) 
md.commit(c)