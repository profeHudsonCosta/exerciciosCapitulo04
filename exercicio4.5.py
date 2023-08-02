tabela = [["Alexandre", 90, 100], ["Bruna", 100, 95], ["Diego", 30, 80], ["Felipe", 40, 10], ["Gabriela", 75, 60]]
contRepNotas = 0
contRepFaltas = 0

for reprovados in tabela:
    if (reprovados[1] < 75):
        contRepFaltas = contRepFaltas + 1
    
    if (reprovados[2] < 60):
        contRepNotas = contRepNotas + 1

percNotas = (len(tabela)*contRepNotas)/100
percFreq = (len(tabela) * contRepFaltas)/100

print("Reprovados por faltas: ", contRepFaltas)
print("Reprovados notas: ", contRepNotas)
print("Percentual de alunos reprovados por nota: ", percNotas, "%")
print("Percentaul de alunos reprovados por falta: ", percFreq, "%")
