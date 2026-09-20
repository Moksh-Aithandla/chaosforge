from flask import Flask, jsonify, request
from app.services.experiment_service import build_experiment
from app.services.experiment_store import save_experiment, get_experiment
from app.services.experiment_worker import execute_experiment

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "ChaosForge",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    
@app.route("/experiments", methods=["POST"])
def create_experiment():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    target = data.get("target")
    action = data.get("action")
    duration_seconds = data.get("duration_seconds")

    if not target or not action or duration_seconds is None:
        return jsonify({
            "error": "target, action, and duration_seconds are required"
        }), 400

    result = build_experiment(
        target=target,
        action=action,
        duration_seconds=duration_seconds
    )

    save_experiment(result)

    return jsonify(result), 202

@app.route("/experiments/<experiment_id>", methods=["GET"])
def retrieve_experiment(experiment_id):
    experiment = get_experiment(experiment_id)

    if experiment is None:
        return jsonify({
            "error": "Experiment not found"
        }), 404

    return jsonify(experiment), 200


@app.route("/experiments/<experiment_id>/execute", methods=["POST"])
def execute_experiment_route(experiment_id):
    result = execute_experiment(experiment_id)

    if result is None:
        return jsonify({
            "error": "Experiment not found"
        }), 404

    return jsonify(result), 200