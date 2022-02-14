# Define the function printHelloWorld that prints "Hello World!" in the console.

# Your code starts after this line
def printHelloWorld():
    print("Hello World!")
# Your code ends before this line


# Define the function printHelloName that takes a new and prints "Hello <name>!"

# Your code starts after this line
def printHelloName(name):
    print("Hello " + name + "!")
# Your code ends before this line


# Define the function add that takes two numbers and returns the sum of the two numbers

# Your code starts after this line
def add(a, b):
    print(a + b)

# Your code ends before this line


# Define the function countMultiples, that takes a number and returns the number of multiples
# of that number that exist between 0 and 100

# Your code starts after this line
def countMultiples(*numbers):
    pass
# Your code ends before this line

# Define the function countLetter, that takes a lower case letter and returns the number of ocurrences
# of the letter (both lower case and upper case) in this text

text = "Mr. and Mrs.  Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you'd expect to be involved in anything strange or mysterious, because they just didn't hold with such nonsense. Mr. Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbors. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere."

# Your code starts after this line
def countLetter():
    pass

# Your code ends before this line

printHelloWorld()
printHelloName('Marcelo')
print("10 + 15 = " + str(add(10, 15)))

for i in [5, 8, 9, 10]:
    print("Multiples of  " + str(i) + ": " + str(countMultiples(i)))

for c in ['a', 'e', 'p', 'q']:
    print("Ocurrences of " + c + ": " + str(countLetter(c)))