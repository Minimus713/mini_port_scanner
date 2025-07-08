from vanilla_scan import vanilla_scan

#0-1023 are well-known and standardized ports assigned by the IANA (Internet Assigned Numbers Authority)

def main():
    startPort = 1
    finalPort = 2#65535
    for portNum in range(startPort, finalPort+1):
        print('Pinging port number', portNum)
        beeep = vanilla_scan(portNum)
        print(beeep)

main()