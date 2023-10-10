first_number = int(input("Enter first number: "))
second_number =int(input("Enter second number: "))
symbol = input("Enter symbol: ")
if symbol == "+":
    print(first_number + second_number)
elif symbol == "-":
    print(first_number - second_number)
elif symbol == "*":
    print(first_number * second_number)
else:
    print(first_number / second_number)

