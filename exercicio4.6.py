tabela = [["Alexandre", 90, 80], ["Bruna", 100, 95], ["Diego", 30, 80], ["Felipe", 40, 10], ["Gabriela", 75, 60]]

maiorNota = tabela[0][2]
alunoMaiorNota = tabela[0][0]

for buscaMaior in tabela:    
    if buscaMaior[2] > maiorNota:
        maiorNota = buscaMaior[2]
        alunoMaiorNota = buscaMaior[0]

print("A maior nota foi ", maiorNota, "e o aluno que tirou ela foi: ", alunoMaiorNota)
