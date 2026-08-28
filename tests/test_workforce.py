from src.workforce import Worker


def test_worker_total_cost():
    worker = Worker(
        "TEST-001",
        "Test Worker",
        "Electrician",
        "Test Project",
        18.00,
        208.00,
    )

    assert worker.total_cost == 3744.00
