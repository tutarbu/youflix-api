from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/get_link")
def get_link():
    yt_url = request.args.get("yt")
    if not yt_url:
        return jsonify({"error": "YouTube link eksik"}), 400
    try:
        result = subprocess.check_output(["yt-dlp", "-g", yt_url])
        return jsonify({"video_url": result.decode().strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
