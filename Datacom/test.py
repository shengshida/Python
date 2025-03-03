from datetime import datetime, timedelta
from time import sleep
from paramiko import SSHClient, AutoAddPolicy
from ncclient import manager
from ncclient.xml_ import to_ele


class DataCom:
    def __init__(self, server, username, password):
        self.server= server
        self.username = username
        self.passwrod = password
        self.client = self._get_clinet()
        self.cli = self.client.invoke_shell()
        self.cli.send("screen-l 0 te\n")
        sleep(1000)
        self.cli.recv(9999)


    def _get_clinet(self):
        client = SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(AutoAddPolicy)
        client.connect(hostname=self.server, username=self.username, password=self.passwrod)
        return client

    def command(self, cmd):
        self.cli.send("{}\n".format(cmd))
        sleep(2)
        return self.cli.recv(9999).decode()

    def check_fan_faulty(self):
        fan_info = self.command("dis fan")
        return fan_info.find("Normal") == -1

    def sftp(self, sfilename, dfilename):
        client = self._get_clinet()
        sftp = client.open_sftp()
        print("download starting.")
        sftp.get(sfilename, dfilename)
        print("download finsh.")

    def close(self):
        self.client.close()


def netconf_by_prc(device_ip, nc_useranem, nc_password, rpc_content):
    with manager.connect_ssh(host=device_ip, username=nc_useranem, password=nc_password, hostkey_verify=False, device_params={"name":"huaweiyang"}) as m:
        m.rpc(to_ele(rpc_content))
        print("netconf config by rpc success.")

def netconf_syslog_host(device_ip, nc_username, nc_password, syslog_server):
    rpc_content = """"
    
    """.format(syslog_server)
    print("netconf config syslog host.")
    netconf_by_rpc(device_ip, nc_username, nc_password, rpc_content)

def netconf_time(device_ip, nc_username, nc_password):
    time = datetime.now().strftime("%Y-%m-%dT00:00:00-%H:%M")
    rpc_content = """
    
    """.format(time)
    print("netconf config time.")
    netconf_by_rpc(device_ip, nc_username, nc_password, rpc_content)

def datacom_loop(device_ip, device_name, username, password, nc_username, nc_password):
    while True:
        datacom = DataCom(device_ip, username, password)
        with open("command.txt") as f:
            for cmd in f:
                print(datacom.command(cmd))

        if datacom.check_fan_faulty():
            print("Alls fan are faulty.")

        try:
            one_day_delta = datetime.now() - last_download_time >= timedelta(days=1)
        except NameError:
            one_day_delta = True

        if one_day_delta :
            netconf_time(device_ip, nc_username, nc_password)
            download_time = datetime.now()
            download_date = download_time.strftime("%Y_%m_%d")
            config_file = "{}_{}.zip".format(device_name, download_date)
            backup_file = "{}_{}.bak".format(device_name, download_date)
            datacom.command("save fo {}".format(config_file))
            datacom.sftp(config_file, backup_file)
            last_download_time = download_time

        datacom.close()
        sleep(300)


device_name = ""
device_ip = ""
username = ""
password = ""
nc_username = ""
nc_password = ""
syslog_server = ""
i
if __name__ == "__main__" :
    try :
        netconf_syslog_host(device_ip, nc_username, nc_password, syslog_server)
        datacom_loop(device_ip, device_name, username, password, nc_username, nc_password)

    except KeyboardInterrupt :
        print("Monitor Stop.")