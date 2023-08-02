cont = 0
tabela = [["Alexandre", 90, 100], ["Bruna", 100, 95], ["Diego", 30, 80], ["Felipe", 40, 10], ["Gabriela", 75, 60]]
for reprovados in tabela:
    if reprovados[1] < 75 and reprovados[2] < 60:
        cont = cont + 1

print(cont, " alunos ficaram reprovados")
