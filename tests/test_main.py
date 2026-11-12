from src.main import (
    tasks,
    add_task,
    complete_task,
    delete_task,
    validate_task_title,
    search_tasks_case_insensitive,
    get_task_stats,
)

def setup_function():
    tasks.clear()

def test_add_and_complete_task():
    task = add_task("Проверить Pull Request")
    assert task["id"] == 1
    assert complete_task(1) is True
    assert tasks[0]["done"] is True

def test_validation_and_search():
    assert validate_task_title("Git") is True
    assert validate_task_title("ab") is False
    add_task("Настроить GitHub Rulesets")
    results = search_tasks_case_insensitive("github")
    assert len(results) == 1

def test_stats_and_delete():
    add_task("Задача 1")
    add_task("Задача 2")
    complete_task(1)
    stats = get_task_stats()
    assert stats == {"total": 2, "completed": 1, "pending": 1}
    delete_task(1)
    assert len(tasks) == 1
