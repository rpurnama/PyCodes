import random

class Greetings:
	
	text = []
	idx = 0
		
	def pagi(self):
		self.text = ['Selamat pagi!',
					'Hello, good morning Sir. How are you today?',
					'Selamat pagi Pak, hope nice day for you.']
					
		idx = random.randint(0,len(self.text)-1)
		#print(self.text[idx])
		
	def siang(self):
		self.text = ['Selamat siang! Nice to see you.',
					'Hello, selamat siang! Bagaimana kabar Anda hari ini?']
					
		idx = random.randint(0,len(self.text)-1)
		print(self.text[idx])
	
	"""
	def sore(self):
		self.text = ['Hi Pak, Selamat sore!',
					'Hi, good noon. how\'s your day?',
					'Hallo, selamat siang.']
					
		idx = random.randint(0,len(self.text)-1)
		print(self.text[idx])
	
	def malam(self):
		self.text = ['Hi Pak, Selamat Siang!',
					'Hi, good noon. how\'s your day?',
					'Hallo, selamat siang.']
					
		idx = random.randint(0,len(self.text)-1)
		print(self.text[idx])
	"""
salam = Greetings()
#salam.pagi()
salam.siang()

		