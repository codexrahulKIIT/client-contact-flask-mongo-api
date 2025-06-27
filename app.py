from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
from flasgger import Swagger, swag_from

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["client_db"]
collection = db["clients"]

@app.route('/clients', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of all clients',
            'content': {
                'application/json': {
                    'example': [{"_id": "abc123", "name": "John"}]
                }
            }
        }
    }
})
def get_clients():
    clients = list(collection.find({}))
    for client in clients:
        client['_id'] = str(client['_id'])
    return jsonify(clients), 200

@app.route('/clients', methods=['POST'])
@swag_from({
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'example': {
                    "name": "John Doe",
                    "email": "john@example.com",
                    "phone": "1234567890"
                }
            }
        }
    },
    'responses': {
        201: {
            'description': 'Client added successfully',
            'content': {
                'application/json': {
                    'example': {"inserted_id": "abc123"}
                }
            }
        }
    }
})
def add_client():
    data = request.get_json()
    result = collection.insert_one(data)
    return jsonify({"inserted_id": str(result.inserted_id)}), 201

@app.route('/clients/<string:id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        }
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'example': {
                    "name": "Updated Name",
                    "email": "updated@example.com"
                }
            }
        }
    },
    'responses': {
        200: {'description': 'Client updated successfully'},
        404: {'description': 'Client not found'}
    }
})
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

@app.route('/clients/<string:id>', methods=['DELETE'])
@swag_from({
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'string'}
        }
    ],
    'responses': {
        200: {'description': 'Client deleted successfully'},
        404: {'description': 'Client not found'}
    }
})
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
