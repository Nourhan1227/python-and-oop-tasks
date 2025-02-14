class Server:
    count = 0  
    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address
        Server.count += 1