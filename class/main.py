from server import Server  

object1 = Server("webserver", "192.168.1.1")
object2 = Server("dbserver", "192.168.1.2")

print(f"Server {object1.name} ip is : {object1.ip_address}")
print(f"Server {object2.name} ip is : {object2.ip_address}")
print(f"Total num of servers is : {Server.count}")