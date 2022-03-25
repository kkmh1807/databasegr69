from besteKjøp import besteKjøp
import logIn
from kaffeSmaking import nyKaffeSmaking
from seeCoffeeTastings import seeCoffeeTastings
from topplisteKaffesmakinger import topplisteKaffesmakinger
from søkEtterKaffe import søkEtterKaffe

print("Heihei, velkommen til kaffedatabase")

# Bruker logges inn, epost returneres
email = logIn.login()

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

while(choice != "l"):
    if (choice == "n"):
        nyKaffeSmaking(email)
    elif (choice == "k"):
        seeCoffeeTastings()
    elif (choice == "t"):
        topplisteKaffesmakinger()
    elif (choice == "b"):
        besteKjøp()
    elif (choice == "s"):
        søkEtterKaffe()

    # Bruker får velge ny handling
    choice = chooseAction()
