from csv import reader
#
with open('ratings.csv', 'r', encoding='utf8') as read_obj:
    csvreader = reader(read_obj)
    usuarios = list(csvreader)
#info - 0 = userId, 1 = movieId, 2 = rating, 3 = timestamp    
def users(ind, pos):
    print(usuarios[ind][pos])
#
with open('movies.csv', 'r', encoding="utf8") as read_obj:
    csvreader = reader(read_obj)
    filmes = list(csvreader)
#info - 0 = movieId, 1 = title, 2 = genres    
def movies(ind, pos):
    print(filmes[ind][pos]) 
#
def titulo(msg):
    print('-'*50)
    print(msg)
    print('-'*50)