from app.services.experiment_queue import (
    enqueue_experiment,
    dequeue_experiment,
    clear_queue,
)


def test_experiment_queue():
    clear_queue()

    experiment_id = "queue-test-123"

    enqueue_experiment(experiment_id)

    result = dequeue_experiment(timeout=1)

    assert result == experiment_id

    clear_queue()