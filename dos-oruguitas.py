# creating a caterpillar effect for the song 'Dos Oruguitas'
# The song lyrics
# create variable called song
# put each line of the song on a different line
# the lyrics are a string
# if you separate out lines - use the """ to ensure python knows it is all one string
song = """Dos oruguitas enamoradas Pasan sus noches y madrugadas Llenas de hambre Siguen andando y navegando un mundo Que cambia y sigue cambiando Navegando un mundo"""

# STEP 1
# Split the song into lines:
# use the newline character to do this (\n)
# lines have to be separated in the programme for Python to recognise this
# .split is the method that takes the parameter 'new line' and assigns it to the object 'song'
lines = song.split(' ')

# STEP 2
# Create some variables:
# indented_lines is currently an empty list that will store the modified lines with the correct indentation.
# indentation keeps track of how many spaces to add to the start of each line, starting at 0
# direction determines whether Python adds spaces (1) or removes spaces (-1) from the indentation.
indented_lines = []
indentation = 0
direction = -1  # 1 for adding space, -1 for removing space

# STEP 3:
# Process each line using string.format for indentation:
# For loop created
# Python loops through the collection ('lines' = the song in split lines)
# Within the loop:
# enumerate is a function that counts items in the collection within ()
# Here - enumerate gives the index/ position (i) and the value (line) for each item in the lines list.
for i, line in enumerate(lines):
    # create new variable = width
    # For each line, 'width' is how much space the line will take up, including the indentation.
    width = len(line) + indentation
    # Format gives you a chance to pass in items in placeholders within {}
    # The format string formats the given line (string) to be right-aligned (>) until 'width' is achieved
    # This adds spaces to the left of line until the total length is width.
    # this --> the variable formatted_line
    formatted_line = f"{line:>{width}}"
    # After formatting the line, it is added to the list (created above) indented_lines.
    # append is the method to add each formatted line to the list
    indented_lines.append(formatted_line)


# STEP 4:
    # Adjust indentation and direction:
    # % means divide LHS by RHS - i.e % index position of line (0,1,2..) by 3
    # If the line is divisible by 3 with 0 remaining (line 3,6,9 ...) (if i % 3 == 0), change the direction
    # Direction is changed by multiplying direction (either 1 or -1 by -1) outcome will either be 1 or -1
    if i % 3 == 0:
        direction *= -1
    # Adjust the indentation by adding direction (which could be -1 or 1) --> ind= ind+dir
    indentation += direction

# STEP 5
# Join the lines back into a single string:
# otherwise it will print as a list of strings with variable spaces in front of each word
# use the method join to connect each line ('\n') following the indented lines pattern created above
indented_song = '\n'.join(indented_lines)

# STEP 6:
# print the variable 'indented_song' created above:
# this should be a single string of 'indented_lines', where each line follows the indentation pattern set above
print(indented_song)
