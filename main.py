import logIn
import kaffeSmaking

print("Heihei, velkommen til kaffedatabase")

# Bruker logges inn, epost returneres
email = logIn.login()

print("""Velg neste handling:
        k - ny kaffesmaking
        l - logg ut""")
choice = input("Ditt valg: ")

while(choice != "l"):
    if (choice == "k"):
        kaffeSmaking.nyKaffeSmaking(email)

    # Bruker får velge ny handling
    print("""Velg neste handling:
        k - ny kaffesmaking
        l - logg ut
            """)
    choice = input("Ditt valg: ")
