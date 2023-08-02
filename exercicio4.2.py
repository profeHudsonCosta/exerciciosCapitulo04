import math

Vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)

media = 0
variancia = 0
desvio = 0
soma = 0
somaVari = 0
quantVendas = len(Vendas)

for venda in Vendas:
    soma = soma + venda

media = soma/quantVendas

#Calculo da variância
for venda in Vendas:
    somaVari = somaVari + (venda - media)**2

variancia = somaVari/len(Vendas)

desvio = math.sqrt(variancia)

print("Valor médio das vendas: ", media)
print("A variância das vendas é: ", variancia)
print("O desvio padrão das vendas é: ", desvio)
