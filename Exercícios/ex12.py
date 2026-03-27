menornota = 0
maiornota = 0
somanotas = 0
qtdnota = 0
I = 0
while I != -1:
    I = float(input("Digite sua nota: "))
    if I == -1: 
        print("A maior nota foi: ", maiornota)
        print("A menor nota foi: ", menornota)
        print("A média das notas é: ", somanotas/qtdnota)
        break
    qtdnota += 1
    somanotas = somanotas + I
    if I < menornota or menornota == 0:
        menornota = I
    if I > maiornota:
        maiornota = I