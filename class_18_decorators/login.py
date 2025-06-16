def login_req(func):
    def inner(name,status):
        if status == False:
            print("Login Required")
        else:
            return func(name,status)
    return inner