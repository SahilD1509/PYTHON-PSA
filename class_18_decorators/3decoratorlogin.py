def login_req(func):
    def inner(name,status):
        if status == False:
            print("Login Required")
        else:
            return func(name,status)
    return inner

@login_req
def home_page(name, status):
    print("Home Page")
@login_req
def order_page(name, status):
    print("Home Page")
@login_req
def update_page(name, status):
    print("Updating Profile")
@login_req
def contact_page(name, status):
    print("Contact Page")

home_page('RG',False)
order_page('RG',False)
update_page('RG',False)
contact_page('RG',True)