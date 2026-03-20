nome = input("Digite o nome do jogador: ")
salario = float(input("Digite o seu salário atual: R$"))
novo_salario = 0
print ("Nome do jogardor: ",nome,"\n")
if salario <= 1000:
    novo_salario = salario + (salario*0.20)
elif salario > 1000 and salario <=5000:
    novo_salario = salario + (salario*0.10)
else:
    novo_salario = salario + (salario*0.05)
print ("O seu novo salário será: ",novo_salario)