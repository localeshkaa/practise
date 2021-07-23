msg = {1: 'Взяли пиво', 2: 'Доставили пиво'}

def message(key):
    global msg
    flag = True
    if flag:
        flag = False
        print(msg[key])