from queue import Queue


experiment_queue = Queue()


def enqueue_experiment(experiment_id):
    experiment_queue.put(experiment_id)


def dequeue_experiment(timeout=3):
    return experiment_queue.get(timeout=timeout)


def mark_complete():
    experiment_queue.task_done()


def clear_queue():
    while not experiment_queue.empty():
        experiment_queue.get_nowait()
        experiment_queue.task_done()