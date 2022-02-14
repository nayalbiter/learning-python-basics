print("the temperature in the USA  is calculate in degrees Fahrenheit, but what is the temperature in Celsius?")
print("type the temperature today in F")
number_string = input()
number_number = int(number_string)
result_number = (number_number - 32) * 5 / 9
result_string = str (result_number)
print ("the temperature today in C is = " + result_string + "!")
