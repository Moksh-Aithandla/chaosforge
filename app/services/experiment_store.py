experiments = {}


def save_experiment(experiment):
    experiments[experiment["experiment_id"]] = experiment
    return experiment


def get_experiment(experiment_id):
    return experiments.get(experiment_id)