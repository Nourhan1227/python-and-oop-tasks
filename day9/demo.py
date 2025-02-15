#######script for user mngmnt system create delete permadd
import subprocess

#add user
def add_user(username):
        subprocess.run(["sudo", "useradd", username])
        print(f"{username} added")
        
#delte user
def delete_user(username):
        subprocess.run(["sudo", "userdel", "-r", username])
        print(f"{username} deleted")

#add user to sec-grp
def modify_user_permissions(username, group="sudo"):
        subprocess.run(["sudo", "usermod", "-aG", group, username])
        print(f"{username} is added to this group {group}")


x=add_user("doha")
print(x)

y=modify_user_permissions("doha", "demogrp")
print(y)

z=delete_user("ali1")
print(z)
