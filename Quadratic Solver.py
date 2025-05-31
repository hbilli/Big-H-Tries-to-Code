digits = input('How many digits per solution part?\n')
def continuer(x):
    if x == "Y" or x == 'y':
        quadratic(input('a = '), input('b = '), input('c = '))
    else:
        print("Goodbye.")

def quadratic(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        minus = str(-b / (2 * a)) + '+' + str((abs(discriminant) ** (1 / 2)) / (2 * a)) + 'i'
        plus = str(-b / (2 * a)) + '-' + str(abs(discriminant) ** (1 / 2) / (2 * a)) + 'i'
        print("Solutions: " + minus + ", " + plus)
        continuer(input('Would you like to solve another quadratic? Y/N: '))
    else:
        minus = str((-b - ((b ** 2) - (4 * a * c)) ** (1 / 2)) / (2 * a))
        plus = str((-b + ((b ** 2) - (4 * a * c)) ** (1 / 2)) / (2 * a))
        print("Solutions: " + minus + ", " + plus)
        continuer(input('Would you like to solve another quadratic? Y/N: '))

quadratic(input('a = '), input('b = '), input('c = '))

# improvements
# streamline how digits are set up
# improve user experience with an interface of some kind?
