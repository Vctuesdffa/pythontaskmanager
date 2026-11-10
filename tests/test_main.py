from src.main import tasks, add_task, complete_task, search_tasks, get_statistics

def test_add_and_search():
    tasks.clear()
    add_task("Проверить Git PR", "Высокий")
    results = search_tasks("git")
    assert len(results) == 1
    assert results[0]["priority"] == "Высокий"

def test_statistics():
    tasks.clear()
    add_task("Задача 1", "Средний")
    add_task("Задача 2", "Низкий")
    complete_task(1)
    stats = get_statistics()
    assert stats == {"total": 2, "completed": 1, "pending": 1}
