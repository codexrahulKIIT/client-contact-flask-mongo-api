from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId  # for PUT/DELETE by ID
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["client_db"]
collection = db["clients"]

# ------------------------ GET ------------------------
@app.route('/clients', methods=['GET'])
def get_clients():
    clients = list(collection.find({}))
    for client in clients:
        client['_id'] = str(client['_id'])  # Convert ObjectId to string
    return jsonify(clients), 200

# ------------------------ POST ------------------------
@app.route('/clients', methods=['POST'])
def add_client():
    data = request.get_json()
    result = collection.insert_one(data)
    return jsonify({"inserted_id": str(result.inserted_id)}), 201

# ------------------------ PUT ------------------------
@app.route('/clients/<string:id>', methods=['PUT'])
def update_client(id):
    try:
        data = request.get_json()
        update_result = collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )
        if update_result.matched_count == 0:
            return jsonify({'error': 'Client not found'}), 404
        return jsonify({'message': 'Client updated successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ------------------------ DELETE ------------------------
@app.route('/clients/<string:id>', methods=['DELETE'])
def delete_client(id):
    try:
        delete_result = collection.delete_one({"_id": ObjectId(id)})
        if delete_result.deleted_count == 0:
            return jsonify({'error': 'Client not found'}), 404
        return jsonify({'message': 'Client deleted successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
