class Address:

	def __init__(self, street, zipcode, state, city, country):
		self.street = street
		self.zipcode = zipcode
		self.state = state
		self.city = city
		self.country = country

	def get_street(self):
		return self.street

	def get_zipcode(self):
		return self.zipcode
		
	def get_state(self):
		return self.state

	def get_city(self):
		return self.city

	def get_country(self):
		return self.country