APP_TITLE = "=== Консольный менеджер задач (Python Task Manager v2.0) ==="
tasks = []

def add_task(title):
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    return task

def list_tasks():
    if not tasks:
        print("Список задач пуст.")
    for t in tasks:
        status = "[X]" if t["done"] else "[ ]"
        print(f"{t['id']}. {status} {t['title']}")

def complete_task(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            return True
    return False

def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]

def validate_task_title(title):
    return isinstance(title, str) and len(title.strip()) >= 3

def search_tasks(keyword):
    return [t for t in tasks if keyword in t["title"]]

def search_tasks_case_insensitive(keyword):
    return [t for t in tasks if keyword.lower() in t["title"].lower()]

if __name__ == "__main__":
    print(APP_TITLE)
    add_task("Изучить ветвление в Git")
    add_task("Оформить отчёт по ЛПР 4")
    complete_task(1)
    list_tasks()

def show_menu():
    print("\n--- Меню управления задачами ---")
    print("1. Список задач | 2. Добавить | 3. Выполнить | 4. Удалить | 5. Поиск")

def get_task_stats():
    total = len(tasks)
    completed = sum(1 for t in tasks if t["done"])
    return {"total": total, "completed": completed, "pending": total - completed}

def show_menu():
    print("\n--- Меню управления задачами ---")
    print("1. Список задач | 2. Добавить | 3. Выполнить | 4. Удалить | 5. Поиск")

def get_task_stats():
    total = len(tasks)
    completed = sum(1 for t in tasks if t["done"])
    return {"total": total, "completed": completed, "pending": total - completed}
