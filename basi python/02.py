name="ada lovelace"
print(name.title())
#name.lower() utile to store data
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
#lettera f per mettere variabili dentro stringhe, f sta per format
print(full_name)
# \t per tab, \n per riga vuota
#per eliminare spazi vuoti agli estremi comandi .rstrip() .lstrip()
#per eliminare prefissi .removeprefix('cosarimuovere')
#costanti tutte maiuscole

nome="mario"
cognome="rossi"
universita="trento"
nome_completo=f"{nome.title()}{cognome.title()}"
messaggio=f"Ciao mi chiamo {nome_completo} e il mio obiettivo è studiare a {universita.upper()}"
print(messaggio)

anno_corrente=2026
anno_nascita=2008
eta=anno_corrente-anno_nascita
print(f"Nel {anno_corrente} compio {eta} anni")
