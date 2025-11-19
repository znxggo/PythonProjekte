#Aufgabe 4

x = "global"

def func():
    global x
    x = "verändert"

func()
print(x)  #Lösung: [verändert]