my_dict = {}

# Добавим элементы в список, связанный с ключом 'key'
if 'key' in my_dict:
    my_dict['key'].append('value1')
    my_dict['key'].append('value2')
else:
    my_dict['key'] = ['value1', 'value2']