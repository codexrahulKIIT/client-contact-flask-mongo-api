from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import os

client_routes = Blueprint('client_routes', __name__)

# Initialize MongoDB connection
mongo_url = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_url)
db = client['client_db']
collection = db['clients']


# POST - Add client
@client_routes.route('/clients', methods=['POST'])
def add_client():
    try:
        data = request.get_json()
        required_fields = ['name', 'email', 'company', 'phone', 'status']
        
        # Validation: Check for missing or empty fields
        if not all(field in data and data[field] for field in required_fields):
            return jsonify({'error': 'Missing or empty required fields'}), 400

        # Insert the validated data
        collection.insert_one(data)
        return jsonify({'message': 'Client added successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# GET - Retrieve all clients
@client_routes.route('/clients', methods=['GET'])
def get_clients():
    try:
        clients = []
        for client in collection.find():
            client['_id'] = str(client['_id'])  # Convert ObjectId to string
            clients.append(client)
        return jsonify(clients), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# PUT - Update client by ID
@client_routes.route('/clients/<client_id>', methods=['PUT'])
def update_client(client_id):
    try:
        data = request.get_json()
        result = collection.update_one({'_id': ObjectId(client_id)}, {'$set': data})
        if result.matched_count == 0:
            return jsonify({'error': 'Client not found'}), 404
        return jsonify({'message': 'Client updated successfully!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# DELETE - Delete client by ID
@client_routes.route('/clients/<client_id>', methods=['DELETE'])
def delete_client(client_id):
    try:
        result = collection.delete_one({'_id': ObjectId(client_id)})
        if result.deleted_count == 0:
            return jsonify({'error': 'Client not found'}), 404
        return jsonify({'message': 'Client deleted successfully!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
