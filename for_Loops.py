# Note: The answers to all this problems need to be calculated using for loops
# assigning the solution by hand or based on the expected will result in a 0 in the whole assignment

from math import sqrt

# Given the list l with the following numbers
l = [1, 5, 12, 4, 3, 6, 8, 10, 11, 3, 4, 5, 7, 1, 0, 10, 12, 15, 17]

# Add all the numbers in l that are smaller than 5
sum = 0
for i in l:
# Your code starts after this line
    if i < 5:
        sum = sum + i
# Your code ends before this line
print("Sum of smaller than 5: " + str(sum))

# Calculate the average of the numbers in l that are between 3 and 10 (not inclusive)
sum = 0
count = 0
for i in l:
# Your code starts after this line
    if i >3 and i <10:
        sum = sum + i
        count = count + 1
# Your code ends before this line
print("Average of between 3 and 10: " + str(round(sum/count,2)))

# Find the largest number in the list
max = 0
for i in l:
# Your code starts after this line
    if i > max:
        max = i
# Your code ends before this line
print("Largest: " + str(max))

# The population standard deviation is defined here:
# https://www.mathsisfun.com/data/standard-deviation.html
# Calculate the population standard deviation of the numbers in l

sum = 0
count = 0
for n in l:
# Your code starts after this line
    sum = sum + n
    count = count + 1
# Your code ends before this line
mean = sum/count
print("Mean: " + str(round(mean, 2)))

sum = 0
count = 0
for n in l:
# Your code starts after this line
    var = pow((n - mean), 2)
    sum = sum + var
    count = count + 1
# Your code ends before this line
std = sqrt(sum/count)
print("Standard Deviation: " + str(round(std, 2)))