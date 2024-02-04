# FASTER VERSION
song = "Dos oruguitas enamoradas Pasan sus noches y madrugadas Llenas de hambre Siguen andando y vegando un mundo Que cambia y sigue cambiando Navegando un mundo"

# create a variable lines which is the song split at the spaces to put each word on a new line
lines = song.split(' ')
# set the variables: 'indentation' starting at 0 and 'direction' (of indentation) -1 = RHS forward, 1 = LHS backwards
indentation = 0
direction = -1
# Loop through each word
# enumerate gives the index/ position (i) and the value (line) for each item in the 'lines' collection.
for i, line in enumerate(lines):
    # Print the word with the current indentation
    # Change indentation direction every third line
    if i % 3 == 0:
        direction *= -1  # Reverse the direction
    indentation += direction  # Update the indentation based on the current direction
    print(' ' * indentation + line)
