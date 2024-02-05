import re
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'


# TODO STEP 1: Add a line of hyphens the same length as the Belgium string:

# Print( the string 'hyphen' multiplied by the length of the variable 'Belgium')
# Print the variable Belgium to confirm the hyphen string is the correct length
# Do the same but using f-string
print('-' * len(Belgium))
print(Belgium)
# F-STRING: literal string format where expressions '-' hyphen is multiplied * to length of Belgium(var)
# print function stringifies the result
# len = length variable returns the number of characters in the string (argument) in the variable Belgium (parameter)
# \n new line to show the Belgium variable below (to compare length to hyphens) by inputting it as expression in braces
print(f"{'-' * len(Belgium)}\n{Belgium}")

# # To keep but not use:
# # PART 1: A line of hyphens the same length as the belgium string
# # print manually inputted hyphens of 7, the same characters of word Belgium
# # the braces and hyphen are the values to be plugged into the function
# # Belgium is the nested argument which is being plugged in the format function
# # prints hyphen at the beginning
# # print("-------, {}".format(Belgium))
# # used literal string format through f-string and embedded Belgium expression in the braces
# # print(f'-------, {Belgium}')
# # print(f"{'-'*6},{Belgium}")


# TODO STEP 2: Replace the commas in the string 'Belgium' with colons:

# create a variable called words
# in this variable, the method '.split' splits the string Belgium at the commas
# Now each word in the string is treated separately
# create a new variable 'joined_words' and use the method 'join' each string back together with ':' between each one
words = Belgium.split(',')
joined_words = ':'.join(words)
print(joined_words)

# alternatively use the replace method (neater code)
# string replace method replaces specified string characters and phrases
# string.replace(oldvalue, newvalue, count)
# replaces the old value ',' in the Belgium var assigned string with new value ':'
print(Belgium.replace(',', ':'))

# Alternative string method - find a character or word in the string and identify its starting position - ADD
# sub function replaces matching substrings with a new string for all occurrences, or a specified number
# a pattern is a regular expression which includes string, character class code and symbols
# re regular expression syntax - specifies a set of string that matches
print(re.sub(",", ":", Belgium))


# TODO EXTRA
# .find method - finds the index of the string requested e.g. Europe starts at index 33 (0 indexed) from LHS
print(Belgium.find('Europe'))


# TODO STEP 3 - Add the population of Belgium to the population of Brussels:

# create 2 variables for the two population figures
# 'population_belgium' take the string in position 1 of the collection 'words'
# Convert that string to an integer and repeat for the string at position 3
# print the summation of the two integers:
population_belgium = int(words[1])
population_brussels = int(words[3])
print('Total population is ', population_brussels + population_belgium)

# Alternatively - neater using f string
# string literal format with f-string total population
# embedded in braces: expression calculates the total population by adding the values at string position 1 and 3
print(f"Total population is {int(words[1]) + int(words[3])}")

# Extra - Splitting and formatting lines:
# split function - just to visualise the first 4 strings:
# breaks string to separate at , to make them elements
# split the string to only include first four elements to print at console to understand what strings answer assigned
elements = Belgium.split(',')[:4]
print(elements)

elements = {'Belgium': 10445852,
            'Brussels': 737966}

for i, key in enumerate(elements.keys(),1):
    print("{:8d} {:<10s} {}".format(i, key, elements[key]))