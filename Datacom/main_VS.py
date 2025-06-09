from datetime import datetime,timedelta
from time import sleep
from ncclient import manager
from ncclient.xml_ import to_ele
from paramiko import SSHClient,AutoAddPolicy

class Datacom:
        def __init__(self,server,username,password):
            self.server = server
            self.username = username
            self.password= password

            self.client = self._get_client()
            self.cli = self.client.invoke_shell()
            self.cli.send("scr 0 te\n")
            sleep(5)
            self.cli.recv(9999)

        def _get_client(self):
            client = SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(AutoAddPolicy)
            client.connect(self.server,username=self.username,password=self.password)
            return client

        def command(self,cmd):
            self.cli.send('{}\n'.format(cmd))
            sleep(1)
            return self.cli.recv(9999).decode()

        def check_fan_fault(self):
            fan_info = self.command('display fan')
            return fan_info.find('Normal') == -1

        def download_config(self,target,config_path='/vrpcfg.zip'):
            print('download starting...')
            client = self._get_client()
            sftp = client.open_sftp()
            sftp.get(config_path,target)
            client.close()

        def close(self):
            self.client.close()

def datacom_loop(device_ip, username, password, device_name):
    while True:
        datacom = Datacom(device_ip, username, password)
        with open('command.txt') as f:
            for command in f:
                print(datacom.command(command))
        if datacom.check_fan_fault():
            print('All fans are faulty')

        try:
            one_day_delta = datetime.now() - last_downloadtime >= timedelta(days=1)
        except NameError:
            one_day_delta = True

        if one_day_delta:
            downloadtime = datetime.now()
            download_date = downloadtime.strftime('%Y_%m_%d')

            config_filename = '{}_{}.zip'.format(download_date, device_name)
            backup_filename = '{}_{}.bak'.format(download_date, device_name)
            datacom.command('save force {}'.format(config_filename))
            datacom.download_config(config_filename, backup_filename)

        last_downloadtime = downloadtime

        datacom.close()
        sleep(5*60)

def netconf_by_rpc(device_ip, username, password, rpc_content):
    with manager.connect_ssh(host = device_ip, username = username, password = password, hostkey_verify = False, device_params = {'name':'huaweiyang'}) as m:
        rpc_command = to_ele(rpc_content)
        m.rpc(rpc_command)
        print('using netconf configuration device has been success')

def netconf_config_syslog_host(device_ip, username, password, log_server):
    rpc_content = """
    
    """.format(log_server)

    print('using netconf configuration syslog host...')
    netconf_by_rpc(device_ip, username, password, rpc_content)

device_ip = '10.255.255.100'
log_server = '10.1.60.2'
username = 'admin@huawei.com'
password = 'Huawei@123'
nc_username = 'admin@huawei.com'
nc_password = 'Huawei@123'
device_name = 'X_T1_AGG1'

if __name__ == '__main__':
    try:
        netconf_config_syslog_host(device_ip,nc_username,nc_password,log_server)
        datacom_loop(device_ip,username,password,device_name)
    except KeyboardInterrupt:
        print('monitor stopped')