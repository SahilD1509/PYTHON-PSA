#Extract from Source
import requests,json
data=requests.get('https://dummyjson.com/products')
product_data=data.json()
print(type(product_data))
products=product_data['products']
print(type(products))
print(len(products))

#transform
beauty_products=[]
for prod in products:
    if prod['category'] == 'beauty':
        beauty_products.append({
            'id': prod['id'],
            'title': prod['title']
        })
        beauty_products.append(prod)

#load into json file
fp = open('beauty.json','w')
json.dump(beauty_products,fp)
print("New file created")
fp.close()