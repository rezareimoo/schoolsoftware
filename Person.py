from Address import Address
class Person:
	def __init__(self, first_name, last_name, date_of_birth, gender, phone, address):
		self.first_name = first_name
		self.last_name = last_name
		self.date_of_birth = date_of_birth
		self.gender = gender
		self.phone = phone
		self.addresses = []

		if isinstance (address, Address):
			self.addresses.append(address)
		elif isinstance(address, list):
			for entry in address:
				if not isinstance(entry, Address):
					raise Error("Invaild Address...")
			self.addresses = address
		else:
			raise Error("Invaild Address...")
	def add_address(self, address):
		if not isinstance(address, Address):
			raise Error("Invaild Address...")
			
		self.addresses.append(address)

	def get_first_name(self):
		return self.first_name

	def get_last_name(self):
		return self.last_name

	def get_age(self):
		return self.age

	def get_gender(self):
		return self.gender

	def get_phone(self):
		return self.phone
