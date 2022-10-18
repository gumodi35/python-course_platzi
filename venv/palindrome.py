# funcion para verificar si una palabra es palindromo
def is_palindrome(string: str) -> bool:
# verificamos que la palabra no tenga espacios en caso de tener los elimina y la pasa a minusculas 
    string = string.replace(' ', '').lower()
# verificamos que la palabra sea igual a la palabra al reves
    return string == string[::-1]

def run():
    print(is_palindrome('anita lava la tina'))

if __name__ == '__main__':
    run()