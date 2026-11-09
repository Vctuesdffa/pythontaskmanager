from src.main import add_task, complete_task, tasks

def test_add_and_complete():
    tasks.clear()
    t = add_task("Тестовая задача")
    assert t["id"] == 1
    assert complete_task(1) is True
