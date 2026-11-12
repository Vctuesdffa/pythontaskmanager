import src.main as app

def setup_function():
    app.tasks.clear()

def test_add_and_complete_task():
    task = app.add_task("Проверить Pull Request")
    assert task["id"] == 1
    assert app.complete_task(1) is True
    assert app.tasks[0]["done"] is True

def test_validation_and_search():
    assert app.validate_task_title("Git") is True
    assert app.validate_task_title("ab") is False
    app.add_task("Настроить GitHub Rulesets")
    results = app.search_tasks_case_insensitive("github")
    assert len(results) == 1

def test_stats_and_delete():
    app.add_task("Задача 1")
    app.add_task("Задача 2")
    app.complete_task(1)
    stats = app.get_task_stats()
    assert stats == {"total": 2, "completed": 1, "pending": 1}
    app.delete_task(1)
    assert len(app.tasks) == 1
