from calculator import Calculator

def main():
	to_calculate = input("Enter calculation  (e.g. 12-1+2*3/10): ")
	result = Calculator(to_calculate)
	print(result)

if __name__ == "__main__":
	main()
