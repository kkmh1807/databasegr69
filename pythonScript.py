import sqlite3

con = sqlite3.connect("kaffe.db")

cursor = con.cursor()

print("Heihei, velkommen til kaffedatabase")
print("Vennligst logg inn")
epost = input("E-post: ")
passord = input("Passord: ")


data = cursor.execute("SELECT * FROM bruker WHERE epost = ?", (epost,))
row = cursor.fetchone()

if(row == None):
    print("Du er ikke registrert. \n Registrer deg med ditt navn: ")
    fornavn = input("Fornavn: ")
    etternavn = input("Etternavn: ")
    script = 'INSERT INTO bruker (epost, passord, fornavn, etternavn) VALUES (?, ?, ?, ?)'
    cursor.execute(script, (epost, passord, fornavn, etternavn))
else:
    print("Skriv inn din kaffesmaking")

#Input fra brukerens side er brenneri, kaffenavn, poeng og smaksnotat.


#Her kommer utspørringene i guess?
# cursor.execute('''INSERT INTO bruker VALUES ('ola@nordmann.no', 'password1', 'Ola', 'Nordmann')''')
con.commit()

con.close()