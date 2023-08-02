tabela = [["Alexandre", 90, 100], ["Bruna", 100, 95], ["Diego", 30, 80], ["Felipe", 40, 10], ["Gabriela", 75, 60]]

for aluno in tabela:
    print(aluno[0])
print("--------------------")
for nome, frequencia, notafinal in tabela:
    print(nome, frequencia, notafinal)
