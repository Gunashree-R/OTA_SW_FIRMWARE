from flask import Flask, jsonify, send_from_directory
import json

app = Flask(__name__)

@app.route("/version")
def get_version():
    with open("version.json", "r") as f:
        data = json.load(f)   # load JSON file
    return jsonify(data)      # return valid JSON response

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory("updates", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
