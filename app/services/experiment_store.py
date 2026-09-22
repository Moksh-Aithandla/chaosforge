import os
import sqlite3


DATABASE = os.getenv("CHAOSFORGE_DATABASE", "chaosforge.db")


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS experiments (
            experiment_id TEXT PRIMARY KEY,
            target TEXT NOT NULL,
            action TEXT NOT NULL,
            duration_seconds INTEGER NOT NULL,
            status TEXT NOT NULL,
            message TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()


def save_experiment(experiment):
    connection = get_connection()

    connection.execute(
        """
        INSERT OR REPLACE INTO experiments (
            experiment_id,
            target,
            action,
            duration_seconds,
            status,
            message
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            experiment["experiment_id"],
            experiment["target"],
            experiment["action"],
            experiment["duration_seconds"],
            experiment["status"],
            experiment["message"],
        ),
    )

    connection.commit()
    connection.close()

    return experiment


def get_experiment(experiment_id):
    connection = get_connection()

    row = connection.execute(
        """
        SELECT
            experiment_id,
            target,
            action,
            duration_seconds,
            status,
            message
        FROM experiments
        WHERE experiment_id = ?
        """,
        (experiment_id,),
    ).fetchone()

    connection.close()

    if row is None:
        return None

    return dict(row)