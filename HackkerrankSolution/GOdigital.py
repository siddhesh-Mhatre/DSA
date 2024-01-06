my_dictionary = {
    'student': {
        'name': 'siddhesh',
        'roll_no': 34,
        'class': 'MscIT'
    },

    'car': {
        'model': 'toyota',
        'color': 'white'
    }
}

path='student.roll_no'
my_item , my_key = path.split('.')
for i in my_dictionary:
    if i==my_item:
        for key, value in my_dictionary[i].items():
            if key==my_key:
                print(value)
        break
    else:
        print(None)
