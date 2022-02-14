print("What is the temperature in Celsius?: ")
number_string = input()
number_number = int(number_string)
result_number = (number_number * 9/5) + 32
result_string = str(result_number)
print("The temperature in Fahrenheit is: " + result_string + "!")