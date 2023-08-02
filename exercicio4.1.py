entrada = (1000, 2000, 5, 15000, 12, 1, 0.5, -2, 1000)
soma =0

for valor in entrada:
    if valor < 100:
        soma = soma + valor
print("A soma dos números menores que 100 é ", soma)
