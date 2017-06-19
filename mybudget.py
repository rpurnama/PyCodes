import sqlite3

print("*** Monthly Expense ***")

koneksi = sqlite3.connect("myfinc.db")
pointer = koneksi.cursor()

#Initiate Table
pointer.execute('''CREATE TABLE budget
				(date text,
				room real,
				electricity real,
				water real,
				internet real,
				other real,
				Total real);''')

def isiData():
	tanggal = input('Tanggal (dd/mm/yy): ')
	roomfee = eval(input('Fee Room in MYR (600): '))
	electfee = eval(input('Electricity bill in MYR: '))
	waterfee = eval(input('Water bill in MYR: '))
	wififee = eval(input('Internet Wifi bill in MYR: '))
	otherfee = eval(input('Other in MYR: '))
	
	totalfee = roomfee + electfee + waterfee + wififee + otherfee
	
	#expense = [(tanggal,roomfee,electfee,waterfee,wififee,otherfee,totalfee)]
	pointer.execute("INSERT INTO budget (date,room,electricity,water,internet,other,Total) \
					VALUES (?,?,?,?,?,?,?);",(tanggal,roomfee,electfee,waterfee,wififee,otherfee,totalfee))
	koneksi.commit()
	
isiData()
pointer.close()

