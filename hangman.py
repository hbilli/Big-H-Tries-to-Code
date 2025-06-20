import random

# words from https://en.wiktionary.org/wiki/Appendix:Basic_English_word_list
wordsString = "come get give go keep let make put seem take be do have say see send may will about across after against among at before between by down from in off on over through to under up with as for of till than a the all any every no other some such that this I he you who and because but or if though while how when where why again ever far forward here near now out still then there together well almost enough even little much not only quite so very tomorrow yesterday north south east west please yes account act addition adjustment advertisement agreement air amount amusement animal answer apparatus approval argument art attack attempt attention attraction authority back balance base behavior belief birth bit bite blood blow body brass bread breath brother building burn burst business butter canvas care cause chalk chance change cloth coal color comfort committee company comparison competition condition connection control cook copper copy cork cotton cough country cover crack credit crime crush cry current curve damage danger daughter day death debt decision degree design desire destruction detail development digestion direction discovery discussion disease disgust distance distribution division doubt drink driving dust earth edge education effect end error event example exchange existence expansion experience expert fact fall family father fear feeling fiction field fight fire flame flight flower fold food force form friend front fruit glass gold government grain grass grip group growth guide harbor harmony hate hearing heat help history hole hope hour humor ice idea impulse increase industry ink insect instrument insurance interest invention iron jelly join journey judge jump kick kiss knowledge land language laugh law lead learning leather letter level lift light limit linen liquid list look loss love machine man manager mark market mass meal measure meat meeting memory metal middle milk mind mine minute mist money month morning mother motion mountain move music name nation need news night noise note number observation offer oil operation opinion order organization ornament owner page pain paint paper part paste payment peace person place plant play pleasure point poison polish porter position powder power price print process produce profit property prose protest pull punishment purpose push quality question rain range rate ray reaction reading reason record regret relation religion representative request respect rest reward rhythm rice river road roll room rub rule run salt sand scale science sea seat secretary selection self sense servant sex shade shake shame shock side sign silk silver sister size sky sleep slip slope smash smell smile smoke sneeze snow soap society son song sort sound soup space stage start statement steam steel step stitch stone stop story stretch structure substance sugar suggestion summer support surprise swim system talk taste tax teaching tendency test theory thing thought thunder time tin top touch trade transport trick trouble turn twist unit use value verse vessel view voice walk war wash waste water wave wax way weather week weight wind wine winter woman wood wool word work wound writing year angle ant apple arch arm army baby bag ball band basin basket bath bed bee bell berry bird blade board boat bone book boot bottle box boy brain brake branch brick bridge brush bucket bulb button cake camera card cart carriage cat chain cheese chest chin church circle clock cloud coat collar comb cord cow cup curtain cushion dog door drain drawer dress drop ear egg engine eye face farm feather finger fish flag floor fly foot fork fowl frame garden girl glove goat gun hair hammer hand hat head heart hook horn horse hospital house island jewel kettle key knee knife knot leaf leg library line lip lock map match monkey moon mouth muscle nail neck needle nerve net nose nut office orange oven parcel pen pencil picture pig pin pipe plane plate plough pocket pot potato prison pump rail rat receipt ring rod roof root sail school scissors screw seed sheep shelf ship shirt shoe skin skirt snake sock spade sponge spoon spring square stamp star station stem stick stocking stomach store street sun table tail thread throat thumb ticket toe tongue tooth town train tray tree trousers umbrella wall watch wheel whip whistle window wing wire worm able acid angry automatic beautiful black boiling bright broken brown cheap chemical chief clean clear common complex conscious cut deep dependent early elastic electric equal fat fertile first fixed flat free frequent full general good great grey hanging happy hard healthy high hollow important kind like living long male married material medical military natural necessary new normal open parallel past physical political poor possible present private probable quick quiet ready red regular responsible right round same second separate serious sharp smooth sticky stiff straight strong sudden sweet tall thick tight tired true violent waiting warm wet wide wise yellow young awake bad bent bitter blue certain cold complete cruel dark dead dear delicate different dirty dry false feeble female foolish future green ill last late left loose loud low mixed narrow old opposite public rough sad safe secret short shut simple slow small soft solid special strange thin white wrong"
wordsList = wordsString.upper().split()

def continuer(x):
    if x.lower() == "y" or x.lower() == 'yes' or x.lower() == 'continue':
        game()
    else:
        print("Goodbye.")

def stickman(l):
    if l >= 6:
        print('      _-----|')
        print('    /^ ^\   |')
        print('    \ _ /   |')
        print('     /|\    |')
        print('    / | \   |')
        print('     / \    |')
        print('    /   \   |')
        print('____________|')
    elif l == 5:
        print('      _-----|')
        print('    /^ ^\   |')
        print('    \ _ /   |')
        print('     /|\    |')
        print('    / | \   |')
        print('     /      |')
        print('    /       |')
        print('____________|')
    elif l == 4:
        print('      _-----|')
        print('    /^ ^\   |')
        print('    \ _ /   |')
        print('     /|\    |')
        print('    / | \   |')
        print('            |')
        print('            |')
        print('____________|')
    elif l == 3:
        print('      _-----|')
        print('    /^ ^\   |')
        print('    \ _ /   |')
        print('     /|     |')
        print('    / |     |')
        print('            |')
        print('            |')
        print('____________|')
    elif l == 2:
        print('      _-----|')
        print('    /^ ^\   |')
        print('    \ _ /   |')
        print('      |     |')
        print('      |     |')
        print('            |')
        print('            |')
        print('____________|')
    elif l == 1:
        print('      _-----|')
        print('    /^ ^\   |')
        print('    \ _ /   |')
        print('            |')
        print('            |')
        print('            |')
        print('            |')
        print('____________|')
    else:
        print('       -----|')
        print('   |    |   |')
        print('   |    |   |')
        print('    _---_   |')
        print('  /       \ |')
        print('            |')
        print(' TRY AGAIN! |')
        print('____________|')

print("Welcome to Hangman!\n")

#START GAME
def game():
    lives = input("Input the number of guesses you would desire.\n6 is recommended, but remember: you may want more lives if you choose a long word!\n\nGuesses/Lives: ")
    lives = int(lives)
    length = input("\nInput how many letters should be in your word.\nMake sure to choose less than 15!\n\nLength: ")

    possibleWords = []
    for wordNumber in range(len(wordsList)):
        if len(wordsList[wordNumber]) == int(length):
            possibleWords.append(wordsList[wordNumber])
    word = possibleWords[random.randint(0, len(possibleWords)-1)]

    print("Let's go!")

    guesses = ""
    wordExpanded = list(word)
    gameWord = ['_'] * int(length)
    while lives > 0:
        stickman(lives)
        print("Letters guessed: " + guesses)
        print("Lives remaining: " + str(lives))
        print("Player word: " + ''.join(gameWord))
        guess = input("Guess a letter!\nGuess: ").upper()
        guesses += guess + ', '
        if guess in wordExpanded:
            indices = ([pos for pos, char in enumerate(word) if char == guess])
            for o in indices:
                gameWord[o] = guess
            print("The letter " + guess + " was in the word!")
            if not('_' in gameWord):
                print("Congratulations! You guessed the word!")
                continuer(input("Would you like to play again?\nY/N or continue: "))
                break
        else:
            lives -= 1
            print("The letter " + guess + " is not in the word!\n")
    print("Game over!")
    print("The word was: " + str(word) + ".")
    continuer(input("Would you like to play again? Y/N or 'continue'.\n"))
game()

# improvements:
# prevent inputs for lives, length, guesses, and continuer that cause errors or don't make sense (e.g. negatives or str for int)
# provide for word 'difficulties' by importing different word lists
# stop guesses from accumulating additional letters that have already been guessed. also: alphabeticalize
# have print of letter is/isn't in word occur AFTER stickman
# improve user-friendliness e.g. w/ a modern interface
