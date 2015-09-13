class Employees(object):
	
	def __init__(self):
		self.id = ""
		self.name = ""
		self.jobs = ""
		self.email = ""
		self.age = 0
		self.__data = [
			('23AS', 'Mark', 'IT Department', 'mark@mail.com', 34),
			('26AD', 'Steve Larry', 'Programmer', 'stelarr@mail.com', 22),
			('19GH', 'Yanwar Solahudin', 'Senior Developer', 'yanzen@mail.com', 25),
			('87FT', 'Olla Merlin', 'Senior Designer', 'ollamerlin@mail.com', 25),
		]
	
	def get_all_employees(self):
		return self.__data
	
	def add(self, *args):
		if len(args) < 5:
			return False
		else:
			self.__data.append(args)
		return True
	
	
	
	
