import re
# !/usr/bin/python

# nested string
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# TODO: A line of hyphens the same length as the belgium string

# strings are immutable
# f-string

print("-------, {}".format(Belgium))
print(f'-------, {Belgium}')
print(f"{'-'*6},{Belgium}")

# TODO: A string with a comma separator replaced by colons

print(re.sub("[ ,]", ":", Belgium))
print(Belgium.replace(',', ':'))


# use join and split
# seperator = ':'.join(Belgium)
# print(seperator)

# TODO: Population of Belgium plus Brussels

# add the population value of string fourth and second
# slice the string
elements = Belgium.split(',')[:4]
print(elements)

second_element = int(elements[1])
fourth_element = int(elements[3])

adding_elements = second_element + fourth_element
print(f"The total population of Belgium and Brussels: {adding_elements}")
