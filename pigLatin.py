print("Welcome to the Pig Latin translator!")

def continuer(x):
    if x == "Y" or x == 'y':
        pigLatin()
    else:
        print("Goodbye.")

def pigLatin():
    phrase = input("Enter phrase to translate into Pig Latin:\n").lower()
    phrase = phrase.lower()
    translation = ''
    for a in range(len(phrase.split())):
        word = phrase.split()[a]
        if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
             if word[len(word) - 1] == 'w' or "W":
                 word += 'ay'
                 translation += word + ' '

             else:
                 word += 'way'
                 translation += word + ' '
        else:
            if word[1] == 'a' or word[1] == 'e' or word[1] == 'i' or word[1] == 'o' or word[1] == 'u':
                word = word[1:] + word[0] + 'ay'
                translation += word + ' '
            else:
                word = word[2:] + word[0] + word[1] + 'ay'
                translation += word + ' '
    translationFinal = translation.capitalize()[:-1]
    print(translationFinal.center(len(translation) + 6, '-'))
    continuer(input("\nWould you like to translate an additional phrase?\nY/N: "))
pigLatin()

#improvements
#Give option to save case as inputed
#ensure that special characters aren't treated
#per usual, better user interface
#make wrapping starting consonants include > 2 letters (e.g. the word stray should be ay-stray, not ray-stay.)
#that said, 'official' pig latin rules are only concerned with first 2!
