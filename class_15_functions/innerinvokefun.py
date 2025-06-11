def outer():
    print("Outer Function Started")

    def inner():
        print("Inner Function Started")

    return inner

inner = outer()
inner()
inner()