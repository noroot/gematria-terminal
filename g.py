#!/usr/bin/env python3

english_gematria = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':600,
    'k':10,
    'l':20,
    'm':30,
    'n':40,
    'o':50,
    'p':60,
    'q':70,
    'r':80,
    's':90,
    't':100,
    'u':200,
    'v':700,
    'w':900,
    'x':300,
    'y':400,
    'z':500
}

def get_word():
    word = input("Word").lower()
    word = word.replace("ä", "a")
    word = word.replace("ö", "o")
    word = word.replace("ü", "u")
    word = word.replace("ß", "s")
    return word


word = get_word()
gematrix = english_gematria

c = []

for w in word:
    print("\t", w, end='')

print("")
for w in word:
    for e in gematrix:
        if w == e:
            #print("\t", gematrix[e])
            #print("\t",e,"=", gematrix[e], end='')
            c.append(gematrix[e])

for i in c:
    print("\t", "--", end='')
print("")
for i in c:
    print("\t", i, end='')
print("")

print( "English Gematria sum:\n\t", sum(c) )
