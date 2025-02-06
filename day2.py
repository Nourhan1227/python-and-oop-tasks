# 1-Convert the following temperatures from Celsius to Fahrenheit:
# 	GET TEMP FROM USER  	Formula: F = (C * 9/5) + 32 Print the converted temperatures.

C=float(input("Pls Enter the temperatures in Celsius"))
F=(C * 9/5) + 32
print(f"the temperatures from Celsius to Fahrenheit is {F}")



#--------------------------------------------------------------------------------------------------------
	
# 2-Write a script that takes a server hostname (e.g., "web-server-01") and extracts the numeric part (01) from the string. Print the extracted number as an integer.
hostname = input("Enter the server hostname (like 'web-server-01') ")
numeric_part=int(hostname.split('-')[-1])
print(numeric_part)
#--------------------------------------------------------------------------------------------------------


#3-Write a script that checks if a given port number is valid (valid ports are between 0 and 65535). Print True if valid, otherwise False.
port=int(input("enter the port number:"))
if  0 <= port <= 65535:
    print("the port number is valid ")
else: 
    print("the port number is invalid")

#-------------------------------------------------------------------------------

# 4-Simulate a login system:
# 	Ask the user to input a username and password.
# 	Check if the username is "admin" and the password is "admin123".
# 	Print "Access granted" if both are correct, otherwise print "Access denied".
username=input("enter the username: ")
password=input("enter the password: ")
if username =="admin" :
    if password=="admin123":
        print("Access granted" )
    else:
        print("Access denied")


#-----------------------------------------------------------------------------------
# 5-Write a script that checks the available disk space:
# 	GET DISK FROM USER
# 	If the disk space is less than 10%, print "Warning: Low disk space!".
# 	If the disk space is between 10% and 20%, print "Warning: Disk space is getting low.".
# 	Otherwise, print "Disk space is sufficient.".
percentage=float(input("pls enter the disk space in num:"))
if percentage < 10:
    print("Warning: Low disk space!")
elif 10 <= percentage <= 20:
    print("Warning: Disk space is getting low.")
else:
    print("Disk space is sufficient.")
#--------------------------------------------------------------------------------------------------
#6-Iterate through the list and print each server name in uppercase
server_name= ['web-server-01', 'web-server-02', 'db-server-03']
for server in server_name:
    print(server.upper())