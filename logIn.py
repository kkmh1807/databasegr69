import sqlite3
# import re module

# re module provides support
# for regular expressions
import re


def login():

    print("Vennligst logg inn")

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = input("E-post: ")

    # pass the regular expression
    # and the string into the fullmatch() method
    while(not re.fullmatch(regex, email)):
        print("Ugyldig epost, prøv igjen")
        email = input("E-post: ")

    passord = input("Passord: ")

    con = sqlite3.connect("kaffe.db")

    cursor = con.cursor()

    data = cursor.execute("SELECT * FROM bruker WHERE epost = ?", (email,))
    row = cursor.fetchone()

    if(row == None):
        print("Du er ikke registrert. \n Registrer deg med ditt navn: ")
        fornavn = input("Fornavn: ")
        etternavn = input("Etternavn: ")
        script = 'INSERT INTO bruker (epost, passord, fornavn, etternavn) VALUES (?, ?, ?, ?)'
        cursor.execute(script, (email, passord, fornavn, etternavn))

    con.commit()

    con.close()

    return email
