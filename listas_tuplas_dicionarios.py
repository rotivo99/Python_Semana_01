#!/usr/bin/env python3

list = ['Abed',
        'Troy',
        'Annie',
        'Shirley',
        'Britta',
        'Jeff',
        'Señor Chang']

print(list)
print('')
print(list[1], 'and', list[0], 'in the morning!')
print(list[2], 'are you OK? Would you tell us that you\'re ok? There\'s a sign in the window, that he struck you, a cresciendo,', list[2] + '.')
print(list[5] + 'ie, you ain\'t gon\' make a pregnant woman run, will you?')
print('IT\'S', list[6].upper(), 'FOR YOU.')
print(list[4] + ', you always ruin guys for us.')

print('')

tuple = ('January',
         'February',
         'March',
         'April',
         'May',
         'June',
         'July',
         'August',
         'September',
         'October',
         'November',
         'December')

print(tuple)
print('')
print('Your lie in', tuple[3] + '.')
print('There', tuple[4].lower(), 'be some things we can change.')

print ('')

dictionary = {'TP53':'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC', 'BRCA1':'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'}

print(dictionary)
print('')
print('{:<35}'.format('The sequence for the TP53 gene is:'), dictionary['TP53'])
print('{:<35}'.format('The sequence for the BRCA1 gene is:'), dictionary['BRCA1'])

print('')
#Para saber a quais classes minhas variáveis pertencem.
print(type(tuple))
print(type(dictionary))
print(type(list))
