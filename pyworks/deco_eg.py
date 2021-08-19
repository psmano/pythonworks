def func():
    return 1

func()

def hello():
    return "Hello!"

greet = hello

print(greet())

print(hello())

del hello

#print(hello())
print(greet())

def hello(name='Jose'):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() function inside hello()!'

    def welcome():
        return '\t This is welcome inside hello()!'

    print('I am going to return a function!')

    if name == 'Jose':
        return greet
    else:
        return welcome

    print(greet())
    print(welcome())
    print('This is the end of the hello function')

my_new_func = hello('Jose')
print(my_new_func)