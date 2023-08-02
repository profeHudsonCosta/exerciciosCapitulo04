Matriz =[]

N = int(input("Entre com o número de linhas da matriz: "))
M = int(input("Entre com o número de colunas da matriz: "))

for i in range(0,N):
    Matriz.append([])
    for j in range(0,M):
        el = int(input("Entre com o elemento da linha " + str(i+1) + " e coluna " + str(j + 1) + ": "))
        Matriz[i].append(el)
        print(Matriz)
