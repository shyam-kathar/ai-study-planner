
def calculate_priority(task):
    """Return a priority score based on difficulty and urgency."""

    difficulty_scores = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3,
    }

    difficulty = difficulty_scores.get(task["difficulty"], 2)
    days_left = max(0, task["deadline_days"])

    urgency_score = 10 / (days_left + 1)

    return difficulty * 2 + urgency_score


def generate_study_plan(tasks, daily_hours):
    """Create a schedule that fits the available study time."""

    pending_tasks = [
        task for task in tasks
        if not task["completed"]
        and task["remaining_hours"] > 0
    ]

    pending_tasks.sort(
        key=calculate_priority,
        reverse=True,
    )

    study_plan = []
    remaining_time = float(daily_hours)

    for task in pending_tasks:
        if remaining_time <= 0:
            break

        allocated_time = min(
            task["remaining_hours"],
            remaining_time,
        )

        study_plan.append({
            "id": task["id"],
            "subject": task["subject"],
            "topic": task["topic"],
            "hours": round(allocated_time, 2),
            "priority": round(calculate_priority(task), 2),
        })

        remaining_time = round(
            remaining_time - allocated_time,
            2,
        )

    return study_plan


def get_next_task(study_plan):
    """Recommend the highest-priority scheduled task."""

    if not study_plan:
        return None

    return study_plan[0]


def get_progress(tasks):
    """Return the percentage of topics marked complete."""

    if not tasks:
        return 0

    completed_count = sum(
        1 for task in tasks if task["completed"]
    )

    return round(completed_count / len(tasks) * 100)
