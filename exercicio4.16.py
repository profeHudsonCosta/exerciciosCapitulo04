dist = {1:{2:1, 3:2, 4:3, 5:4}, 
        2:{1:2, 5:3},
        3:{1:2, 4:2},
        4:{1:3, 5:1, 3:2},
        5:{1:4, 4:1, 2:3}}

somaDist = 0
flag = 1
while flag != -1:
    p1 = int(input("Informe o 1o ponto: "))
    p2 = int(input("Informe o 2o ponto: "))
    somaDist = somaDist + dist[p1][p2]
    flag = int(input("Digite -1 para sair: "))

print("A distância percorrida é: ", somaDist)
