from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

def get_db_client():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    return client

@app.route('/')
def ping_server():
    client = get_db_client()
    client.admin.command('ping')
    return "DB is working."

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)