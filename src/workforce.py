"""
Saudi Workforce Management
A practical workforce management tool for Saudi Arabia.
"""

from dataclasses import dataclass


@dataclass
class Worker:
    worker_id: str
    name: str
    job_title: str
    project: str
    hourly_rate: float
    working_hours: float
    status: str = "Active"

    @property
    def total_cost(self) -> float:
        return self.hourly_rate * self.working_hours


def show_worker(worker: Worker) -> None:
    print("\n--- Worker Details ---")
    print(f"Worker ID    : {worker.worker_id}")
    print(f"Name         : {worker.name}")
    print(f"Job Title    : {worker.job_title}")
    print(f"Project      : {worker.project}")
    print(f"Hourly Rate  : {worker.hourly_rate:.2f} SAR")
    print(f"Working Hours: {worker.working_hours:.2f}")
    print(f"Total Cost   : {worker.total_cost:.2f} SAR")
    print(f"Status       : {worker.status}")


def main() -> None:
    workers = [
        Worker("SWM-001", "Sample Worker 1", "Electrician", "Project A", 18.00, 208.00),
        Worker("SWM-002", "Sample Worker 2", "Carpenter", "Project A", 18.00, 208.00),
        Worker("SWM-003", "Sample Worker 3", "Mason", "Project B", 18.00, 208.00),
    ]

    print("🇸🇦 Saudi Workforce Management")
    print("=" * 40)

    total_project_cost = 0.0

    for worker in workers:
        show_worker(worker)
        total_project_cost += worker.total_cost

    print("\n--- Summary ---")
    print(f"Total Workers : {len(workers)}")
    print(f"Total Cost    : {total_project_cost:.2f} SAR")


if __name__ == "__main__":
    main()
