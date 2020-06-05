#from csv import reader
import csv



#Utilitarios
def titulo(msg):
    print('-'*50)
    print(msg)
    print('-'*50)



lcomp = []
with open('ratings.csv', 'r', encoding="utf8") as file:
    ndf = csv.reader(file)
    for linha in ndf:
        lcomp.append(linha)


def busca(user, movie):
    movieId = []
    for i in range(len(user)):
        userR = str(user[i])
        userR = userR.replace("'", "")
        userR = userR.replace("[", "")
        userR = userR.replace("]", "")
        if (userR == "8"):
            index = i
            movieId.append(movie[index])
    return movieId

userId = []
movieId = []
rating = []
for linha in lcomp:
    Separado = []
    for separado in linha:
        Separado.append(separado.split(','))
    userId.append(Separado[0])
    movieId.append(Separado[1])
    rating.append(Separado[2])

comb = busca(userId, movieId)
print(comb)




