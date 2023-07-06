from concurrent.futures import ThreadPoolExecutor
import netmiko
import yaml

def ssh_connection(devices_data, command):
    with netmiko.ConnectHandler(**devices_data) as ssh:
        ssh.enable()
        x = ssh.send_config_set(command)
        return x

with open('logpass.yaml') as file:
    devices = yaml.safe_load(file)

with ThreadPoolExecutor(max_workers=2) as ex:
    cmds = ['ip pim rp-address 3.3.3.3']
    result = ex.map(ssh_connection, devices, [(cmds)]*len(devices))
    for device in result:
        print(device)
