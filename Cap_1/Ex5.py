from decimal import Decimal

salarioFixo = Decimal(input("Digite o salario"))
valorDeVendas = Decimal(input("Digite o total do valor vendido"))

valorGanho = salarioFixo + valorDeVendas * Decimal(0.04)

print("O valor ganho pelo funcionario foi: ", valorGanho)