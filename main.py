

#0-1023 are well-known and standardized ports assigned by the IANA (Internet Assigned Numbers Authority)

def main():
    startPort = 0
    finalPort = 65535
    for portNum in range(startPort, finalPort+1):
        print('Pinging port number', portNum)

main()