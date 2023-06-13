import nmap

def count_connected_devices():
    scanner = nmap.PortScanner()
    scanner.scan(hosts="192.168.0.1/24", arguments="-sn")
    
    for host in scanner.all_hosts():
        if 'mac' in scanner[host]['addresses']:
            mac_address = scanner[host]['addresses']['mac']
            print(f"IP: {host}\tMAC Address: {mac_address}")

count_connected_devices()
