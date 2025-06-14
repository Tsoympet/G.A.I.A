from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import re

app = Flask(__name__)
CORS(app)

# Example license store (in production, use a secure DB)
valid_licenses = {
    "user@example.com": "GAIA-1234-5678-ABCD",
    "another@demo.com": "GAIA-9999-XXXX-YYYY"
}

def is_valid_email(email):
    # Basic email format validation
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route("/validate", methods=["POST"])
def validate_license():
    try:
        data = request.get_json()
        email = data.get("email", "").strip().lower()
        key = data.get("key", "").strip()

        if not email or not key:
            return jsonify({"valid": False, "error": "Missing fields"}), 400

        if not is_valid_email(email):
            return jsonify({"valid": False, "error": "Invalid email format"}), 400

        # Check license
        expected_key = valid_licenses.get(email)
        if expected_key and expected_key == key:
            return jsonify({"valid": True})
        else:
            return jsonify({"valid": False, "error": "Invalid license or email"}), 403
    except Exception as e:
        return jsonify({"valid": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
