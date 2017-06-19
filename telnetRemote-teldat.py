import getpass
import sys
import telnetlib

HOST = "192.168.1.1"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("status\n")
#tn.write("show config\n")

print tn.read_all()