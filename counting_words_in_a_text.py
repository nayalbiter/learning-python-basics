text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way--in short, the period was so far like the present period that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace('--', ' ')

words = text.split(' ')

count = 0
for word in words:
  if( word [0] == "i"or word [0] ==  "I"):
      count = count + 1
print("Number of words  that start with ‘I’ or ‘i’: " + str(count))     