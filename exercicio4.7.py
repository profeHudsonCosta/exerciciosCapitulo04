import math

tabela = [["Alexandre", 90, 100], ["Bruna", 100, 95], ["Diego", 30, 80], ["Felipe", 40, 10], ["Gabriela", 75, 60]]

somaNotas = 0
contRep = 0
somaNotasVar = 0

for media in tabela:
    somaNotas = somaNotas + media[2]
    if (media[1] < 75) and (media[2] < 60):
        contRep = contRep +1

#print(len(tabela))
#print(somaNotas)
media = somaNotas/len(tabela)
for vari in tabela:
    somaNotasVar = somaNotasVar + (vari[2] - media)**2

variancia = somaNotasVar/len(tabela)

desvioPadrao = math.sqrt(variancia)

percRep = (len(tabela)*contRep)/100

print("A média aritimética da turma é: ", media)
print("O desvio padrão da turma é: ", desvioPadrao)
print("O percentual de reprovações é: ", percRep, "%")
