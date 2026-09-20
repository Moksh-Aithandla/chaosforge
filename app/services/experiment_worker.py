from app.services.experiment_status import RUNNING, COMPLETED, FAILED
from app.services.experiment_store import get_experiment, save_experiment


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

def test_execute_experiment():
    client = app.test_client()

    create_response = client.post(
        "/experiments",
        json={
            "target": "demo-service",
            "action": "cpu_stress",
            "duration_seconds": 30
        }
    )

    experiment_id = create_response.json["experiment_id"]

    result = execute_experiment(experiment_id)

    assert result["experiment_id"] == experiment_id
    assert result["status"] == "completed"
    assert result["message"] == "Experiment completed successfully"

def test_execute_missing_experiment():
    result = execute_experiment("does-not-exist")

    assert result is None