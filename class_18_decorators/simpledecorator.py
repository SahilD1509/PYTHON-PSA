def decorator(func):
    def wrapper():
        print("Before Callling the function")
        func()
        print("After calling the function")
    return wrapper

@decorator
def greet():
    print("Hello World")
greet()