from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

messages = []
users = []

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/register', methods=['POST'])
def register_user():
    username = request.json.get('username')
    if username not in users:
        users.append(username)
        return jsonify({"status": "User registered"}), 201
    return jsonify({"error": "User already exists"}), 400

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/messages', methods=['POST'])
def post_message():
    message = request.json.get('message')
    if message:
        messages.append(message)
        return jsonify({"status": "Message received"}), 201
    return jsonify({"error": "No message provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
