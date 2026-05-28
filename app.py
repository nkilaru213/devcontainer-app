from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Set up devcontainer", "done": True},
    {"id": 2, "title": "Run Flask app", "done": False},
]

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

@app.route("/api/tasks", methods=["GET", "POST"])
def task_api():
    if request.method == "POST":
        data = request.get_json() or {}
        title = data.get("title", "").strip()

        if not title:
            return jsonify({"error": "Task title is required"}), 400

        new_task = {
            "id": len(tasks) + 1,
            "title": title,
            "done": False
        }
        tasks.append(new_task)
        return jsonify(new_task), 201

    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
