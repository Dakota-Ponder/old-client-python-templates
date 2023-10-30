# program that authenticates users using a username and password.
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
users = {}


@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    username = request.json.get('username')
    password = request.json.get('password')
    if username in users:
        return jsonify({'message': 'Username already taken'}), 400
    users[username] = generate_password_hash(password)
    return jsonify({'message': 'Successfully registered'}), 201


@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user."""
    username = request.json.get('username')
    password = request.json.get('password')
    if username not in users or not check_password_hash(users[username], password):
        return jsonify({'message': 'Invalid credentials'}), 401
    return jsonify({'message': 'Logged in successfully'}), 200


if __name__ == '__main__':
    app.run()
