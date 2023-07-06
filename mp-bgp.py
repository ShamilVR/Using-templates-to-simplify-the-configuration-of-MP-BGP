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
        if interface_type in ['eth', 'lo', 'fa', 'gi', 'e', 'ethernet', 'fastethernet', 'gigabitethernet', 'loopback', 'fast', 'gig']:
            ip_address = input("Enter the IP address and mask (e.g., 192.168.1.1/24): ")
            interface_config = interface_template.render(interface_type=interface_type, ip_address=ip_address)
            interface_configs.append(interface_config)
            print(f"Configured {interface_type} interface with IP address {ip_address}.")
        else:
            print("Invalid interface type. Please try again.")

        return_to_previous = input("Do you want to configure another interface or proceed with configuring OSPF (yes/OSPF): ").lower()
        if return_to_previous in ['no', 'OSPF', 'os', 'osp', 'proceed', 'o', 'ospf', 'OS', 'OSP', 'O']:
            return interface_configs

def configure_ospf_process():
    ospf_process_number = input("Enter the OSPF process number: ")
    ospf_config = f"router ospf {ospf_process_number}"
    return ospf_config


def configure_ospf(ospf_process_number):
    ospf_template = Template('''
 network {{ network }} area {{ area }}
''')
    ospf_configs = []

    while True:
        network = input("Enter the network address and wildcard mask (e.g., 192.168.0.0 0.0.0.255): ")
        area = input("Enter the OSPF area for the network: ")
        ospf_config = ospf_template.render(network=network, area=area)
        ospf_configs.append(ospf_config)
        print(f"Configured OSPF network: {network} with area: {area}.")

        return_to_previous = input(
            "Do you want to add another network? (yes/no): ").lower()
        if return_to_previous == 'finish':
            return ospf_configs
        elif return_to_previous in ['no', 'bgp', 'BGP', 'proceed', 'b']:
            break

    return ospf_configs



def configure_bgp_asn():
    bgp_asn = input("Enter the BGP AS number: ")
    bgp_config = f"router bgp {bgp_asn}"
    return bgp_config


def configure_bgp_neighbors():
    neighbor_template = Template("neighbor {{ neighbor.ip }} remote-as {{ neighbor.asn }}")
    neighbors = []

    while True:
        neighbor_ip = input("Enter the neighbor IP address: ")
        neighbor_asn = input("Enter the neighbor AS number: ")
        neighbors.append({"ip": neighbor_ip, "asn": neighbor_asn})

        return_to_previous = input("Do you want to configure another BGP neighbor or finish the configuration? (yes/finish): ").lower()
        if return_to_previous in ['no', 'finish', 'end', 'stop', 'f', 'fin']:
            break

    neighbor_configs = []
    for neighbor in neighbors:
        neighbor_config = neighbor_template.render(neighbor=neighbor)
        neighbor_configs.append(neighbor_config)

    return neighbor_configs

def configure_mpls_ldp(interface):
    mpls_ldp_template = Template('''
mpls ldp router-id Loopback0 force
interface {{ interface }}
 mpls ip
''')
    mpls_ldp_config = mpls_ldp_template.render(interface=interface)
    print("MPLS and LDP configuration for P router:")
    print(mpls_ldp_config)
    pyperclip.copy(mpls_ldp_config)
    print("Configuration copied to clipboard.")

def configure_mp_bgp():
    router_role = input("Step 1: Specify the router role (provider's edge router or provider's router): ").lower()

    if router_role in ['pe', "provider's edge router", "provider's edge", 'providers edge', 'providers edge router']:
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
            print(
                f"Configured VRF: {vrf_name} with RD: {rd}, route-target export: {rt_export}, route-target import: {rt_import}.")

            return_to_previous = input("Do you want to configure another VRF? (yes/no): ").lower()
            if return_to_previous == 'no':
                break

        print("MP-BGP configuration completed.")
        return vrf_configs

    elif router_role in ['p', "provider's router"]:
        print("Performing MPLS and LDP configuration for P router.")
        interface = input("Step 2: Enter the interface on which you want to enable MPLS: ")
        configure_mpls_ldp(interface)
        return []

    else:
        print("Invalid router role. Please try again.")


def main():
    basic_config = input("Step 1: Do you require basic configuration? Enter 'yes' or 'no': ").lower()

    if basic_config == 'yes':
        interface_configs = configure_interface()
        ospf_process_number = configure_ospf_process()
        ospf_configs = configure_ospf(ospf_process_number)
        bgp_asn_config = configure_bgp_asn()
        bgp_neighbor_configs = configure_bgp_neighbors()
        vrf_configs = []
    elif basic_config == 'no':
        routing_protocol = input("Step 1: Which routing protocol do you want to configure, OSPF, BGP, or MP-BGP? ").lower()

        if routing_protocol in ['ospf', 'o', 'OSPF', 'os', 'osp', 'OS', 'OSP', 'O']:
            interface_configs = []
            ospf_process_number = configure_ospf_process()
            ospf_configs = configure_ospf(ospf_process_number)
            bgp_asn_config = ''
            bgp_neighbor_configs = []
            vrf_configs = []
        elif routing_protocol in ['bgp', 'bg', 'b', 'BGP', 'BG', 'B']:
            interface_configs = []
            ospf_process_number = ''
            ospf_configs = []
            bgp_asn_config = configure_bgp_asn()
            bgp_neighbor_configs = configure_bgp_neighbors()
            vrf_configs = []
        elif routing_protocol in ['mp-bgp', 'MP', 'M', 'm', 'mp', 'mpbgp', 'MPBGP']:
            interface_configs = []
            ospf_process_number = ''
            ospf_configs = []
            bgp_asn_config = ''
            bgp_neighbor_configs = []
            vrf_configs = configure_mp_bgp()
        else:
            print("Invalid routing protocol. Please try again.")
            return

    configuration_parts = interface_configs + [ospf_process_number] + ospf_configs + [bgp_asn_config] + bgp_neighbor_configs + vrf_configs
    configuration_parts = [part for part in configuration_parts if part is not None]
    configuration = "\n".join(map(str, configuration_parts))

    print("Complete configuration:\n")
    print(configuration)
    pyperclip.copy(configuration)
    print("Configuration copied to clipboard.")

if __name__ == "__main__":
    main()


