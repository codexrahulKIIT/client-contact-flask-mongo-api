from flask import Blueprint, request, jsonify
from db_config import init_db
from MySQLdb import OperationalError

client_routes = Blueprint('client_routes', __name__)
mysql = None

@client_routes.record_once
def setup(state):
    global mysql
    mysql = init_db(state.app)

# POST - Add client
@client_routes.route('/clients', methods=['POST'])
def add_client():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        company = data.get('company')
        phone = data.get('phone')
        status = data.get('status')

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO clients (name, email, company, phone, status)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, email, company, phone, status))
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Client added successfully!'}), 201

    except OperationalError:
        return jsonify({'error': 'Database connection lost'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# GET - All clients
@client_routes.route('/clients', methods=['GET'])
def get_clients():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM clients")
        rows = cur.fetchall()
        cur.close()

        clients = [
            {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'company': row[3],
                'phone': row[4],
                'status': row[5]
            } for row in rows
        ]
        return jsonify(clients), 200
    except OperationalError:
        return jsonify({'error': 'Database connection lost'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
