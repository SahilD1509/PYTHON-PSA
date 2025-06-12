product_prices = [98,198,298,398,498]
new_prices = []

#using for loop
for price in product_prices:
    new_prices.append(price + 1)
print(new_prices)

#using lambda
def addone(price):
    return price + 1
map_obj=map(addone,product_prices)
new_prices = list(map_obj)
print(product_prices)
print(new_prices)