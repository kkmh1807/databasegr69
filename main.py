from bestBuy import bestBuy
from login import login
from newCoffeeTasting import newCoffeeTasting
from seeCoffeeTastings import seeCoffeeTastings
from topCoffeTasters import topCoffeTasters
from searchForCoffee import searchForCoffee

print("Heihei, velkommen til kaffedatabase")

# Bruker logges inn, epost returneres og tas vare på
email = login()

# Funksjon for å la bruker velge en handling
def chooseAction():
    print("""Velg neste handling:
            n - ny kaffesmaking
            k - se kaffesmakinger
            t - toppliste kaffesmakere i år
            b - toppliste beste kjøp
            s - søk etter kaffe
            l - logg ut""")
    return input("Ditt valg: ")


# Bruker får velge handling
choice = chooseAction()

# Dette er hovedprogrammet, som fortsetter å loope så lenge brukeren
# ikke skriver inn "l".
while(choice != "l"):
    if (choice == "n"):
        newCoffeeTasting(email)
    elif (choice == "k"):
        seeCoffeeTastings()
    elif (choice == "t"):
        topCoffeTasters()
    elif (choice == "b"):
        bestBuy()
    elif (choice == "s"):
        searchForCoffee()

    # Bruker får velge ny handling
    choice = chooseAction()
