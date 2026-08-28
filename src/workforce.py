"""
Saudi Workforce Management
A practical workforce management tool for Saudi Arabia.
"""

from dataclasses import dataclass
import csv
from pathlib import Path


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


def load_workers_from_csv(csv_path: str) -> list[Worker]:
    workers = []

    with open(csv_path, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            workers.append(
                Worker(
                    worker_id=row["Worker ID"],
                    name=row["Name"],
                    job_title=row["Job Title"],
                    project=row["Project"],
                    hourly_rate=float(row["Hourly Rate (SAR)"]),
                    working_hours=float(row["Working Hours"]),
                    status=row["Status"],
                )
            )

    return workers


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
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "workforce_sample.csv"

    workers = load_workers_from_csv(str(csv_path))

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
