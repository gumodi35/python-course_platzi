# declaring the functio to verify if the number is prime

def isPrime(num):
   # if num == '':
   #   return print('give me a number')
    if num < 1: 
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

# declaring the function to receive the input
def app():
    num = int(input('Give me your number budy: '))
    result = isPrime(num)

    if result is True:
        print('Yep the Number is Prime champ!!')
    else:
        print('Nope the Number is not Prime champ!!')

    if __name__ == '__main__':
        app()