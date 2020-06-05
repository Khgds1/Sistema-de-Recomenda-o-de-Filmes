from csv import reader
#
with open('movies.csv', 'r', encoding="utf8") as read_obj:
    csvreader = reader(read_obj)
    list = list(csvreader)
    print(list)
#
def titulo(msg):
    print('-'*50)
    print(msg)
    print('-'*50)