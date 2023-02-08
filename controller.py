import input_data as in_d
import output_data as out_d
import view

def choice():
    number = view.operation()
    if number == 1:
        in_d.new_record()
    elif number == 0:
        out_d.get_database()
    else:
        print('Операция недоступна')
