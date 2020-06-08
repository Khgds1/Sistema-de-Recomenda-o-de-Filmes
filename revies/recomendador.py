#Importações
import csv

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

print(rcomp)