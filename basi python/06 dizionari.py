alien_0={'color':"verde",'punteggio':5}
#un dizionario è una collezione di coppie chiave-valore, in questo caso la chiave è color e il valore è verde, la chiave è punteggio e il valore è 5
print(alien_0["color"])
print(alien_0["punteggio"])
alien_0["x_position"]=0
alien_0["y_position"]=25
print(alien_0)

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print(f"Posizione iniziale: {alien_0['x_position']}")
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
elif alien_0['speed']=='fast':
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment
print(f"Nuova posizione: {alien_0['x_position']}")
alien_0['speed']='fast'
del alien_0['speed']

linguaggi={
    'jen':' python',
    'sarah':' java',
    'edward':' c++',
    'phil':' python',
    }

point_value=alien_0.get('points','nessun punteggio assegnato')
#se la chiave points non esiste, restituisce il valore di default 'nessun punteggio assegnato'
print(point_value)

for key,value in alien_0.items():
    print(f"Chiave: {key}")
    print(f"Valore: {value}")

for name in linguaggi.keys():
    print(name.title())

for name in sorted(linguaggi.keys()):#alfabetico
    print(name.title())

for name in linguaggi.values():
    print(name.title())

for name in set(linguaggi.values()):#valori unici, set è una collezione non ordinata di elementi unici
    print(name.title())

alien_0={'color':"verde",'punteggio':5}
alien_1={'color':"giallo",'punteggio':10}
alien_2={'color':"rosso",'punteggio':15}
aliens=[alien_0,alien_1,alien_2]

aliens=[]
for alien_number in range(30):#range(30) genera numeri da 0 a 29, quindi 30 alieni
    new_alien={'color':'verde','punteggio':5,'speed':'slow'}
    aliens.append(new_alien)

pizza={
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

users={
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username,user_info in users.items():
    print(f"\nUsername: {username}")
    full_name=f"{user_info['first']} {user_info['last']}"
    location=user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")