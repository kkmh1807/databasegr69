from datetime import date
import sqlite3
import textwrap

# Denne filen oppfyller brukerhistorie 4 og 5.
def searchForCoffee():

    # Her opprettes tomme strenger for å muliggjøre gjenbruk av kode mellom
    # brukerhistorie 4 og 5.
    searchDescriptionSQLstring = ""
    searchCountrySQLstring = ""
    searchProsessingSQLstring = ""
    fromWhereSQLstring = ""

    # Kobler til databasen
    con = sqlite3.connect("kaffe.db")
    con.row_factory = sqlite3.Row
    cursor = con.cursor()

    print("Her kan du søke etter kaffe")

    # Denne delen av koden hører til brukerhistorie 4. Koden gjør det mulig å søke
    # etter nøkkelord i beskrivelser av kaffene av både brukere og brenneriene.
    print("     Ønsker du å søke etter nøkkelord i beskrivelser av kaffene?")
    if(input("y/n: ") == "y"):
        print("Her kan du søke etter ord som er blitt brukt til å beskrive kaffer av brukere eller brennerier.")
        searchWord = input("Ditt søk: ")
        searchDescriptionSQLstring = """and (K.beskrivelse like '%{}%' or kaffeID in
            (SELECT kaffeID
            FROM Kaffesmaking
            WHERE smaksnotater like '%{}%'))""".format(searchWord, searchWord)

    # Denne delen av koden hører til brukerhistorie 5. Koden gjør det mulig å søke
    # etter opprinnelseslandet til kaffene. Man kan legge til flere land i søket.
    print("     Ønsker du å søke etter opprinnelseslandet til kaffene?")
    countryBoolString = input("y/n: ")
    if(countryBoolString == "y"):
        print("""Her kan du søke etter landet kaffebønnene kommer fra.
        Dersom du ønsker å søke etter flere land, separer landene med komma.""")
        searchCountries = input("Ditt søk: ").split(",")
        if len(searchCountries) != 0:
            i = 0
            searchCountrySQLstring = """and ("""
            while i < len(searchCountries):
                if(i > 0):
                    searchCountrySQLstring += " or "
                searchCountrySQLstring += "KR.landsnavn = '{}'".format(searchCountries[i])
                i += 1
            searchCountrySQLstring += ")"

    # Denne delen av koden hører til brukerhistorie 5. Koden gjør det mulig å søke
    # etter foredlingsmetoder som ikke skal være brukt på kaffene.
    print("     Ønsker du å søke etter foredlingsmetoder som ikke skal være brukt på kaffene?")
    processingBoolString = input("y/n: ")
    if(processingBoolString == "y"):
        print("""Her kan du søke etter foredlingsmetoden til kaffen.""")
        searchProcessing = input("Ditt søk: ")
        searchProsessingSQLstring = """and F.navn not like '%{}%'""".format(searchProcessing)

    # Her bestemmes FROM og WHERE delen av SQL spørringen, basert på hvilke søkekriterier
    # brukeren tar i bruk. Man kunne ha brukt brukerhistore 5 sin FROM/WHERE del i både
    # spørringen til brukerhistore 5 og 4, men den ville ha brukt mer ressurser og tid.
    # Derfor bruker vi brukerhistore 4 sin FROM/WHERE del når brukeren kun gjennomfører
    # søking slik som i brukerhistorie 4.
    if (countryBoolString == "y" or processingBoolString == "y"):
        fromWhereSQLstring = """FROM Kaffe as K, KaffebønneParti as P, Foredlingsmetode as F, Kaffegård as KG, KaffeRegion as KR
        WHERE K.partiID = P.partiID and P.foredlingsID = F.foredlingsID  and P.gårdID = KG.gårdID and KG.regionID = KR.regionID"""
    else:
        fromWhereSQLstring = """FROM Kaffe as K, KaffebønneParti as P
                        WHERE K.partiID = P.partiID"""

    # Denne delen av koden hører til både brukerhistorie 4 og 5. Ettersom det var
    # noe overlappende logikk i de to brukerhistoriene, valgte vi å samle noe av det.
    # Noe av sql koden for å hente ut data er lik i brukerhistorie 4 og 5, og den
    # resterende sql koden som er unik for hver brukerhistore blir lagt til med
    # .format funksjonen.
    cursor.execute(
        """SELECT K.kaffenavn, K.kaffebrenneri, K.dato as brennedato
            {} {} {} {}"""
            .format(fromWhereSQLstring, searchProsessingSQLstring, searchCountrySQLstring, searchDescriptionSQLstring))
    coffeeList = cursor.fetchall()

    # Her sjekkes det om søket har levert et resultat tilbake, og det blir printet
    # et passende utprint.
    if(coffeeList == None or len(coffeeList) == 0):
        print("Fant ingen kaffe med ditt søk!")
        return
    else:
        print("Kaffer som oppfyller ditt søk:")

    for row in coffeeList:
        prefix = "  *  " # Prefix som skaper en fin punktliste
        preferredWidth = 70 # Bredden på utprintfeltet
        wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,
                                       subsequent_indent=' '*len(prefix)) # Fint utskriftformat
        print(wrapper.fill(
            "<<{coffeeName}>>(brent: {burnDate}) fra brenneriet {roastery}"
            .format(coffeeName=row['kaffenavn'], burnDate=row['brennedato'], roastery=row['kaffebrenneri'])))

    con.commit()
    con.close()


def main():
    searchForCoffee()


if __name__ == "__main__":
    main()
