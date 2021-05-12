pyg = 'ay'
original = raw_input('Enter a word that you want translated into pig latin: ')
if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:]
    print "Your word becomes: " + new_word
    raw_input ('Press <enter> to exit')
else:
    print 'You did not input a word'
    raw_input ('Press <enter> to exit.')
