tabela = [["Alexandre", 90, 100], ["Bruna", 100, 95], ["Diego", 30, 80], ["Felipe", 40, 10], ["Gabriela", 75, 60]]
for aprovados in tabela:
    if aprovados[1] >= 75 and aprovados[2] >= 60:
        print(aprovados[0])
