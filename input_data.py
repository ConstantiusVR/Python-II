def new_record():
    print ('Внесите новую запись с данными в следующей последовательности, через пробел: ID, Имя, Фамилия, номер телефона, комментарии ');
    with open ('phone_book.txt', 'a') as data:
        data.write (input() + '\n')

 