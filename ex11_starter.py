Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# TODO STEP 1
# Add a line of hyphens the same length as the Belgium string:
# Print( the string 'hyphen' multiplied by the length of the variable 'Belgium')
# Print the variable Belgium to confirm the hyphen string is the correct length
# Do the same but using f-string
print('-' * len(Belgium))
print(Belgium)
# alternatively use f-strong
print(f"{':'* len(Belgium)}")


# TODO STEP 2
# Replace the commas in the string 'Belgium' with colons:
# create a variable called words
# in this variable, the method '.split' splits the string Belgium at the commas
# Now each word in the string is treated separately
# create a new variable 'joined_words' and use the method 'join' each string back together with ':' between each one
words = Belgium.split(',')
joined_words = ':'.join(words)
print(joined_words)
# alternatively use the replace method (neater code)
print(Belgium.replace(',', ':'))
# another string method - find a character or word in the string and identify its starting position

# TODO EXTRA
print(Belgium.find('Europe'))


# TODO STEP 3
# Add the population of Belgium to the population of Brussels
# create 2 variables for the two population figures
# 'population_belgium' take the string in position 1 of the collection 'words'
# Convert that string to an integer and repeat for the string at position 3
# print the summation of the two integers:

# population_belgium = int(words[1])
# population_brussels = int(words[3])
# print('Total population is ', population_brussels + population_belgium)
# Alternatively - neater using f string
print(f"Total population is {int(words[1]) + int(words[3])}")


