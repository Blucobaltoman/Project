biciclette=["bici1","bici2","bici3"]
print(biciclette[0])
print(biciclette[-1])#-2,-3...
biciclette.append("bici4")#aggiunge alla fine
biciclette.insert(0,"bici0")#aggiunge in posizione 0, tutto slitta di 1
del biciclette[0]#elimina elemento in posizione 0
popped_bicicletta=biciclette.pop()#elimina l'ultimo elemento e lo salva in una variabile
popped_bicicletta=biciclette.pop(0)#elimina elemento in posizione 0 e lo salva in una variabile
biciclette.remove("bici2")#elimina elemento con quel valore, se ci sono più elementi con quel valore elimina il primo

macchine=["fiat","audi","bmw"]
macchine.sort()#ordina alfabeticamente
macchine.sort(reverse=True)#ordina alfabeticamente al contrario
print(sorted(macchine))#ordina alfabeticamente senza modificare la lista originale
macchine.reverse()#inverte l'ordine della lista
lunghezza=len(macchine)#lunghezza della lista

maghi=["harry","hermione","ron"]
for mago in maghi:
    print(mago.title())

for value in range(1,6):#range(start,stop,step), numeri da 1 a 5
    print(value)
numero=list(range(1,6))#crea una lista con numeri da 1 a 5
numero2=list(range(1,6,2))#crea una lista con numeri da 1 a 5 con step di 2
print(numero)
print(numero2)
quadrati=[value**2 for value in range(1,6)]#crea una lista con i quadrati dei numeri da 1 a 5
print(quadrati)
print(quadrati[0:3])#stampa i primi 3 elementi della lista
for quadrato in quadrati[:3]:#stampa i primi 3 elementi della lista
    print(quadrato)

cibo=["pizza","pasta","gelato"]
cibo_amico=cibo[:]#copia della lista cibo, senza il simbolo [:] cibo_amico sarebbe un riferimento alla lista cibo e non una copia
#NON cibo=cibo_amico, perché così cibo_amico sarebbe un riferimento alla lista cibo e non una copia

dimensioni=(200,50)#tuple, non modificabile
dimensioni=(400,100)#modifica la variabile dimensioni, ma non la tuple originale
