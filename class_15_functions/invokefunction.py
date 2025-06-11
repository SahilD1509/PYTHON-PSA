def outer():
    print("Outer function started")

    def inner():
        print("Inner Function")
    inner()

    def login():
        print("Login Success")
    login()

outer()