router_name = input('')
print('en\nconf t\nip domain lookup\nline console 0\nexec-tim 0\nrouter ospf 1')

if router_name == '2':
    towards_what1 = '23.1'
    towards_what2 = '26.1'
    intlo = '2.2.2.2'
    print('int eth 0/3\nip add 192.168.21.1 255.255.255.252\nno shut')
    print(f'int eth 0/0\nip add 10.10.{towards_what1} 255.255.255.252\nip ospf 1 area 0\nno shut')
    print(f'int eth0/1\nip add 10.10.{towards_what2} 255.255.255.252\nip ospf 1 area 0\nno shut')
    print(f'int lo0\nip add {intlo} 255.255.255.255\nip ospf 1 area 0')
elif router_name == '3':
    towards_what1 = '23.2'
    towards_what2 = '43.2'
    intlo = '3.3.3.3'
    print(f'int eth 0/0\nip add 10.10.{towards_what1} 255.255.255.252\nip ospf 1 area 0\nno shut')
    print(f'int eth0/1\nip add 10.10.{towards_what2} 255.255.255.252\nip ospf 1 area 0\nno shut')
    print(f'int lo0\nip add {intlo} 255.255.255.255\nip ospf 1 area 0')
elif router_name == '4':
    towards_what1 = '46.1'
    towards_what2 = '43.1'
    intlo = '4.4.4.4'
    print('int eth 0/3\nip add 192.168.45.1 255.255.255.252\nno shut')
    print(f'int eth 0/0\nip add 10.10.{towards_what1} 255.255.255.252\nip ospf 1 area 0\nno shut')
    print(f'int eth0/1\nip add 10.10.{towards_what2} 255.255.255.252\nip ospf 1 area 0\nno shut')
    print(f'int lo0\nip add {intlo} 255.255.255.255\nip ospf 1 area 0')
elif router_name == '6':
    towards_what1 = '46.2'
    towards_what2 = '26.2'
    intlo = '6.6.6.6'
    print(f'int eth 0/0\nip add 10.10.{towards_what1} 255.255.255.252\nip ospf 1 area 0\nno shut')
    print(f'int eth0/1\nip add 10.10.{towards_what2} 255.255.255.252\nip ospf 1 area 0\nno shut')
    print(f'int lo0\nip add {intlo} 255.255.255.255\nip ospf 1 area 0')