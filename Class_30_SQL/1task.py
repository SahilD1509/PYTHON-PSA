import requests,csv, json
import mysql.connector
import pymongo
#Extract Data

users_resp=requests.get("https://jsonplaceholder.typicode.com/users")
users=users_resp.json()
print(type(users))

#Transform for csv
user_data = []
for user in users:
    user_data.append((user['id'],user['username'],user['email']))

#transform for json
user_json_data = []
for user in users:
    user_json_data.append({'uid':user['id'], 'uname': user['username']})

#Loads data in csv file
fp = open('users.csv','w',newline='')
cw_obj = csv.writer(fp)
cw_obj.writerow(['uid','uname','email','city'])
cw_obj.writerows(user_data)
print("New Csv file created")


fp2=open("users.json",'w')
json.dump(user_json_data, fp2)
print("New json file is created")


"""dbcon = None
try:
    db = mysql.connector.connect(host="localhost",user="root",password="root",database="dbone")"""
