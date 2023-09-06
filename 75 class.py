class Person:
	"""docstring for Person"""
	def __init__(self, name, lastname, age):
		super(Person, self).__init__()
		self.myname = name
		self.mylastname = lastname
		self.myage = age

	def year(self,age):
		birthyear = 2023- age
		self.birthyear = birthyear
		return birthyear


name= input('please enter your name: ')
lstname= input('please enter your lastname: ')
age= int(input('please enter your age: '))
pers1 = Person(name, lstname, age)
print(f'hello {pers1.myname} {pers1.mylastname}, your age is {pers1.myage} so you was born in {pers1.year(age)}')
