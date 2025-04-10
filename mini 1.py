#Taschenrechner
print("Mit diesem Taschenrechner können sie +, -, +, /, % und Potenzen berechnen")
print("Geben sie bitte ja ein wenn sie gefragt werden weiter zu machen, wenn sie weitermachen wollen, sonst geben sie Nein ein.")
#kurze anleitung
weitermachen = str("Ja")
while not weitermachen == "Nein":
    print("Geben sie ihre Rechnung ein:)
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
    
    elif operator == "%":
        print(ersteZ % zweiteZ)
        
    elif operator == "potenz" or "Potenz":
        print(ersteZ ** zweiteZ)
    #in dieser Funktion wird erst kontrolliert welchen wert der Operator hat und dann Berechnet
    
    weitermachen = input("Wollen sie Weitermachen?:")
    #kontrollieren ob der nutzer weitermachen will
    

