MatrizA = []
MatrizT = []

L = int(input("Informe o número de linhas da Matriz A: "))
C = int(input("Informe o número de colunas da Matriz A: "))

for i in range(0,L):
    MatrizA.append([])
    for j in range(0,C):
        el = int(input("Entre com o elemento da linha " + str(i+1) + " e coluna "+ str(j + 1) + ": "))
        MatrizA[i].append(el)

print("Matriz A")
for elem in MatrizA:
    print(elem)

for i in range(0,C):
    MatrizT.append([])
    for j in range(0,L):
        MatrizT[i].append(MatrizA[j][i])

print("Matriz transposta de A")
for elem in MatrizT:
    print(elem)
