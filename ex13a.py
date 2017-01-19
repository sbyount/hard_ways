# from sys import argv

# unpack
# script, word = argv

# name = raw_input("Enter a word: ")

# print "Your new word is '%s'" % (word + name)

# Pig latin translator
word = raw_input("Enter a word: ")
# Get the first character
first_char = word[0]
# Get the rest of the word
root = word[1:]
# Concatenate and add "ay" to the end
pig_word = root + first_char + "ay"

print "\nYour new word is: %s" % pig_word
