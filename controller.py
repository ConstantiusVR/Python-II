import input_data as in_d
import output_data as out_d
import view

def choice():
    res = None
    number = view.get_operation()
    if number == 1:
        res = in_d.new_record()
    else:
        res = out_d.get_database()
    