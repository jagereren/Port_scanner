import sys
import socket
from datetime import datetime

def port_scanner():
    target = input("Enter a target to scan: ") 
    remoteServerIP = socket.gethostbyname(target)
    socket.setdefaulttimeout(2)
    print("="*50)
    print("Target adress : "+remoteServerIP)
    print("="*50)
    print("Scanning ports...")
    print("="*50)
    open_ports = []
    try :
        for port in range(1,400):
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = socket_.connect_ex((remoteServerIP, port))
            print(f"Testing port {port}")
            if(result==0):
                print("Open")
                open_ports.append(port)
        print("Open ports : ",open_ports)
    except KeyboardInterrupt:
        print("Ctrl+C interruption")
        sys.exit()

    except socket.gaierror:
        print("Hostname couldn't be resolved")
        sys.exit()

    except socket.error:
        print("Couldn't connect to the server")
        sys.exit()

port_scanner()
