altezza=int(input("Inserisci la tua altezza in cm: "))
print(f"La tua altezza è {altezza} cm")

uncorfirmed_users=['alice','brian','candace']
confirmed_users=[]

while uncorfirmed_users:
    current_user=uncorfirmed_users.pop()
    print(f"Verifico l'utente: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nGli utenti confermati sono:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses={}
polling_active=True
while polling_active:
    name=input("\nQual è il tuo nome? ")
    response=input("Qual è la tua città preferita? ")
    responses[name]=response #aggiunge la risposta al dizionario

    repeat=input("Vuoi far partecipare un'altra persona? (s/n) ")
    if repeat=='n':
        polling_active=False

print("\nRisultati del sondaggio:")
for name, response in responses.items():
    print(f"{name.title()}: {response}")