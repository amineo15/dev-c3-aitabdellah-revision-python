def calculatrice():
    n1 = float(input("Quelle est le premier nombre? "))
    n2 = float(input("Quelle est le deuxieme nombre? "))
    operation = input("Quelle est la opération? ")
    if operation == "+":
        resultat = n1 + n2
        print(resultat)
    elif operation == "-":
        resultat = n1 - n2
        print(resultat)
    elif operation == "*" or operation == "x":
        resultat = n1 * n2
        print(resultat)
    elif operation == "/":
        if n2 == 0:
            print("Imopossible de diviser par 0")
        else : 
            resultat = n1 / n2
            print(resultat)
