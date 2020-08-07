from Person import Person
from Course import Course
class Professor(Person):

	def __init__(self, first_name, last_name, date_of_birth, gender, phone, address, salary):
		super().__init__(self, first_name, last_name, date_of_birth, gender, phone, address)
		self.salary = salary
		self.courses = []
		self.got_raise = False

	def check_raise(self):
		if len(self.courses) >= 4 and not self.got_raise:
			self.salary += 20000
			self.got_raise = True

	def add_couse(self, course):
		if not isinstance(course, Course):
			raise Error("Invaild Course")
		self.courses.append(course)
