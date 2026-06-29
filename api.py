from flask import Flask, request, jsonify
from producer import send_message

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ API running. Use /send endpoint"

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "GET":
        return jsonify({
            "info": "Use POST to send message",
            "example": {
                "message": "Hello RabbitMQ"
            }
        })

    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"error": "Missing message"}), 400

        msg = data["message"]
        send_message(msg)

        return jsonify({
            "status": "Message sent",
            "message": msg
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)