import pyperclip
def config_creation(router_name):
    if router_name == '2':
        towards_what1 = '23.1'
        towards_what2 = '26.1'
        towards_what3 = '21.1'
        hostname = 'R2'
        intlo = '2.2.2.2'
        y = (f'int eth 0/3\nip add 192.168.{towards_what3} 255.255.255.252\nno shut\n')
    elif router_name == '3':
        towards_what1 = '23.2'
        towards_what2 = '43.2'
        hostname = 'R3'
        intlo = '3.3.3.3'
    elif router_name == '4':
        towards_what1 = '46.1'
        towards_what2 = '43.1'
        hostname = 'R4'
        intlo = '4.4.4.4'
        towards_what3 = '45.1'
        y = (f'int eth 0/3\nip add 192.168.{towards_what3} 255.255.255.252\nno shut\n')
    elif router_name == '6':
        towards_what1 = '46.2'
        towards_what2 = '26.2'
        hostname = 'R6'
        intlo = '6.6.6.6'

    x = (f'en\nconf t\nhostname {hostname}\nip domain lookup\nip domain-name shamsham.local\n'
         'username Shamil password shomashama\nline vty 0 4\ntransport input ssh\nlogin local\n'
         'crypto key generate rsa\n2048\nip ssh version 2\nline console 0\nexec-tim 0\nrouter ospf 1\n')
    z = (f'int eth 0/0\nip add 10.10.{towards_what1} 255.255.255.252\nip ospf 1 area 0\nno shut\n'
         f'int eth 0/1\nip add 10.10.{towards_what2} 255.255.255.252\nip ospf 1 area 0\n'
         f'no shut\nint lo0\nip add {intlo} 255.255.255.255\nip ospf 1 area 0\ndo copy running-config startup-config\n')
    abc = x+z
    pyperclip.copy(abc)
    try:
        pyperclip.copy(abc+y)
    except(UnboundLocalError):
        pyperclip.paste()

e = input()
config_creation(e)