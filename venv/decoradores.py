# programando un decorador
def hello_world(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("Hello world!")
    return wrapper

@hello_world
def hello_world2():
    print("Now I'm Hello World 2")

hello_world2()
print("Now I'm Hello World 3")