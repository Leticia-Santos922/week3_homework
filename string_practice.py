import textwrap


# TODO: Make text to a caterpillar
# 3 ''' or """ allows to create strings which span multiple lines
# \ removes the space at the top and the bottom of lyrics which was there automatically
# not indented as python assumes that the white space for indentation is part of the string
encanto_song = '''\
Dos oruguitas enamoradas,
Pasan sus noches y madrugadas,
llenas de hambre,
Siguen andando y navegando un mundo, 
Que cambia y sigue cambiando, 
Navegando un mundo, 
Que cambia y sigue cambiando.\
'''


# # TODO: Caterpillar
# indent_line = " "
#
# print(textwrap.indent(encanto_song, indent_line))
# # print(encanto_song.format(49))
#
#
# # TODO: string slicing - Lyrics in reverse
#
# # # reverse string slicing with negative index
# reversed_lyrics = encanto_song[::-1]
# print(reversed_lyrics)

# slicing first and last row
# start index and final
# first_row = encanto_song[25:-30]
# print(first_row)


# TODO: string.format (seems useful when placing strings)

txt = "We have {:<8} chickens."
print(txt.format(39))


# TODO f-string including split and join (create caterpillar)

# for each_line in encanto_song.split(','):

