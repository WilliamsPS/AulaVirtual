from flask import Flask, request, jsonify
from pymongo import MongoClient
import psycopg2
import os

app = Flask(__name__)

POSTGRES_URL = os.environ.get('POSTGRES_URL', 'postgresql://postgres:postgres@postgres:5432/postgres')
MONGO_URL = os.environ.get('MONGO_URL', 'mongodb://mongo:27017/')

# Initialize PostgreSQL connection (placeholder)
try:
    pg_conn = psycopg2.connect(POSTGRES_URL)
    pg_conn.autocommit = True
except Exception:
    pg_conn = None

# Initialize MongoDB connection (placeholder)
try:
    mongo_client = MongoClient(MONGO_URL)
    mongo_db = mongo_client.get_database('aula')
except Exception:
    mongo_client = None
    mongo_db = None

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    # TODO: validate user against database
    return jsonify({'token': 'fake-token', 'user': username})

@app.route('/api/courses')
def courses():
    # TODO: fetch courses from database
    return jsonify({'courses': []})

@app.route('/api/library')
def library():
    # TODO: fetch library items from MongoDB
    return jsonify({'items': []})

@app.route('/api/videos')
def videos():
    # TODO: fetch videos from MongoDB
    return jsonify({'videos': []})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
