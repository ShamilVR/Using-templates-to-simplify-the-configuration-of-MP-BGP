from jinja2 import Template
import pyperclip

def configure_interface():
    interface_template = Template('''
interface {{ interface_type }}
 ip address {{ ip_address }}
''')
    interface_configs = []

    while True:
        interface_type = input("Enter the interface type (eth, lo, fa, gi): ").lower()
        if interface_type in ['eth', 'lo', 'fa', 'gi']:
            ip_address = input("Enter the IP address and mask (e.g., 192.168.1.1/24): ")
            interface_config = interface_template.render(interface_type=interface_type, ip_address=ip_address)
            interface_configs.append(interface_config)
            print(f"Configured {interface_type} interface with IP address {ip_address}.")
        else:
            print("Invalid interface type. Please try again.")

        return_to_previous = input("Do you want to return to the previous step? (yes/no): ").lower()
        if return_to_previous == 'no':
            return interface_configs

def configure_ospf():
    ospf_template = Template('''
router ospf
 network {{ network }}
''')
    ospf_configs = []

    while True:
        network = input("Enter the network address and mask (e.g., 192.168.0.0/24): ")
        ospf_config = ospf_template.render(network=network)
        ospf_configs.append(ospf_config)
        print(f"Configured OSPF network: {network}.")

        return_to_previous = input("Do you want to return to the previous step? (yes/no): ").lower()
        if return_to_previous == 'no':
            return ospf_configs

def configure_bgp():
    bgp_template = Template('''
router bgp {{ asn }}
 neighbor {{ neighbor_ip }} remote-as {{ neighbor_asn }}
''')
    bgp_configs = []

    while True:
        asn = input("Enter the BGP AS number: ")
        neighbor_ip = input("Enter the neighbor IP address: ")
        neighbor_asn = input("Enter the neighbor AS number: ")
        bgp_config = bgp_template.render(asn=asn, neighbor_ip=neighbor_ip, neighbor_asn=neighbor_asn)
        bgp_configs.append(bgp_config)
        print(f"Configured BGP neighbor: {neighbor_ip} with ASN: {neighbor_asn}.")

        return_to_previous = input("Do you want to return to the previous step? (yes/no): ").lower()
        if return_to_previous == 'no':
            return bgp_configs

def configure_mp_bgp():
    router_role = input("Step 1: Specify the router role (pe or p): ").lower()

    if router_role == 'pe':
        vrf_configs = []

        while True:
            interface_template = Template('''
interface {{ interface }}
 ip vrf forwarding {{ vrf_name }}
 ip address {{ ip_address }}
''')
            vrf_name = input("Enter the VRF name: ")
            interface = input("Enter the interface number and type (e.g., GigabitEthernet0/0): ")
            ip_address = input("Enter the IP address and mask (e.g., 192.168.1.1/24): ")
            interface_config = interface_template.render(interface=interface, vrf_name=vrf_name, ip_address=ip_address)
            vrf_configs.append(interface_config)
            print(f"Configured VRF interface: {interface} with VRF name: {vrf_name}, IP address: {ip_address}.")

            return_to_previous = input("Do you want to configure another interface? (yes/no): ").lower()
            if return_to_previous == 'no':
                break

        vrf_template = Template('''
ip vrf {{ vrf_name }}
 rd {{ rd }}
 route-target export {{ rt_export }}
 route-target import {{ rt_import }}
''')


        while True:
            vrf_name = input("Step 3: Enter the VRF name: ")
            rd = input("Enter the RD (Route Distinguisher) value: ")
            rt_export = input("Enter the route-target export value: ")
            rt_import = input("Enter the route-target import value: ")
            vrf_config = vrf_template.render(vrf_name=vrf_name, rd=rd, rt_export=rt_export, rt_import=rt_import)
            vrf_configs.append(vrf_config)
            print(f"Configured VRF: {vrf_name} with RD: {rd}, route-target export: {rt_export}, route-target import: {rt_import}.")

            return_to_previous = input("Do you want to configure another VRF? (yes/no): ").lower()
            if return_to_previous == 'no':
                break

        print("MP-BGP configuration completed.")
        return vrf_configs

    elif router_role == 'p':
        print("Performing MPLS and LDP configuration for P router.")


    else:
        print("Invalid router role. Please try again.")

def main():
    basic_config = input("Step 1: Do you require basic configuration? Enter 'yes' or 'no': ").lower()

    if basic_config == 'yes':
        interface_configs = configure_interface()
        ospf_configs = configure_ospf()
        bgp_configs = configure_bgp()
    elif basic_config == 'no':
        routing_protocol = input("Step 1: Which routing protocol do you want to configure, OSPF, BGP or mp-bgp? ").lower()

        if routing_protocol == 'ospf':
            ospf_configs = configure_ospf()
            bgp_configs = []
        elif routing_protocol == 'bgp':
            ospf_configs = []
            bgp_configs = configure_bgp()
        elif routing_protocol == 'mp-bgp':
            vrf_configs = configure_mp_bgp()
            interface_configs = []
            ospf_configs = []
            bgp_configs = []
        else:
            print("Invalid routing protocol. Please try again.")
            return

    configuration = "\n".join(interface_configs + ospf_configs + bgp_configs + vrf_configs)
    print("Complete configuration:\n")
    print(configuration)
    pyperclip.copy(configuration)
    print("Configuration copied to clipboard.")

if __name__ == "__main__":
    main()
