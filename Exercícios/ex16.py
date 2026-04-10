def valorPagar (prod, pag):
    return prod*pag
produto = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade de produtos: "))

resultado = valorPagar(produto,quantidade)
print ("O valor total  a pagar é de: R$ {:.2f}".format(resultado))