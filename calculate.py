import sys

a = int(sys.argv[1])
b = int(sys.argv[3])
op = sys.argv[2]

if len(sys.argv) > 4:
    print("Error. Too much variables.")
elif op not in ["+", "-", "/", "*"]:
    print("Error. Supported operations: +, -, *, /. If you are using * op, please try to run the script is python calculate.py 2 '*' 3")
elif op == "/" and b == 0:
    print("Error, division by zero - restricted.")
elif op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a // b)
else:
    print("Error, something went wrong. Please, try again.")
