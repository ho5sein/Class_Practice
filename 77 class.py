class Car(object):
	"""docstring for Car"""
	def __init__(self, name, model, price, color):
		super(Car, self).__init__()
		self.name = name
		self.model = model
		self.price = price
		self.color = color
		self.status = False

	def start(self):
		if self.status:
			print(f'your {self.name} is started before')
		else:
			print(f'your {self.name} is strating')
			self.status = True

	def shutdown(self):
		if self.status:
			print(f'your {self.name} is shut-down')
			self.status = False
		else:
			print(f'The {self.name} didnt start')

car1= Car('benz', 2015, 5000, 'white')
car2= Car('pride',2023,2000, 'black')

print(car1.status )
print(car2.status )
car1.start()
car1.start()
car2.shutdown()
car1.shutdown()
print(car1.status )
print(car2.status )