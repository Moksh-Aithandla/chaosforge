from app.api.app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["service"] == "ChaosForge"
    assert response.json["status"] == "running"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_create_experiment():
    client = app.test_client()

    response = client.post(
        "/experiments",
        json={
            "target": "demo-service",
            "action": "cpu_stress",
            "duration_seconds": 30
        }
    )

    assert response.status_code == 202
    assert response.json["message"] == "Experiment created successfully"
    assert response.json["experiment_id"]
    assert response.json["status"] == "pending"

def test_create_experiment_missing_fields():
    client = app.test_client()

    response = client.post(
        "/experiments",
        json={
            "target": "demo-service"
        }
    )

    assert response.status_code == 400
    assert "error" in response.json

def test_get_experiment():
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

    get_response = client.get(f"/experiments/{experiment_id}")

    assert get_response.status_code == 200
    assert get_response.json["experiment_id"] == experiment_id
    assert get_response.json["status"] == "pending"

def test_get_missing_experiment():
    client = app.test_client()

    response = client.get("/experiments/does-not-exist")

    assert response.status_code == 404
    assert response.json["error"] == "Experiment not found"