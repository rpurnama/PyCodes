#!/usr/bin/python3

"""
Version	: 0.0 (Beta-release)
Author	: Rakhmadian Purnama <rakhmadian_purnama@yahoo.com>
Source	: http://rpoernama.wordpress.com

This is a Python script to generate intial configuration for INE CCIE R&S v5 Lab. It's distributed for free to help CCIE hunter during their study.
No fee and specific permission is required to use this script but please take at your own risk.

Supported features:
	-> Add / Update Database Router
	-> List Database Router
	-> Push Initial Configuration based on INE CCIE R&S v5 Lab Workbook

Requirements:
	>> It has been tested and working fine on Linux (Ubuntu) environment
	>> Python3 and later
	>> Netmiko library
	>> Tkinter library
	>> GNS3 v2.1.3 and later
	>> INE CCIE R&S v5 Lab Workbook + Edited Topology (can be found at https://github.com/rpurnama/CCIE_RS_v5.git)
"""

#Import all Python modules (Tkinter and Netmiko may need installed separately on your environment)
import sys
import os
import sqlite3
from netmiko import ConnectHandler
from datetime import datetime
from tkinter import filedialog
from tkinter import *

#define connection to database and cursor
conn = sqlite3.connect("devices.db")
curs = conn.cursor()

#define folder location
#folder = Tk()
#folder_location = filedialog.askdirectory()

#create table
def initial_table():
	#original
	#curs.execute("CREATE TABLE IF NOT EXISTS tbDevice(hostname TEXT, type TEXT, ip_addr TEXT, tcp_port INTEGER)")
	
	#modified
	curs.execute("CREATE TABLE IF NOT EXISTS tbDevice(ip_addr TEXT NOT NULL, \
	telnet_port INTEGER default 23, \
	hostname TEXT NOT NULL, \
	username VARCHAR(10) default '', \
	password VARCHAR(8) default 'cisco', \
	secret VARCHAR(8) default '', \
	device_type TEXT default 'unknown', \
	UNIQUE(ip_addr), UNIQUE(hostname))")


#Reset Database
def reset_db():
	#Default IOS Router
	curs.execute("INSERT OR REPLACE INTO tbDevice VALUES('192.168.122.101', 23, 'R1', '', 'cisco', 'ciscosec', 'router')")
	curs.execute("INSERT OR REPLACE INTO tbDevice VALUES('192.168.122.102', 23, 'R2', '', 'cisco', 'ciscosec', 'router')")
	curs.execute("INSERT OR REPLACE INTO tbDevice VALUES('192.168.122.103', 23, 'R3', '', 'cisco', 'ciscosec', 'router')")
	curs.execute("INSERT OR REPLACE INTO tbDevice VALUES('192.168.122.104', 23, 'R4', '', 'cisco', 'ciscosec', 'router')")
	curs.execute("INSERT OR REPLACE INTO tbDevice VALUES('192.168.122.105', 23, 'R5', '', 'cisco', 'ciscosec', 'router')")
	curs.execute("INSERT OR REPLACE INTO tbDevice VALUES('192.168.122.106', 23, 'R6', '', 'cisco', 'ciscosec', 'router')")
	curs.execute("INSERT OR REPLACE INTO tbDevice VALUES('192.168.122.107', 23, 'R7', '', 'cisco', 'ciscosec', 'router')")
	curs.execute("INSERT OR REPLACE INTO tbDevice VALUES('192.168.122.108', 23, 'R8', '', 'cisco', 'ciscosec', 'router')")
	curs.execute("INSERT OR REPLACE INTO tbDevice VALUES('192.168.122.109', 23, 'R9', '', 'cisco', 'ciscosec', 'router')")
	curs.execute("INSERT OR REPLACE INTO tbDevice VALUES('192.168.122.110', 23, 'R10', '', 'cisco', 'ciscosec', 'router')")
	conn.commit()

#input data into table
def update_data():	
	ip = input("IPv4 Address = ")
	tcp = input("Telnet Port (default:23) = ")
	if tcp=='':
		tcp=23

	hn = input("Hostname = ").upper()
	uid = input("Login Username = ").lower()
	pwd = input("Login Password = ")
	sec = input("Secret Password = ")
	dt = input("Device Type (Router/Switch) = ").lower()	
	
	print("\n")
	print("""This device information will be added into database:
Hostname: %s
IP address: %s (tcp: %s)
Username: %s
Password: %s
Secret Password: %s
Device Type: %s\n""" %(hn, ip, tcp, uid, pwd, sec, dt))

	confirmation = input("Do you want to continue? (yes/no): ")
	
	if confirmation.lower() == "yes":
		curs.execute("INSERT OR REPLACE INTO tbDevice(ip_addr, telnet_port, hostname, username, password, secret, device_type) \
		VALUES(?,?,?,?,?,?,?)", (ip, int(tcp), hn, uid, pwd, sec, dt))
		conn.commit()
	else:
		sys.exit(0)
		
	#terminate database session
	curs.close()
	conn.close()

#read data from the table
def read_data():
	#curs.execute("SELECT * FROM tbDevice WHERE device_type='router' AND device_type='switch'")
	curs.execute("SELECT * FROM tbDevice")
	list_device = curs.fetchall()

	#Print Data Full Table
	#print(list_device)
	#print("\n")
	
	print("%s	\t%s	\t%s\t%s\t%s"%("IP ADDRESS", "PORT", "HOSTNAME", "PASSWORD", "TYPE"))
	for row in list_device:
		print("%s	\t%s	\t%s	\t%s	\t%s"%(row[0],row[1],row[2],row[4],row[6]))
	
#delete data from the table
def delete_data():
	curs.execute("SELECT * FROM tbDevice")
	list_data = curs.fetchall()
	
	print("Delete based on input type below:")
	print("1) IP Address")
	print("2) Hostname")
	print("3) Device Type")
	
	inp_type = int(input("Enter your number between 1 to 3 >> "))
	inp_val = str(input("Enter your value >> "))
	
	try:
		if inp_type==1:
			curs.execute("DELETE FROM tbDevice WHERE ip_addr='%s'" %(inp_val))
			conn.commit()
		elif inp_type==2:
			curs.execute("DELETE FROM tbDevice WHERE hostname='%s'" %(inp_val))
			conn.commit()
		elif inp_type==3:
			curs.execute("DELETE FROM tbDevice WHERE device_type='%s'" %(inp_val))
			conn.commit()
		else:
			print("Option is not available!")

	except ValueError:
		print("Oops! Sorry, your input is not valid")

#push configuration into the devices
def push_config():
	curs.execute("SELECT * FROM tbDevice")
	list_device = curs.fetchall()
	
	folder_location = filedialog.askdirectory()
	
	startTime = datetime.now()
	for devices in list_device:
		cisco_ios = {'device_type':'cisco_ios_telnet', 'ip':devices[0], 'username':devices[3], 'password':devices[4], 'secret':devices[5]}
		#cisco_ios = {'device_type':'cisco_ios_telnet', 'ip':devices[0], 'password':devices[4]}
		dev_conn = ConnectHandler(**cisco_ios)
		dev_conn.enable()
		#dev_conn.send_command("hostname "+devices[2])
		dev_conn.send_config_from_file(folder_location+"/"+devices[2]+".txt")
		#print(file_cfg+" --> Done")

	endTime = datetime.now()
	total_time = endTime - startTime
	print("\nEstimated Finish Time: %s" %(total_time))


#Initial Main Page
print("\nWelcome to INE CCIE Lab Initial Configurator")
print("Coded by: rpoernama <rakhmadian_purnama@yahoo.com>")
print("Version : 0.0 (Beta-release)")
print("--------------------------------------------\n")
print("""Please select your option:
1) Update Information
2) Read Information
3) Delete Information
4) Configuration Trigger
5) Reset Database
6) Exit System""")


initial_table()
opt_usr = str(input("Option selected: "))

if opt_usr == "1":
	update_data()

elif opt_usr == "2":
	read_data()

elif opt_usr == "3":
	delete_data()

elif opt_usr == "4":
	push_config()

elif opt_usr == "5":
	reset_db()
	
else:
	print("System Exit!")
	
#terminate database session
curs.close()
conn.close()
sys.exit(0)
