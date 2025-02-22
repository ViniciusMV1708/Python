from decimal import Decimal

peso = Decimal(input("Digite um peso em KG"))
pesoGramas = peso * Decimal(1000)

print(f'O peso em gramas é {pesoGramas:.2f}')