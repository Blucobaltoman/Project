class Dog:
    def __init__(self, name, age):#self obbligatorio
        self.name=name #ogni variabile con self. è accessibile in tutta la classe
        self.age=age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog=Dog('Willie',6) #creo un oggetto della classe Dog
print(f"My dog's name is {my_dog.name}.") #accedo alle variabili della classe tramite l'oggetto
my_dog.sit() #chiamo un metodo della classe tramite l'oggetto

class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car=Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #super() richiama il metodo della classe genitore, deve essere usato per inizializzare gli attributi della classe genitore
        self.battery=Battery() #creo un oggetto della classe Battery

    def describe_battery(self):
        self.battery.describe_battery() #chiamo il metodo della classe Battery tramite l'oggetto battery

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size=battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla=ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#per importare una classe da un altro file si usa la sintassi: from nome_file import nome_classe
#si può anche fare import nome_file e poi usare nome_file.nome_classe per accedere alla classe

#le librerie standard di python contengono molte classi già pronte all'uso, ad esempio la classe datetime per lavorare con date e orari
from random import randint #importo la funzione randint dalla libreria random
random_number=randint(1,10) #genero un numero casuale tra 1 e 10
print(random_number)
