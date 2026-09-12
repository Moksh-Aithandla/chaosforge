from uuid import uuid4


def run_experiment(target, action, duration_seconds):
    return {
        "experiment_id": str(uuid4()),
        "target": target,
        "action": action,
        "duration_seconds": duration_seconds,
        "status": "simulated",
        "message": "Experiment simulated successfully"
    }