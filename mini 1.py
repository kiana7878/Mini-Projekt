#Taschenrechner
anzahl = int(input("Wie viele Rechnungen wollen sie Ausführen:"))
#mit dieser Variable legt man fest wie viele Rechnungen Ausgeführt werden sollen

for i in range (0, anzahl):
#Mit dieser Funktion kann das Programm anzahl mal Ausgeführt werden
    ersteZ = int(input())
    operator = str(input())
    zweiteZ = int(input())
    #hier werden erstmals die Variablen festgelegt indem man sie nach einnander eingibt

    if operator == "+":
        print(ersteZ + zweiteZ)
        
    elif operator == "-":
        print(ersteZ - zweiteZ)
        
    elif operator == "*":
        print(ersteZ * zweiteZ)
        
    elif operator == "/":
        print(ersteZ / zweiteZ)
    #in dieser Funktion wird erst kontrolliert welchen wert der Operator hat und dann Berechnet

