import os

import redis


REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
QUEUE_NAME = "chaosforge:experiments"

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True,
)


def enqueue_experiment(experiment_id):
    redis_client.rpush(QUEUE_NAME, experiment_id)


def dequeue_experiment(timeout=5):
    result = redis_client.blpop(QUEUE_NAME, timeout=timeout)

    if result is None:
        return None

    _, experiment_id = result
    return experiment_id


def mark_complete():
    # Redis BLPOP removes the item from the queue when consumed.
    # No task_done() operation is required.
    pass


def clear_queue():
    while redis_client.llen(QUEUE_NAME) > 0:
        redis_client.lpop(QUEUE_NAME)