from decimal import Decimal

preco1 = Decimal(input("Digite o preço do produto: "))

novoPreoc = preco1 * Decimal(0.9)

print("O novo preço é: ", novoPreoc)