import logIn
import kaffeSmaking

print("Heihei, velkommen til kaffedatabase")

# Bruker logges inn, epost returneres
email = logIn.login()

# Funksjon for å la bruker velge en handling


def chooseAction():
    print("""Velg neste handling:
            k - ny kaffesmaking
            s - se kaffesmakinger
            l - logg ut""")
    return input("Ditt valg: ")


# Bruker får velge handling
choice = chooseAction()

while(choice != "l"):
    if (choice == "k"):
        kaffeSmaking.nyKaffeSmaking(email)
    elif (choice == "s"):
        kaffeSmaking.seKaffeSmakinger()

    # Bruker får velge ny handling
    choice = chooseAction()
