import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from flask_cors import CORS
from agents.router import RouterAgent


app = Flask(
    __name__,
    static_folder="../frontend",
    static_url_path=""
)
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize Router Agent
router = RouterAgent()
@app.route('/')
def home():
    return app.send_static_file('index.html')




@app.route('/health')
def health():
    return jsonify({"status": "healthy"})


@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"})

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"response": "No message provided"}), 400

    message = data.get("message", "").strip()

    if not message:
        return jsonify({"response": "Empty message"}), 400

    # Route query to appropriate agent
    response = router.route(message)

    return jsonify({"response": response})


if __name__ == '__main__':
    print("=" * 50)
    print("Starting Coal Chatbot Backend...")
    print("Multi-Agent Architecture Enabled")
    print("API running at: http://localhost:5000")
    print("=" * 50)

    app.run(host='0.0.0.0', port=5000, debug=True)