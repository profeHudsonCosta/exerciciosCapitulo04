listaAlunosNotas = []
quantAlunos = 0

quantAlunos = int(input("Informe a quantidade de alunos: "))

for aluno in range(0, quantAlunos):
    listaAlunosNotas.append([])
    print(aluno + 1,"o -", end="")
    nome = input("Informe o nome do aluno: ")
    nota = float(input("Informe a nota do aluno: "))
    listaAlunosNotas[aluno].append(nome)
    listaAlunosNotas[aluno].append(nota)

print("Exibição de acordo com a inserção:")
print("Alunos", end= " ")
print("\t Notas")
for i in listaAlunosNotas:
    print(i[0], end= " ")
    print("\t", i[1])

print("Exibição de acordo com o enunciado:")
print("Alunos", end= " ")
print("\t Notas")
listaAlunosNotas.reverse()
listaAlunosNotas.sort(reverse=True)
for i in listaAlunosNotas:
    print(i[0], end= " ")
    print("\t", i[1])
