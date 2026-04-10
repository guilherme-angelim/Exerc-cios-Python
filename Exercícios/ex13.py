qtdUsuarios = 0 
qtdAdultos = 0
while qtdUsuarios != -1:
    nome = input("Digite o nome do usuário (ou 'encerrar' para sair): ")
    
    if nome == 'encerrar' or nome == 'Encerrar':
        break
    
    idade = int(input("Digita a idade do usuário: "))
    qtdUsuarios += 1
    if idade >= 18:
        qtdAdultos += 1
        
print("Quantidade de usuários: ", qtdUsuarios)
print("Quantidade de adultos: ", qtdAdultos)