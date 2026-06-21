from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
tasks = [{"id": 1, "title": "Build ML portfolio project", "completed": False}, {"id": 2, "title": "Practice JavaScript interview questions", "completed": False}]
next_id = 3

@app.get("/api/tasks")
def get_tasks():
    return jsonify(tasks)

@app.post("/api/tasks")
def create_task():
    global next_id
    data = request.get_json() or {}
    title = data.get("title", "").strip()
    if not title:
        return jsonify({"error": "Task title is required"}), 400
    task = {"id": next_id, "title": title, "completed": False}
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

@app.patch("/api/tasks/<int:task_id>")
def update_task(task_id):
    data = request.get_json() or {}
    for task in tasks:
        if task["id"] == task_id:
            if "title" in data: task["title"] = data["title"].strip()
            if "completed" in data: task["completed"] = bool(data["completed"])
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.delete("/api/tasks/<int:task_id>")
def delete_task(task_id):
    global tasks
    before = len(tasks)
    tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == before:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"status": "deleted"})

if __name__ == "__main__":
    app.run(debug=True)
