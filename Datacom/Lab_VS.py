from datetime import datetime,timedelta
from time import sleep
from ncclient import manager
from ncclient.xml_ import to_ele
from paramiko import SSHClient,AutoAddPolicy

class Datacom:
    def __init__(self,server,username,password):
        self.server=server
        self.username=username
        self.password=password
        self.client=self._get_client()
        self.cli=self.client.invoke_shell()
        self.cli.send('screen-length 0 tem\n')
        sleep(1)
        self.cli.recv(9999)

    def _get_client(self):
        client=SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(AutoAddPolicy)
        client.connect(hostname=self.server,username=self.username,password=self.password)
        return client

    def command(self,cmd):
        self.cli.send('{}\n'.format(cmd))
        sleep(2)
        return self.cli.recv(9999).decode()

    def check_fan_fault(self):
        fan_info=self.command('dis fan')
        return fan_info.find('Normal')==-1

    def sftp(self,sfile,dfile):
        client=self._get_client()
        sftp=client.open_sftp()
        print('starting download')
        sftp.get(sfile,dfile)
        print('download finish')
        client.close()

    def close(self):
        self.client.close()

def netconf_by_rpc(device_ip,username,password,rpc_content):
    with manager.connect_ssh(
        host=device_ip,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={'name':'huaweiyang'}
    ) as m:
        rpc_command=to_ele(rpc_content)
        m.rpc(rpc_command)
        print('netconf config by rpc success')

def netconf_syslog_host(device_ip,username,password,syslog_server):
    rpc_content="""
  <edit-config>
    <target>
      <running/>
    </target>
    <config>
      <syslog:syslog xmlns:syslog="urn:ietf:params:xml:ns:yang:ietf-syslog">
        <syslog:log-actions>
          <syslog:remote>
            <syslog:destination>
              <syslog:name>syslog-host</syslog:name>
              <syslog:udp>
                <syslog:address>{}</syslog:address>
                <syslog:port>43</syslog:port>
              </syslog:udp>
              <syslog:destination-facility xmlns:ietf-syslog-types="urn:ietf:params:xml:ns:yang:ietf-syslog-types">ietf-syslog-types:local0</syslog:destination-facility>
            </syslog:destination>
          </syslog:remote>
        </syslog:log-actions>
      </syslog:syslog>
    </config>
  </edit-config>""".format(syslog_server)
    print('using netconf config syslog host')
    netconf_by_rpc(device_ip,username,password,rpc_content)

def netconf_time(device_ip,username,password):
    date=datetime.now()
    time=date.strftime('%Y-%m-%dT00:00:00-%H:%M')
    print(time)
    rpc_content = """
    <sys:set-current-datetime xmlns:sys="urn:ietf:params:xml:ns:yang:ietf-system">
      <sys:current-datetime>{}</sys:current-datetime>
    </sys:set-current-datetime>""".format(time)
    print('using netconf config time')
    netconf_by_rpc(device_ip, username, password, rpc_content)

def datacom_loop(device_ip,username,password,device_name,nc_username,nc_password):
    while True:
        datacom=Datacom(device_ip,username,password)
        with open('command.txt') as f:
            for cmd in f:
                print(datacom.command(cmd))

        if datacom.check_fan_fault():
            print('All fans are fault.')

        try:
            one_day_delta=datetime.now()-last_download_time>=timedelta(days=1)
        except NameError:
            one_day_delta=True
        if one_day_delta:
            netconf_time(device_ip,nc_username,nc_password)
            download_time=datetime.now()
            download_date=download_time.strftime('%Y_%m_%d')
            config_filename='{}_{}.zip'.format(download_date,device_name)
            backup_filename='{}_{}.bak'.format(download_date,device_name)
            datacom.command('save {}'.format(config_filename))
            datacom.command('y')
            datacom.sftp(config_filename,backup_filename)
            last_download_time=download_time
        datacom.close()
        sleep(300)

device_ip='192.168.240.253'
username='python'
password='Huawei@123'
nc_username='netconf'
nc_password='Huawei@123'
device_name='X_T1_AGG1'
syslog_server='10.1.60.2'

if __name__=='__main__':
    try:
        netconf_syslog_host(device_ip,nc_username,nc_password,syslog_server)
        datacom_loop(device_ip,username,password,device_name,nc_username,nc_password)
    except KeyboardInterrupt:
        print('monitor stop')




