print("Übung Nummer 3 Di 6. November 2018\n")

prosa = ["Feuerkelch, Der", "In einem fremden Land", "Iluminati", "Alpha Zentauri"]#, "Parfüm, Das"]
print ("Aufgabe2:\n")
print (prosa[0:4])
print ("Aufgabe3:\n")
print (prosa[0])
print ("Aufgabe4:\n")
print (prosa[3])
print ("Aufgabe5:\n")
print (prosa[-2:])
print ("Aufgabe6:\n")
print (sorted(prosa)[0:]) #help(sorted)
prosa.insert(2, "de Beauvoir")
print (sorted(prosa)[0:]) #help(sorted)
print (prosa[0:])
del prosa[2]
prosa.insert(2, "De Beauvoir")
print (sorted(prosa)[0:]) #help(sorted)
print ("1. Erzeugen Sie eine Kopie Ihrer Romanliste.")
print (prosa.count("Effi Briest")) # Ausgabe: 4
print (prosa.count("Iluminati"))
print (prosa.count("fremd"))
print ("Übung sortieren")
prosa_backup = prosa
print (sorted(prosa)[0:])
del prosa[-1]
print (sorted(prosa_backup))

#Schreibe String in liste

meineListe = []

meineListe.append(prosa[2]);
print (prosa[1]);
print (meineListe);
              
            



