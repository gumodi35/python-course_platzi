# programa para eliminar duplicados de una lista usando set

def eliminar_duplicado(lista):
    return list(set(lista))

def main():
    lista = [1,1,2,3,4,5,5,6,7,8,9,9,10]
    print(eliminar_duplicado(lista))

if __name__ == "__main__":
    main()