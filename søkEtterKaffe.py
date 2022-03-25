from datetime import date
import sqlite3
import textwrap

# Denne filen oppfyller brukerhistorie 4 og 5.
def søkEtterKaffe():

    # Her opprettes tomme strenger for å muliggjøre gjenbruk av kode mellom
    # brukerhistorie 4 og 5.
    searchDescriptionSQL = ""
    searchCountrySQL = ""
    searchProsessingSQL = ""

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
        searchDescriptionSQL = """and (K.beskrivelse like '%{}%' or kaffeID in
            (SELECT kaffeID
            FROM Kaffesmaking
            WHERE smaksnotater like '%{}%'))""".format(searchWord, searchWord)

    # Denne delen av koden hører til brukerhistorie 5. Koden gjør det mulig å søke
    # etter opprinnelseslandet til kaffene. Man kan legge til flere land i søket.
    print("     Ønsker du å søke etter opprinnelseslandet til kaffene?")
    if(input("y/n: ") == "y"):
        print("""Her kan du søke etter landet kaffebønnene kommer fra.
        Dersom du ønsker å søke etter flere land, separer landene med komma.""")
        searchCountries = input("Ditt søk: ").split(",")
        if len(searchCountries) != 0:
            i = 0
            searchCountrySQL = """and ("""
            while i < len(searchCountries):
                if(i > 0):
                    searchCountrySQL += " or "
                searchCountrySQL += "KR.landsnavn = '{}'".format(searchCountries[i])
                i += 1
            searchCountrySQL += ")"

    # Denne delen av koden hører til brukerhistorie 5. Koden gjør det mulig å søke
    # etter foredlingsmetoder som ikke skal være brukt på kaffene.
    print("     Ønsker du å søke etter foredlingsmetoder som ikke skal være brukt på kaffene?")
    if(input("y/n: ") == "y"):
        print("""Her kan du søke etter foredlingsmetoden til kaffen.""")
        searchProcessing = input("Ditt søk: ")
        searchProsessingSQL = """and F.navn not like '%{}%'""".format(searchProcessing)

    # Denne delen av koden hører til både brukerhistorie 4 og 5. Ettersom det var
    # mye overlappende logikk i de to brukerhistoriene, valgte vi å samle noe av det.
    # Noe av sql koden for å hente ut data er lik i brukerhistorie 4 og 5, og den
    # resterende sql koden som er unik for hver brukerhistore blir lagt til med
    # .format funksjonen.
    cursor.execute(
        """SELECT K.kaffenavn, K.kaffebrenneri, K.dato as brennedato
            FROM Kaffe as K, KaffebønneParti as P, Foredlingsmetode as F, Kaffegård as KG, KaffeRegion as KR
            WHERE K.partiID = P.partiID and P.foredlingsID = F.foredlingsID  and P.gårdID = KG.gårdID and KG.regionID = KR.regionID
            {} {} {}"""
            .format(searchProsessingSQL, searchCountrySQL, searchDescriptionSQL))
    coffeeList = cursor.fetchall()

    # Her sjekkes det om søket har levert et resultat tilbake, og det blir printet
    # et passende utprint.
    if(coffeeList == None or len(coffeeList) == 0):
        print("Fant ingen kaffe med ditt søk!")
        return
    else:
        print("Kaffer som oppfyller ditt søk:")

    for row in coffeeList:
        prefix = "  *  "
        preferredWidth = 70
        wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,
                                       subsequent_indent=' '*len(prefix))
        print(wrapper.fill(
            "<<{coffeeName}>>(brent: {burnDate}) fra brenneriet {roastery}"
            .format(coffeeName=row['kaffenavn'], burnDate=row['brennedato'], roastery=row['kaffebrenneri'])))

    con.commit()
    con.close()


def main():
    søkEtterKaffe()


if __name__ == "__main__":
    main()
