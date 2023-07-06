import yaml

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.171.141',
    'username': 'Shamil',
    'password': 'shomashama',
    'secret': 'enablepass'}

with open('yaml_R6.yaml', 'w') as f:
    yaml.dump(cisco_router, f)