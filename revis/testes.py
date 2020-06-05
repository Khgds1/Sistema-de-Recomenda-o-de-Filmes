import csv 

""""lista = [['julian', '0', '5'], ['ana', '10', '4']]
elemento = 'julian'
# vamos criar uma função de 'busca'
def encontrar(elemento):
    pos_i = 0 # variável provisória de índice
    pos_j = 0 # idem

    for i in range (len(lista)): # procurar em todas as listas internas
        for j in range (i): # procurar em todos os elementos nessa lista
            if elemento in lista[i][j]: # se encontrarmos elemento ('ana')
                pos_i = i # guardamos o índice i
                pos_j = j # e o índice j
                break # saímos do loop interno
            break # e do externo
    return (pos_i, pos_j) # e retornamos os índices


r = encontrar('julian') # chamamos a função e salvamos em r
print(r) # imprime índices
print(lista[r[0]][r[1]]) # usa índices na lista como prova"""


Geralzao = []
with open('ratings.csv','r', encoding="utf-8") as file:
    ObjetoUn = csv.reader(file)
    for linha in ObjetoUn:
        Geralzao.append(linha)

def FindMovie(user, movie):
    movieId = []
    for i in range(len(user)):
        userR = str(user[i])
        userR = userR.replace("'", "")
        userR = userR.replace("[", "")
        userR = userR.replace("]", "")
        if (userR == "1"):
            index = i
            movieId.append(movie[index])
    return movieId

userId = []
movieId = []
rating = []
for linha in Geralzao:
    Separado = []
    for separado in linha:
        Separado.append(separado.split(','))
    userId.append(Separado[0])
    movieId.append(Separado[1])
    rating.append(Separado[2])

sla = FindMovie(userId, movieId)
print(sla)


        

