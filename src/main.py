from colorama import init, Fore, Style

init(autoreset=True)

APP_TITLE = "=== PYTHON TASK MANAGER v2.0 | Система управления задачами ==="
tasks = []

def show_header():
    print(Fore.CYAN + Style.BRIGHT + APP_TITLE)

def add_task(title, priority="Средний"):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    print(Fore.GREEN + f"[+] Задача '{title}' (приоритет: {priority}) успешно добавлена.")
    return task

def list_tasks():
    if not tasks:
        print(Fore.YELLOW + "Список задач пуст.")
        return
    for t in tasks:
        status = Fore.GREEN + "Выполнена" if t["completed"] else Fore.RED + "В работе"
        print(f"#{t['id']} [{t['priority']}] {t['title']} — {status}")

def complete_task(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            print(Fore.GREEN + f"[v] Задача #{task_id} отмечена как выполненная.")
            return True
    print(Fore.RED + f"[!] Задача #{task_id} не найдена.")
    return False

def delete_task(task_id):
    global tasks
    initial_len = len(tasks)
    tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) < initial_len:
        print(Fore.YELLOW + f"[-] Задача #{task_id} удалена.")
        return True
    return False

def search_tasks(keyword):
    return [t for t in tasks if keyword.lower() in t["title"].lower()]

def get_statistics():
    total = len(tasks)
    done = sum(1 for t in tasks if t["completed"])
    return {"total": total, "completed": done, "pending": total - done}

if __name__ == "__main__":
    show_header()
    add_task("Разрешить конфликт слияния в Git", "Высокий")
    add_task("Оформить документацию README.md", "Высокий")
    add_task("Проверить окружение requirements.txt", "Средний")
    complete_task(1)
    list_tasks()
    stats = get_statistics()
    print(Fore.CYAN + f"Итого задач: {stats['total']} | Выполнено: {stats['completed']} | В работе: {stats['pending']}")
