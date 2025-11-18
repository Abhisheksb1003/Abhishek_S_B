import sys

class Calculator:
  
    def __init__(self, a, b, operation):
        self._a = a  
        self._b = b
        self._operation = operation

   
    def calculate(self):
        
        operation_lower = self._operation.lower()
        
        if operation_lower in ["add", "+"]:
            return self._a + self._b
        
        elif operation_lower in ["subtract", "-"]:
            return self._a - self._b
        
        elif operation_lower in ["multiply", "*"]:
            return self._a * self._b
        
        elif operation_lower in ["divide", "/"]:
            if self._b != 0:
                return self._a / self._b
            else:
                
                raise ZeroDivisionError("Division by zero is not allowed!")
        
        else:
        
            raise ValueError(f"Invalid operation: {self._operation}")


    def getA(self):
        return self._a


def main():
   
    try:
        a_input = input("Enter first number (a): ")
        a = float(a_input)
    except ValueError:
        print("Error: Invalid input for number a.")
        return 

    
    try:
        b_input = input("Enter second number (b): ")
        b = float(b_input)
    except ValueError:
        print("Error: Invalid input for number b.")
        return 
        
   
    operation = input("Enter operation (add, subtract, multiply, divide or +, -, *, /): ")

  
    calc = Calculator(a, b, operation)

   
    try:
        result = calc.calculate()
        print(f"Result: {result}")
    except (ZeroDivisionError, ValueError) as e:
    
        print(f"Error: {e}")
    except Exception as e:
      
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

