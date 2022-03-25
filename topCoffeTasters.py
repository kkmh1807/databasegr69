from datetime import date
import sqlite3
import textwrap

from sympy import DenseNDimArray

# Denne filen oppfyller brukerhistorie 2.
# Funksjonen skriver ut en liste over hvilke brukere som
# har smakt flest unike kaffer så langt i år, sortert synkende

def topCoffeTasters():

    # Kobler til databasen
    con = sqlite3.connect("kaffe.db")
    con.row_factory = sqlite3.Row
    cursor = con.cursor()

    # Utfører SQL spørringen mot databasen
    cursor.execute(
        """SELECT Bruker.fornavn, Bruker.etternavn, Bruker.epost, count(DISTINCT Kaffesmaking.kaffeID) as antallKaffesmakinger
        FROM Bruker, Kaffesmaking
        WHERE Kaffesmaking.epost = Bruker.epost and Kaffesmaking.dato > '{lastYear}-12-31'
        GROUP BY Kaffesmaking.epost
        ORDER BY count(DISTINCT Kaffesmaking.kaffeID) DESC"""
        .format(lastYear=int(date.today().year)-1))
    coffeeList = cursor.fetchall()

    if(coffeeList == None or len(coffeeList) == 0):
        print("Det finnes ingen kaffesmakinger i år!")
        return

    # Resultatet printes ut med pen overskrift og fint format
    print("Toppliste over hvilke brukere som har smakt flest unike kaffer så langt i år, sortert synkende:")
    ind = 1
    for row in coffeeList:
        prefix = "Nr." + str(ind) + ": " # Prefix som viser hvilken plass brukeren kom på
        ind += 1
        preferredWidth = 70 # Bredden på utprintfeltet
        wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,
                                       subsequent_indent=' '*len(prefix)) # Fint utskriftformat
        print(wrapper.fill(
            "{firstName} {lastName}({email}) har smakt {numberOfCoffees} unike kaffer så langt i år."
            .format(firstName=row['fornavn'], lastName=row['etternavn'], email=row['epost'],
            numberOfCoffees=row['antallKaffesmakinger'])))

    con.commit()
    con.close()


def main():
    topCoffeTasters()


if __name__ == "__main__":
    main()
