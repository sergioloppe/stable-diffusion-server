from flask import jsonify, send_from_directory
from src.main import app


@app.route('/api', defaults={'path': ''})
def serve(path):
    try:
        return send_from_directory(app.static_folder, 'index.html')
    except FileNotFoundError:
        # Handle missing files correctly
        return jsonify({"error": "Not found", "message": "Resource not found"}), 404


@app.route('/api/test')
def test():
    return jsonify({"message": "Hello, World!"})
