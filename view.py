def get_operation():
    number = int(input('Ведите 1 для заполнения справочника или введите 0 для чтения информации: '))
    if number == 1 or 0:
        return number
    else:
        print ('Введено неверное значение')