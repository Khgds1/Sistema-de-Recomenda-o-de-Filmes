#Importações
import csv
from random import randint

##Importando Ratings.csv
rcomp = []
with open('ratings.csv', 'r', encoding='utf8') as file:
    ndf = csv.reader(file)
    for linha in ndf:
        rcomp.append(linha)

##Importando Movies.csv
mcomp = []
with open('movies.csv', 'r', encoding='utf8') as file:
    ndf = csv.reader(file)
    for linha in ndf:
        mcomp.append(linha)

#Entradas
#b1 = 0 
#b1 = 0
print('Info: o ID deve ser entre 1 e 63')
idUser = str(input('Informe a ID do usuário: ')) 
#idMovie = str(input('Informe a ID de um filmes: '))
print('Info: o ID deve ser entre 1 e 63')
userId2 = str(input('Informe a ID de um outro usuário: '))

#Dividindo Listas
##Ratings.csv
userId = []
movieId = []
rating = []
for linha in rcomp:
    Separado = []
    for separado in linha:
        Separado.append(separado.split(','))
    userId.append(Separado[0])
    movieId.append(Separado[1])
    rating.append(Separado[2])

##Movies.csv
title = []
genres = []
for linha in mcomp:
    Separado = []
    for separado in linha:
        Separado.append(separado.split(','))
    title.append(Separado[1])
    genres.append(Separado[2])   
cat = []     
for linha in genres:
    Separado = []
    for separado in linha:
        Separado.append(separado.split('|'))
    cat.append(Separado[0])    
cat2 = []    
for linha in cat:
    Separado = []
    for separado in linha:
        Separado.append(separado.split(','))
    cat2.append(Separado[0])    

##Lista de Generos sem Repetição
###id = 1 - 18
listLimpa = []
for i in range(len(cat2)):
    if cat2[i] not in listLimpa:
        listLimpa.append(cat2[i])

#Listas Externas
notasA = []     #Filmes com notas mais altas do Usuario1
notasA2 = []    #Filmes com notas mais altas do Usuario2
reco = []
lfilm = []

#Buscas
def busca(user, movie, rat, gene, userId2, title):
    movieId = []
    movieId2 = []
    genres = []
    genres2 = []
    for i in range(len(user)):
        userR = str(user[i])
        userR = userR.replace("'", "")
        userR = userR.replace("[", "")
        userR = userR.replace("]", "")
        if (userR == idUser):
            index = i
            movieId.append(movie[index])
            movieId.append(rat[index])
            genres.append(gene[index])
            if '4.0' in rat[index]:
                notasA.append(movie[index])
            if '4.5' in rat[index]:
                notasA.append(movie[index])
            if '5.0' in rat[index]:
                notasA.append(movie[index])  
    cat = []
    for linha in genres:
        Separado = []
        for separado in linha:
            Separado.append(separado.split('|'))
        cat.append(Separado[0])    
    catc = []
    for linha in cat:
        Separado = [] 
        for separado in linha:
            Separado.append(separado.split(','))
        catc.append(Separado[0])         
    
    for i in range(len(user)):
        userR = str(user[i])
        userR = userR.replace("'", "")
        userR = userR.replace("[", "")
        userR = userR.replace("]", "")
        if (userR == userId2):
            ind = i
            movieId2.append(movie[ind])
            genres2.append(gene[ind])
            if '4.0' in rat[ind]:
                notasA2.append(movie[ind])
            if '4.5' in rat[ind]:
                notasA2.append(movie[ind])
            if '5.0' in rat[ind]:
                notasA2.append(movie[ind])
    cat2 = []
    for linha in genres2:
        Separado = []
        for separado in linha:
            Separado.append(separado.split('|'))
        cat2.append(Separado[0])  

#Encontrando categoria favorita     
    prefGen = ''
    prefGen2 = ''
    cb = 2
    cb2 = 2
    ff = 1
    ff2 = 1
    while ff <= 18:
        for f in range(len(catc)):
            x = catc.count(listLimpa[ff])
            if x > cb:
                prefGen = listLimpa[ff]
                cb = x
        ff = ff + 1      
    while ff2 <= 18:
        for g in range(len(catc)):
            z = catc.count(listLimpa[ff2])
            if z > cb2 and z < cb:
                prefGen2 = listLimpa[ff2]
        ff2 = ff2 + 1       

#Comparando
    for n in range(len(cat2)):
        prefGenR = str(prefGen)
        prefGenR = prefGenR.replace("'", "")
        prefGenR = prefGenR.replace("[", "")
        prefGenR = prefGenR.replace("]", "")
        if prefGenR in cat2[n]:
            if movieId2[n] not in reco:
                reco.append(movieId2[n])
        prefGen2R = str(prefGen2)
        prefGen2R = prefGen2R.replace("'", "")
        prefGen2R = prefGen2R.replace("[", "")
        prefGen2R = prefGen2R.replace("]", "")        
        if prefGen2R in cat2[n]:
            if movieId2[n] not in reco:
                reco.append(movieId2[n])
    print('-'*50)        
    print('Recomendamos  os seguintes filmes para o usuário:')        
    for m in range(len(reco)):
        print('{}'.format(reco[m]))
    return movieId               

#Info Def    
busca(userId, title, rating, genres, userId2, title)
