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
    assert response.json["message"] == "Experiment accepted"
    assert response.json["experiment"]["status"] == "simulated"

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