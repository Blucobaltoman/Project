cars=["audi","bmw","fiat"]
for car in cars:
    if car=="bmw":
        print(car.upper())
    else:
        print(car.title())

eta1=17
eta2=18
if eta1>=15 and eta2>=15:
    print("entrambi hanno più di 15 anni")
else:
    print("almeno uno ha meno di 15 anni")

if eta1>=15 or eta2>=15:
    print("almeno uno ha più di 15 anni")
elif eta1<15 and eta2<15:
    print("entrambi hanno meno di 15 anni")
else:
    print("almeno uno ha meno di 15 anni")

condimenti=["ketchup","maionese","senape"]
if "ketchup" in condimenti:
    print("ketchup è presente")

game_active=True

for condimento in condimenti:
    print(f"Vorrei aggiungere {condimento} al mio panino")

if condimenti:#se la lista condimenti non è vuota
    for condimento in condimenti:
        print(f"Vorrei aggiungere {condimento} al mio panino")
else:#se la lista condimenti è vuota
    print("Non ci sono condimenti disponibili")

condimenti_disponibili=["ketchup","maionese","senape"]
condimenti_richiesti=["ketchup","maionese","senape","salsa bbq"]
for condimento in condimenti_richiesti:
    if condimento in condimenti_disponibili:
        print(f"Aggiungo {condimento} al panino")
    else:
        print(f"Mi dispiace, non abbiamo {condimento}")
print("Il tuo panino è pronto!")