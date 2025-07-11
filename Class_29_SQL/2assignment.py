import requests, csv, json
import mysql.connector
from pymongo import MongoClient

try:
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    # Save to CSV & JSON
    keys = users[0].keys()
    with open("users.csv", "w", newline='') as f: csv.DictWriter(f, keys).writeheader(); csv.DictWriter(f, keys).writerows(users)
    with open("users.json", "w") as f: json.dump(users, f, indent=2)

    # MySQL
    db = mysql.connector.connect(host='localhost', user='root', password='root', database='dbone')
    cur = db.cursor()

    for u in users:
        cur.execute("REPLACE INTO user_data VALUES (%s, %s, %s, %s)", (u['id'], u['name'], u['username'], u['email']))
    db.commit(); cur.close(); db.close()

    # MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    dbm = client["testdb"]; col = dbm["user_data"]
    col.delete_many({}); col.insert_many(users)
    client.close()

    print("Done!")

except Exception as e:
    print("Error:", e)
