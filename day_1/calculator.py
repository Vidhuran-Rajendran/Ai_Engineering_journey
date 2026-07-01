class calculator:
    
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
operation = input("enter the operation (add, subtract, multiply, divide): ")
input2 = int(input("enter the first number: "))
input3 = int(input("enter the second number: "))

print("The result is: ", end="")
calc = calculator()

if operation == "add":
    print(calc.add(input2, input3))
elif operation == "subtract":
    print(calc.subtract(input2, input3))
elif operation == "multiply":
    print(calc.multiply(input2, input3))
elif operation == "divide":
    print(calc.divide(input2, input3))