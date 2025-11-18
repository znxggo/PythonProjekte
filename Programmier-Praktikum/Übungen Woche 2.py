#Aufgaben Woche 2

#Aufgabe 1

def to_binary(n: int) -> str:
    return bin(n)

print(to_binary(42))  #erwartet:0b101010

#Aufgabe 2

print(oct(255))
print(hex(255))

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

#Aufgabe 4

x = "global"

def func():
    global x
    x = "verändert"

func()
print(x)  #Lösung: [verändert]

#Aufgabe 5

#Mach ich zuhause