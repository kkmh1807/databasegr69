import sqlite3
import re

# Denne funksjonen er en hjelpefunksjon for å sikre at det er
# en innlogget bruker som utfører handlinger i applikasjonen.
# Det er ikke en bra måte å logge inn på, men tilstrekkelig for
# formålet, altså å ha en gyldig bruker med epost i databasen.
def login():

    print("Vennligst logg inn")

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = input("E-post: ")

    # Sjekker om epost passer formatet med fullmatch() funksjonen
    # Dersom den ikke passer formatet må bruker skrive inn på nytt
    while(not re.fullmatch(regex, email)):
        print("Ugyldig epost, prøv igjen")
        email = input("E-post: ")

    passord = input("Passord: ")

    # Kobler til databasen
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()

    # Utfører SQL spørringen mot databasen
    data = cursor.execute("SELECT * FROM bruker WHERE epost = ?", (email,))
    row = cursor.fetchone()

    # Dersom det ikke er noe resultat fra spørringen, finnes det ikke en
    # bruker med denne eposten, og det må da opprettes en bruker.
    if(row == None):
        print("Du er ikke registrert. \n Registrer deg med ditt navn: ")
        fornavn = input("Fornavn: ")
        etternavn = input("Etternavn: ")
        script = 'INSERT INTO bruker (epost, passord, fornavn, etternavn) VALUES (?, ?, ?, ?)'
        cursor.execute(script, (email, passord, fornavn, etternavn))

    con.commit()
    con.close()

    return email
