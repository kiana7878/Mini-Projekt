#Passwortprüfung

passwort = input("Geben sie bitte ihr Passwort ein:")
#Hier wird das Passwort eingegeben

if len(passwort) >= 8 and any(char.isdigit() for char in passwort):
#Jetzt wird geschaut ob sie die Kriterien erfüllt haben
    print("Sicher")
elif len(passwort) >= 8 and not any(char.isdigit() for char in passwort):
#Jetzt wird geschaut ob nur eine Zahl fehlt
    print("Es fehlt eine Zahl!")
elif not len(passwort) >= 8 and any(char.isdigit() for char in passwort):
#Jetzt wird geschaut ob die länge richtig ist
    print("Es ist zu kurz!")
else:
#Hier wird jetzt gesagt das sein Passwort ungültig ist
    print("Falsch")