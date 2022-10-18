# Eliminar repetidos

def remove_duplicates(list)
    new_list = []
    for item in list:
        if item not in new_list:
            new_list.append(item)
    return new_list

def run():
    random_list = [1, 1, 2, 2, 4]
    print(random_list)

if __name__ == '__main__':
    run()
