#demo to check the port of my localhost if it's open or not using socket module
import socket  #check connection of a server or check ports
import sys
ip = sys.argv[1]  # Get the IP from user input

try:
    hostnamet = socket.gethostbyname(ip)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket.AF_INET means >> using ipv4  and socket.SOCK_STREAM means using tcp protocl

    for port in range(1, 90): 
      # connect_ex is fn to connect the port and if it's open return 0 and if others return any num
      res = s.connect_ex((hostnamet, port))
      if res==0:
           f=open(f'server{ip}.logs','a')
           f.write(f'port {port}is open\n')
           f.close()
           print(f'{res} {port}')
except socket.gaierror:
    print("Invalid IP address")  # If the provided IP is incorrect
except socket.error:
    print("Internet failure")  # If there is an issue with the internet connection
except KeyboardInterrupt:
    print("Someone canceled the script")  # If the user interrupts the script
    sys.exit(0)
else:
    print("all ports checked")

