#This code reduces playback speed of sentences, seperating every word with elipses.

# Prompt user for input
words = input( )

# Seperate words in the sentence
slow_down = words.split()

# Return words with elipses
print(*slow_down, sep='...')