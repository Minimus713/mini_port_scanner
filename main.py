from vanilla_scan import vanilla_scan
import ipaddress
import socket
import sys

#0-1023 are well-known and standardized ports assigned by the IANA (Internet Assigned Numbers Authority)
default_test_ip = '8.8.8.8'

def get_ip_from_user():
    ip = input('Enter the IP address or hostname to scan: ').strip()

    if not ip:
        print(f'No input given, using default test IP: {default_test_ip}')
        return default_test_ip
    
    try:
        ipaddress.ip_address(ip)
        return ip
    except Exception:
        try:
            resolved_ip = socket.gethostbyname(ip)
            return resolved_ip
        except Exception:
            print(f'Invalid input entered, exiting.')
            sys.exit()
    

def main():
    host_ip = get_ip_from_user()
    
    vanilla_scan(host_ip)

main()