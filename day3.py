# 1-List of Servers
# 	Task: Create a list of server hostnames and perform operations on it.
# 		Create a list of server hostnames (e.g., ["server1", "server2", "server3"]).
# 		Remove a server from the list.
# 		Check if a specific server exists in the list.
# 		Print all servers in the list.
server_names=["server1", "server2", "server3"]
server_names.append("server4")  
print(server_names)
server_names.pop(1)
print(server_names)  
# server_names.remove("server2")  
# print(server_names)
check="server10"
if  check in server_names:
    print(f"{check} is in the list.")
else:
    print(f"{check} is not in the list.")
# 2-Use a tuple to store immutable server configuration details.
# 	Create a tuple containing server configuration details (e.g., ("192.168.1.1", "8080", "root")).
# 	Unpack the tuple into separate variables for IP, port, and username.
# 	Print the configuration details.
t=("192.168.1.1", "8080", "root")
IP,port,username=t
print(IP,port,username)
print(f"IP Address: {IP}")
print(f"Port: {port}")
print(f"Username: {username}")

# 3-Use a dictionary to manage server inventory.
# 	Create a dictionary where the keys are server hostnames and the values are their IP addresses.
# 	Add a new server to the dictionary.
# 	Update the IP address of an existing server.
# 	Remove a server from the dictionary.
# 	Print all servers and their IP addresses.
server_inventory = {
    "server1": "192.168.1.1",
    "server2": "192.168.1.2"   
}
server_inventory["server3"]="192.168.1.3"
print(server_inventory)
server_inventory["server2"]="192.168.1.5"
print(server_inventory)
del server_inventory["server1"]
print(server_inventory)

# 4-Write a function to check the status of a server.
# 	Create a function check_server_status that takes a server hostname as input.
# 	Use a dictionary to store server statuses (e.g., {"server1": "online", "server2": "offline"}).
# 	The function should return the status of the server or "Server not found" if the server doesn't exist
server= {
    "server1": "online",
    "server2": "offline",
    "server3": "online",
}

def  check_server_status(name):
    if  name in server:
        return server[name]
    else:
        return "Server not found"
check_server_status("server2")
print(check_server_status("server2"))
check_server_status("server10")
print(check_server_status("server10"))
#-------------------------------------------------------------------------------------------------------
# 5-Analyze server logs stored as a list of tuples.
# 	Create a list of tuples where each tuple represents a log entry (e.g., ("server1", "error", "2023-10-01")).
# 	Count how many error logs are in the list.
# 	Extract all log entries for a specific server.
logs=[ ("server1", "error", "2023-10-01"), ("specific-server", "error", "2023-10-02")]
count=0
for err in logs :
    if err[1]=="error":
        count+=1
print(count)
        # if err[2]=="error":
        #     count+=1
        #     print(count)
####specific-server######
specific_servers=[]
for specific in logs:
    if specific[0]=="specific-server":
        specific_servers.append(specific)
        print(f"the specific is : {specific_servers}")
    else:
        print("there is no specific_servers")
#____________________________________________________________
def table(n):
    table = []
    for i in range(1, n+1):
        row = []
        for j in range(1, i+1):
            row.append(i * j)
        table.append(row)
    return table

n=int(input("Enter a number: "))

table = table(n)
print(table)



