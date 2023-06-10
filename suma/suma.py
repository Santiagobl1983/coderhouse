import sys

def suma(num1, num2):
    return num1 + num2

if len(sys.argv) == 3:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(suma(num1, num2))
else:
    print("Error, esperaba 2 argumentos")

    