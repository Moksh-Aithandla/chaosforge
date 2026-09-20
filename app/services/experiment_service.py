from uuid import uuid4

from app.services.experiment_status import PENDING


def build_experiment(target, action, duration_seconds):
    return {
        "experiment_id": str(uuid4()),
        "target": target,
        "action": action,
        "duration_seconds": duration_seconds,
        "status": PENDING,
        "message": "Experiment created successfully"
    }