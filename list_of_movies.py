import csv
import pandas as pd

movies = ["Parasite", "Green Book", "The Shape of Water", "Moonlight", "Spotlight", "Birdman",
"12 Years a Slave", "Argo", "The Artist", "The King's Speech", "The Hurt Locker", "Slumdog Millionaire",
"No Country for Old Men", "The Departed", "Crash", "Million Dollar Baby", "The Lord of the Rings: The Return of the King",
"Chicago", "A Beautiful Mind", "Gladiator", "American Beauty", "Shakespeare in Love", "Titanic",
"The English Patient", "Braveheart", "Forrest Gump", "Schindler’s List", "Unforgiven", "The Silence of the Lambs",
"Dances With Wolves", "Driving Miss Daisy"]

# Note: For all these questions you need to take the values out of the list.
# You can't just assign a string to the variable

# Reverse the movies list so that instead of from 2020 to 1990 it goes from 1990 to 2020
# Your code starts after this line
movies.reverse()

# Your code ends before this line

# Set the variable winner_1990 to the best picture winner in 1990
# Your code starts after this line
winner_1990 = movies[0]

# Your code ends before this line

# Set the variable winner_2000 to the best picture winner in 2000
# Your code starts after this line
winner_2000 = movies[10]
# Your code ends before this line

# Set the variable winners_2010s to the best picture winners from 2010 to 2019
# Your code starts after this line
winners_2010s = movies[20:30]
# Your code ends before this line

# Replace the winner in 1999 with the movie 'The Thin Red Line'
# Your code starts after this line
movies.pop(9)
movies.insert(9, 'The Thin Red Line')
# Your code ends before this line

# Assign the count of all the movies to the variable movie_count
# Your code starts after this line
movie_count = len(movies)
# Your code ends before this line

# Using the range function create a variable year that contains a list of numbers from 1990 to 2020
# Your code starts after this line

years = []
for i in range(1990,2021):
    years.insert(0, i)
years.reverse()
# Your code ends before this line

print("Winner 1990: " + str(winner_1990))
print("Winner 2000: " + str(winner_2000))
print("Winners 2010s: " + str(winners_2010s))
print("New Winner 1999: " + str(movies[9]))
print("Count of movies: " + str(movie_count))
print("Years: " + str(list(years)))