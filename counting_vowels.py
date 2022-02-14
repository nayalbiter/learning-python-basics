string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of light, it was the season of darkness, it was the spring of hope, it was the winter of despair."
count_vowels = 0
for character in string:
   if character == 'a' or character =='A' or character =='e' or character =='E' or character =='i' or character =='I' or character =='o' or character =='O' or character =='u' or character =='U':
       count_vowels += 1
print("the number of vowels is " + str(count_vowels))
