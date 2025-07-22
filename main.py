from vanilla_scan import vanilla_scan
import socket

#0-1023 are well-known and standardized ports assigned by the IANA (Internet Assigned Numbers Authority)

def main():
    host_ip = socket.gethostbyname('www.google.com')
    print(host_ip)

    print('Running vanilla scan: ')
    vanilla_scan(host_ip)

main()