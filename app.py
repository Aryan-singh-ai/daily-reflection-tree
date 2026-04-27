from flask import Flask, render_template, request, jsonify
from tree.tree_logic import evaluate_day

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json

    task_done = data.get("task_done")
    productivity = data.get("productivity")

    result = evaluate_day(task_done, productivity)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)