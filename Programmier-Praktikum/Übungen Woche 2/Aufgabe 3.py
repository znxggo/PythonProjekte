#Aufgabe 3

global x
x= "global"

def func():
    x = "lokal"
    print("In func:", x)

func()
print("Außerhalb:", x)

    #Fragestellung: Was gibt das Programm aus? Erkläre kurz warum.

    #Antwort:
    #Die Funktion func() gibt [In func: lokal] aus
    #print("Außerhalb:", x) gibt [Außerhalb: global] aus