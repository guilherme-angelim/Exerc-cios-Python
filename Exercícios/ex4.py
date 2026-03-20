custo_veiculo = float(input("Digite o custo total: "))
print("Valor do custo do veículo: R$", custo_veiculo)
valor_imposto = custo_veiculo*0.45
print("Valor de impostos: R$", valor_imposto)
print("Valor do custo do veículo com impostos aplicados: R$",valor_imposto + custo_veiculo)
print("O lucro gerado ao vendedor foi: R$",(valor_imposto + custo_veiculo) * 0.12)