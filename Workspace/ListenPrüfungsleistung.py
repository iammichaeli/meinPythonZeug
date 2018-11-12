# Erstellt: 2018-11-09 Michael Imhof

#Aufgabe 1: Legen Sie eine Liste aus fünf Städten an und geben Sie die Liste auf dem Bildschirm aus.
print ("Aufgabe 1: ");
myList = ["Rom", "Moskau", "Buenos Aires", "Wien", "Darmstadt"];
print (myList[:]); # : Weil nach der Liste und nicht deren Inhalt gefragt wurde.
#Aufgabe 2:    Geben Sie den Anfangsbuchstaben der ersten Stadt in der Liste und den letzten Buchstaben der letzen Stadt in der Liste aus.
print ("Aufgabe 2: ");
print (myList[0][0]);print (myList[-1][-1]) # :-)
#Aufgabe 3a: Lassen Sie IhrE BenutzerIn eine weitere Stadt eingeben, speichern Sie die in einer Variablen.
print ("Aufgabe 3: ")
myStringTemp = str(input ("Bitte geben Sie einen String ein. Dieser wird der Liste für Städtenamen hinzugefügt: "))
#Aufgabe 3b: Lassen Sie außerdem eine Position von 1 bis Länge der Liste eingeben.
myIntTemp = int((input ("Bitte geben sie die gewünschte Position nullbasiert an, an der die Stadt in der Liste eingefügt werden soll mit einem Integer ein: \nDie Liste hat derzeit eine Länge von " + str(len(myList)) + " Einträgen.")))
#Aufgabe 3c: Fügen Sie die neue Stadt an der entsprechenden Position in die Liste ein.
myList.insert(myIntTemp, myStringTemp)
#Aufgabe 3d: Geben Sie die entstandene Liste aus.
print ("Ok! Die Liste sieht jetzt so aus:\n" + str(myList[:]))
#Aufgabe 4:    Ihr Benutzer möge diesmal den Namen einer Stadt, die in der Liste steht, eingeben. Löschen Sie den entsprechenden Eintrag aus der Liste.
print ("Aufgabe 4: ")
del myList[myList.index(str(input("Bitte geben Sie einen Stadtnamen aus der Liste ein den sie löschen möchten:")))]
#Aufgabe 5:    Geben Sie die endgültige Liste sortiert aus.
print ("Aufgabe 5: ")
print ("Ok! Die Liste wurde alphabetisch sortiert und sieht jetzt so aus:\n" + str(sorted(myList)[:]))