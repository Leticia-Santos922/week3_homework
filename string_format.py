# string handling

text = ('cool')

print(text.capitalize())
print(text.upper())
print(text.title())
print('<' + text.center(12) + '>')
print('<' + text.ljust(12) + '>')
print('<' + text.rjust(12) + '>')
print('<' + text.zfill(12) + '>')


# LITERAL STRING INTERPOLATION:
# names = list of strings inside [] - indexed as 0,1,2,3
# third_member is a variable that is being assigned a string.
# F strings - embed a python expression inside string literals using {}
# This string is formatted using an f-string, which is indicated by the f before the opening "
# names[3] accesses the 3rd item in the names list (2 as 0-indexed), which is "Elvie"
# The result of this expression is a string saying "The 3rd member is Elvie
# This string is then stored in the variable third_member
names = ['Tom', 'Cally', 'Elvie', 'Alessia']
third_member = f"The 3rd member is {names[2]}"
print(third_member)

# Combining F strings with raw strings
drive = 'C'
dir = 'Windows'
path = fr"{drive}\{dir}"
print(path)

# F strings syntax in example below:
# variable = f"string {variable} string {function(variable)} string {variable(list)}"


suffix = ['st', 'nd', 'rd', 'th']
n = 0
second_member = f"{str(n + 1) + suffix[n]} of {len(names)} is {names[n]}"
print(second_member)
# n variable = what number the person is in the list
# second_member = variable assigned a string
# f-string: create a string (n+1) - a 0-indexed - and add the suffix in the n position
# e.g. 1 (0+1) + st (0th), 2 (1+1) + nd (1st) = 1st or 2nd
# of = a string
# len(names) = length of names list = 4
# is = a string
# names[n] = the name at position 'n' e.g. Tom at position 0


# SLICING A STRING
# strings are immutable
# slice by start and end+1 position (0-indexed)
text = "Nice counting there, Buddy"
print(len(text))
print(text[11:14])
print(text[-7:-1])
# print characters 11-->14 from LHS 0,1,2,3...
# print characters -7-->-1 (not incl -1) from RHS -1,-2,-3...
print(text[:11])
print(text[:-7])
print(text[-7:])
print(text[1:21:2])
# print up to 11 from LHS, print up to 7 from RHS, print last 7 from RHS, print alt characters in range 1-20

name = 'caroline'
print(name[::-1].upper())
# all characters are printed (::) in reverse (-1). Taking the method .upper --> characters converted to uppercase


# SPLIT AND JOIN STRINGS
line = 'Cally::is:rubbish:at.Python'
elems = line.split(':')

elems[0] = 'Lady Kilduff'
elems[3] = 'FANTASTIC'
line = ':'.join(elems)
print(line)
