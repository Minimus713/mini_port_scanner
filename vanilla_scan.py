import socket
import sys
socket.setdefaulttimeout(0.5) #Set timeout to x sec for all sockets

def vanilla_scan(host_ip):
    COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 161, 443, 445, 465, 514, 587, 993, 995, 1723, 3306, 3389, 5900, 8080]

    port_statuses = {
        'open': [],
        'closed': [],
        'filtered': []
    }

    print(f'Running common port vanilla scan on: {host_ip}')

    for portNum in COMMON_PORTS:
        port_status = single_port_scan(host_ip, portNum)
        if(port_status == 0): 
            port_statuses['closed'].append(portNum)
        elif(port_status == 1): 
            port_statuses['open'].append(portNum)
        elif(port_status == 2): 
            port_statuses['filtered'].append(portNum)
        else:
            print(f'{portNum} failed to scan')
    
    print('Open ports: ', port_statuses['open'])
    print('Closed ports: ', port_statuses['closed'])
    print('Filtered ports: ', port_statuses['filtered'])


def single_port_scan(host_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Status 1 = open
    # Status 0 = closed
    # Status 2 = filtered
    try:
        s.connect((host_ip, port))
        return(1) 
    except socket.timeout:
        return(2)
    except ConnectionRefusedError:
        return(0)
    except KeyboardInterrupt:
        print("Exiting Program.")
        sys.exit()
    except Exception as e:
        print(f"error: {e}")
        pass
    finally:
        s.close()