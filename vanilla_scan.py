import socket
import sys
socket.setdefaulttimeout(1) #Set timeout to 1 sec for all sockets

def vanilla_scan(host_ip):
    startPort = 1
    finalPort = 2#65535


    for portNum in range(startPort, finalPort+1):
        print('Pinging port number', portNum)
        single_port_scan(host_ip, portNum)

def single_port_scan(host_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        conn = s.connect((host_ip, port))
        print(conn)
        print(s.recv(1024))
        conn.close()
    except socket.timeout:
        print('port filtered or no response.')
    except KeyboardInterrupt:
        print("Exiting Program.")
        sys.exit()
    except ConnectionRefusedError:
        print('closed')
    except Exception as e:
        print(f"error: {e}")
        pass