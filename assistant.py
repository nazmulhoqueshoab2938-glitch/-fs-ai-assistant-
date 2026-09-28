from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# API key environment variable থেকে নেওয়া হবে
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "reply": "Please enter a message."
        })

    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            input=message
        )

        return jsonify({
            "reply": response.output_text
        })

    except Exception as e:
        print("Error:", e)

        return jsonify({
            "reply": "Sorry, I couldn't connect to the AI."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
