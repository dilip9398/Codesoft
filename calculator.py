print("A Simple Calculator")
first_number = float(input("Enter the first number: "))
user_operator = input("Enter the operation, you want \n '+', '-', '*', '/', '**', '/' \n Note: '**' for squaring or power : ")

second_number = float(input("Enter the second number: "))

if user_operator == '+':
    sum = first_number + second_number
    print(sum)
elif user_operator == '-':
    sub = first_number - second_number
    print(sub)
elif user_operator == '*':
    multiplication = first_number * second_number
    print(multiplication)
elif user_operator == '**':
    power = first_number ** second_number
    print(power)
elif user_operator == '/':
    division = first_number / second_number
    print(division)
else:
    print("Invalid input!")
