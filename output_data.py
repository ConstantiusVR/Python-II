def get_database():
    path = 'phone_book.txt'
    data = open(path, 'r')
    for line in data:
        print (line)


