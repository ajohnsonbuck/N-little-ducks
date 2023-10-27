# -*- coding: utf-8 -*-
"""
N Little Ducks: A little fun with a popular children's song.

User inputs an arbitrary integer N greater than 2, and the program provides
the lyrics to the song "N little ducks."

With each new verse, one less duck is present, until all are gone.

Then, in the final verse, all the ducks miraculously return.

Created in 2021 by Alex Johnson-Buck

@author: aledb
"""

def printVerse(n,str):
    if(n>1):
        print(p.number_to_words(n)[0].upper()+p.number_to_words(n)[1:]+str[0])
    elif(n==1):
        print(p.number_to_words(n)[0].upper()+p.number_to_words(n)[1:]+str[1])    
    n = n-1
    if(n>1):
        print(str[2] + p.number_to_words(n) + str[3])
    elif(n==1):
        print(str[4])
    else:
        print(str[5])
    print("")

str = [" little ducks went swimming one day\nOver the hill and far away\nMother duck said, \"Quack quack quack quack\"",
       " little duck went swimming one day\nOver the hill and far away\nMother duck said, \"Quack quack quack quack\"",
       "But only ",
       " little ducks came back.",
       "But only one little duck came back.",
       "But no little ducks came back.",
       "Sad mother duck went out one day\nOver the hill and far away\nMother duck said, \"Quack quack quack quack\"",
       "And all the ",
       " ducks came swimming back!"]

ducks = int(input("Give me a number greater than 1:"))

while ducks < 2:
    ducks = int(input("Error: please enter a whole number greater than 1:"))
import inflect
p = inflect.engine()

print('\n' + p.number_to_words(ducks)[0].upper() + p.number_to_words(ducks)[1:] + ' Little Ducks: \n')
for n in range(ducks,0,-1):
    printVerse(n,str)
    
print(str[6])
print(str[7] + p.number_to_words(ducks) + str[8])
