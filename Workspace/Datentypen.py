# Das war die Übung zu Datentypen
x = 3 * 4 + 1
print(x * len("Python") < 5)

print(3/2)

print(type(3/2))

print(type ("Hallo " + "Welt"))

print(type(3/3))

print("\n Ho " * 3 + "\n Das ist ja witzig :-) \n")

#Fragen Sie den/die Benutzer_in nach dem Namen und grüßen Sie mit
#»Hallo Benutzername!« (oder einer Grußformel Ihrer Wahl)

UserName = input("Bitte Namen eingeben: ")

NumberoffChoise = 0
NumberoffChoise = int(input ("Hallo " + UserName + ", bitte gib einen Integer ein, Werte Größer 10 brechen das Programm ab: "))
#TODO: richtigne Datentyp abfangen!

while NumberoffChoise < 10:

    NumberoffChoise = int(input ("Bitte gib einen Integer ein:"))

    def f(pNumberoffChoise):
        return {
                1: "\n Eins - Langweilig gib mir mehr! ",
                2: "\n Zwei" * 2,
                3: "\n Drei" * 3  
                }.get(pNumberoffChoise, "Ich kann nur bis 3 zählen.\n")
                            
    print (f(NumberoffChoise) + "\n. \n..\n..."+ "\nnochmal?")

Ausgabe = "\n Programmende erreicht. - Machs Gut " + UserName + "!" * len(UserName) 
print(Ausgabe)
print ("-" * len(Ausgabe))



