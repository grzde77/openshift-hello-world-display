from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URL of the first app's API
API_URL = "http://my-hello-world-count:8080/api/visits"

@app.route("/")
def display_visits():
    try:
        # Call the first app's API to get the visit count
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        visit_count = data.get("visits", 0)
    except Exception as e:
        return jsonify({"error": "Unable to fetch visit count", "details": str(e)}), 500

    # Return the visit count as a response
    return jsonify({"message": f"Total visits recorded by the first app: {visit_count}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
