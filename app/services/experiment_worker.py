from queue import Empty

from app.services.experiment_status import RUNNING, COMPLETED, FAILED
from app.services.experiment_store import get_experiment, save_experiment
from app.services.experiment_queue import dequeue_experiment, mark_complete


def execute_experiment(experiment_id):
    experiment = get_experiment(experiment_id)

    if experiment is None:
        return None

    experiment["status"] = RUNNING
    save_experiment(experiment)

    try:
        # Simulated chaos action.
        # Real AWS/Kubernetes actions will be added later.
        experiment["status"] = COMPLETED
        experiment["message"] = "Experiment completed successfully"

    except Exception as error:
        experiment["status"] = FAILED
        experiment["message"] = str(error)

    save_experiment(experiment)

    return experiment


def process_next_experiment():
    try:
        experiment_id = dequeue_experiment(timeout=1)
    except Empty:
        return None

    try:
        return execute_experiment(experiment_id)
    finally:
        mark_complete()