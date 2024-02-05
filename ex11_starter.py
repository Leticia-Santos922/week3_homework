# CALLY

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# TODO: STEP 1
# Add a line of hyphens the same length as the Belgium string:
# Print( the string 'hyphen' multiplied by the length of the variable 'Belgium')
# Print the variable Belgium to confirm the hyphen string is the correct length
# Do the same but using f-string
print('-' * len(Belgium))
print(Belgium)


# F-STRING: literal string format where expressions '-' hyphen is multiplied * to length of Belgium(var)
# print function stringifies the result
# len = length variable returns the number of characters in the string (argument) in the variable Belgium (parameter)
# \n new line to show the Belgium variable below by inputting it as expression in braces
print(f"{'-' * len(Belgium)}\n{Belgium}")



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
# string replace method replaces specified string characters and phrases
# string.replace(oldvalue, newvalue, count)
# replaces the old value ',' in the Belgium var assigned string with new value ':'
print(Belgium.replace(',', ':'))
# another string method - find a character or word in the string and identify its starting position - ADD





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
# string literal format with f-string total population
# embedded in braces: expression calculates the total population by adding the values at string position 1 and 3
print(f"Total population is {int(words[1]) + int(words[3])}")


# # LETICIA
#
import re
# # !/usr/bin/python
#
# # A full string with objects, the commas are string values
# # the comma does not mean that the items are one string
# Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
#
# # To keep but not use
# # PART 1: A line of hyphens the same length as the belgium string
# # print manually inputted hyphens of 7, the same characters of word Belgium
# # the braces and hyphen are the values to be plugged into the function
# # Belgium is the nested argument which is being plugged in the format function
# # prints hyphen at the beginning
# # print("-------, {}".format(Belgium))
# # used literal string format through f-string and embedded Belgium expression in the braces
# # print(f'-------, {Belgium}')
# # print(f"{'-'*6},{Belgium}")



# PART 2: A string with a comma separator replaced by colons

# sub function replaces matching substrings with a new string for all occurrences, or a specified number
# a pattern is a regular expression which includes string, character class code and symbols
# re regular expression syntax - specifies a set of string that matches
print(re.sub(",", ":", Belgium))

# string replace method replaces specified string characters and phrases
# string.replace(oldvalue, newvalue, count)
# replaces the old value ',' in the Belgium var assigned string with new value ':'
print(Belgium.replace(',', ':'))

# TODO: Alternative

# # use join and split
# # seperator = ':'.join(Belgium)
# # print(seperator)


# PART 3: Population of Belgium plus Brussels

# add the population value of string fourth and second
# slice the string to include the first four strings

# split function breaks string to seperate at , to make them elements
# split the string to only include first four elements to print at console to understand what strings answer assigned
elements = Belgium.split(',')[:4]
print(elements)

# fourth and second variables takes the first and third string
# int method turns them into numerical values from string elements
second_element = int(elements[1])
fourth_element = int(elements[3])

# added both elements as numerical value to have total population of Belgium and Brussels
adding_elements = second_element + fourth_element

# F STRING: String literal format the population
# embedded in braces the arithmetic solution of the elements above to show the total of the two element as int
print(f"The total population of Belgium and Brussels: {adding_elements}")

