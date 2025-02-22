from decimal import Decimal

nota1 = Decimal(input("Digite a primeira nota: "))
nota2 = Decimal(input("Digite a segunda nota: "))

mediaPonderada = (Decimal(2) * nota1 + Decimal(3) * nota2) / Decimal(5)

print("A sua média é:", mediaPonderada)