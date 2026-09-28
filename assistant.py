```python from flask import Flask, request, jsonify app = Flask(name) @app.route

def chat data = request .json message = data .get("message", "") return jsonify app if name == "main" app.run()। 
