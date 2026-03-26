nota1 = float(input("Nota um: "))
nota2 = float(input("Nota dois: "))
nota3 = float(input("Nota três: "))
media = (nota1+nota2+nota3)/3

if media >=8:
    print("Média geral: A")
elif media >=5 and media<8:
    print ("Média geral: B")
else:
    print ("Média geral: C")