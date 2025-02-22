from decimal import Decimal

peso = Decimal(input("Digite um peso em KG"))
pesoEngordar = peso * Decimal(1.15)
pesoEmagrecer = peso * Decimal(0.8)

print(f'O novo peso se a pessoa engordar 15% é {pesoEngordar:.2f}')
print(f'O novo peso se a pessoa emagrecer 20% é {pesoEmagrecer:.2f}')