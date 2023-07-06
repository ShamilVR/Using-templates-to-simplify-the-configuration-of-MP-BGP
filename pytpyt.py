import netmiko
import yaml

with open('logpass.yaml') as f:
    devices = yaml.safe_load(f)
for dev in devices:
    ssh = netmiko.ConnectHandler(**dev)
    ssh.enable()
    ssh.send_command('sh clock')