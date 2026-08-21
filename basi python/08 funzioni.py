def greet_user(username):
    print(f"Hello, {username.title()}!")
greet_user('alice')

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet(animal_type='dog', pet_name='willie')#se si specificano i parametri con il nome, l'ordine non è importante

def get_formatted_name(first_name, last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)
musician=get_formatted_name('john','hooker','lee')
print(musician)

def build_person(first_name, last_name):
    person={'first': first_name, 'last': last_name}
    return person
musician=build_person('jimi','hendrix')
print(musician)

def greet_users(names):
    for name in names:
        msg=f"Hello, {name.title()}!"
        print(msg)

usernames=['alice', 'bob', 'charlie']
greet_users(usernames)
greet_users(usernames[:])#passa una copia della lista

def make_pizza(*toppings):#* indica che la funzione può accettare un numero variabile di argomenti
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):#** indica che la funzione può accettare un numero variabile di argomenti chiave-valore
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile=build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

#con import nome_modulo si importa un modulo e si può usare il nome del modulo per accedere alle funzioni al suo interno
#con from nome_modulo import nome_funzione si importa una funzione specifica da un modulo e si può usare direttamente il nome della funzione
#as permette di dare un alias a un modulo o a una funzione importata
#* import nome_modulo importa tutte le funzioni di un modulo, ma non è consigliato perché può creare conflitti di nomi
