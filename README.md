Python Basic Programs – A collection of simple Python programs demonstrating arithmetic operations, series generation, and list processing.

Description
This repository contains Python programs designed to illustrate:
Functions and Classes: Basic Object-Oriented style programming where appropriate.
Loops and Conditional Statements
Working with Lists and Dictionaries (Map equivalent)
Exception Handling and input validation
Each program includes clear comments and examples so anyone can understand the flow of logic, even without prior experience.

Features
Perform arithmetic operations using a Calculator class.
Generate the first $x$ odd numbers.
Generate odd numbers up to a given number.
Count how many numbers in a list are divisible by numbers
Beginner-friendly, commented code.
Error handling for invalid operations (like division by zero).

Installation / Setup Instructions
Install Python
Download Python 3 from https://www.python.org/downloads/.
Install following your OS instructions (Windows/macOS/Linux).
Verify installation:
Bash
python --version
or sometimes:
python3 --version

Install an IDE (Optional)
VS Code with Python Extension Pack: https://code.visualstudio.com/
PyCharm Community Edition: https://www.jetbrains.com/pycharm/download/

Programs Included
Calculator Program (program_1.py)
Description: Performs basic arithmetic operations (addition, subtraction, multiplication, division) on two numbers using a Calculator class. Supports both word-based (add) and symbol-based (+) input.
Features:
Encapsulation with instance variables (_a, _b, _operation).
__init__ method (constructor) to initialize values.
calculate() method with if/elif structure to perform the chosen operation.
Handles division by zero (ZeroDivisionError) and invalid operations (ValueError).
How it Works:
The user inputs two numbers (a and b) and an operation. The program creates a Calculator object. The calculate() method performs the operation using conditional logic. The result is displayed, or an error is shown if the input is invalid.
Example Run:
Bash
Enter first number (a): 10
Enter second number (b): 5
Enter operation (add, subtract, multiply, divide or +, -, *, /): *
Result: 50.0

First X Odd Numbers (program_2.py)
Description: Generates and prints the first $x$ odd numbers, separated by commas.
Features:
Loops from 1 to $x$.
Calculates odd numbers using the formula $2*i - 1$.
Uses string manipulation to achieve proper comma-separated output.
How it Works:
User enters the number $x$. A loop iterates $x$ times. For each iteration, the corresponding odd number is calculated and printed, with commas separating all numbers.
Example Run:
Bash
Enter a number (x): 5
1, 3, 5, 7, 9

Odd Numbers up to a Given Number (program_3.py)
Description: Prints all odd numbers up to a given number $a$. If $a$ is even, the program reduces it by 1 to ensure the largest number printed is odd.
Features:
Conditional check (ternary operator equivalent) to adjust even input.
Uses formula $2*i - 1$ to generate odd numbers.
Proper comma-separated output.
How it Works:
User inputs a number $a$. The code checks if $a$ is even and, if so, adjusts the number of terms. It then loops up to the adjusted number, calculates the odd numbers, and prints them in sequence.
Example Run:
Bash
Enter a number (a): 8
1, 3, 5, 7

Count Multiples in Array (program_4.py)
Description: Counts how many numbers in a predefined list are divisible by numbers 1 through 9 and stores the results in a dictionary.
Features:
Loops through divisors 1–9 using range(1, 10).
Uses modulus operator % to check divisibility.
Stores counts in a dictionary (Python's equivalent of a Map).
How it Works:
A predefined list of numbers is iterated over. An outer loop iterates through divisors 1 to 9. An inner loop counts the multiples for the current divisor. The final count is stored in a dictionary where the divisor is the key and the count is the value.
Example Run:
Bash
{1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 3, 7: 0, 8: 2, 9: 2}

Usage
To run any of the programs, use the Python interpreter from your terminal:
Bash
python program_1.py
python program_2.py
python program_3.py
python program_4.py
