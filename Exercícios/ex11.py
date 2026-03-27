nome = (input("Digite o seu nome: "))
senhaadm = 12345678

senha = int(input("Digite a sua senha: "))
I = 1
while I <= 3:
    if senha == senhaadm:
        print("Acesso permitido")
        break
    else:
        if I<3:
            I = I+1
            senha = int(input("Digite a sua senha novamente: "))
        else:
            print("Acesso negado")
            break