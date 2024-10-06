from abc import ABC, abstractmethod

class Shape(ABC):
	@abstractmethod
	def calculate_area(self):
		pass
		
	@abstractmethod
	def calculate_perimeter(self):
		pass
		
		
class Rectangle(Shape):
	def __init__(self, length, width):
		self.length = length
		self.width = width
		
	def calculate_area(self):
		return self.length * self.width

	def calculate_perimeter(self):
		return 2 * self.length + 2 * self.width
		
class Square(Rectangle):
	def __init__(self, length):
		super().__init__(length, length)
		
class Circle:
	def __init__(self, radius):
		self.radius = radius

	def calculate_area(self):
		return 3.14 * self.radius * self.radius

	def calculate_perimeter(self):
		return 3.14 * 2 * self.radius

class Triangle:
	def __init__(self, length, height):
		self.length = length
		self.height = height

	def calculate_area(self):
		return 0.5 * self.length * self.height
		
class Calculator:
	def __init__(self, to_calculate):
		import re
		OPERATIONS = r"([-+/*])"
		s = re.split(OPERATIONS, to_calculate)
		while len(s) > 2:
			result = self.calculate(s[1], s[0], s[2])
			temp = s[3:]
			temp.insert(0, result)
			s = temp
		self.to_calculate = to_calculate
		self.result = result
		
	def getfloat(self, number):
		try:
			num = float(number)
		except ValueError:
			print("Invalid number, try again")
			exit()
		return num

	def calculate(self, operator, number1, number2):
		number1 = self.getfloat(number1)
		number2 = self.getfloat(number2)

		if operator == "+":
			return self.add2numbers(number1, number2)
		if operator == "-":
			return self.subtract2numbers(number1, number2)
		if operator == "*":
			return self.multiply2numbers(number1, number2)
		if operator == "/":
			return self.divide2numbers(number1, number2)
		return

	def add2numbers(self, number1, number2):
		return number1 + number2

	def subtract2numbers(self, number1, number2):
		return number1 - number2

	def multiply2numbers(self, number1, number2):
		return number1 * number2

	def divide2numbers(self, number1, number2):
		try:
			result = number1 // number2
		except ZeroDivisionError:
			print("Can't divide by Zero!")
			exit()
		return result


def main():
	user_calculation = input() # Example: 2*2/2+1
	c = Calculator(user_calculation)
	print(f"{c.to_calculate} = {c.result}")

if __name__ == "__main__":
	main()
