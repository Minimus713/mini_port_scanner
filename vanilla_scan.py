import socket
import sys

def vanilla_scan(port_num):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket.setdefaulttimeout(1)
    print("Socket created successfully")        
    try:
        host_ip = socket.gethostbyname('www.google.com')
        print(host_ip)
        conn = s.connect((host_ip, port_num))
        print('nun')
        print(conn)
        #print(s.recv(1024))
    except KeyboardInterrupt:
        print("Exiting Program.")
        sys.exit()
    except Exception as e:
        pass


    conn.close()
    return port_num
