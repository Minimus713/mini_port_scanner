import socket
import sys

def vanilla_scan(port_num):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.settimeout(1)
    print("Socket created successfully")        
    try:
        host_ip = socket.gethostbyname('www.google.com')
        print(host_ip)
        conn = s.connect((host_ip, port_num))
        print(conn)
        print(s.recv(1024))
        conn.close()
    except socket.timeout:
        print('port filtered or no response.')
    except KeyboardInterrupt:
        print("Exiting Program.")
        sys.exit()
    except Exception as e:
        pass


    return port_num
