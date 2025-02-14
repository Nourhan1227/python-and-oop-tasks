import nmap
import sys

ip = sys.argv[1]  
scanner = nmap.PortScanner()

try:
    scanner.scan(ip, '1-90')  
    for port in scanner[ip]['tcp']:
        if scanner[ip]['tcp'][port]['state'] == 'open':
            print(f"Port {port} is open")
except nmap.PortScannerError:
    print("Nmap not found or an error occurred")
except KeyboardInterrupt:
    print("Someone canceled the script")
    sys.exit(0)
except Exception as e:
    print(f"Error: {e}")
