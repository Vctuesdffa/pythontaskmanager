from colorama import init, Fore, Style
init(autoreset=True)

APP_TITLE = "=== PYTHON TASK MANAGER v2.0 | Система управления задачами ==="

def show_header():
    print(Fore.CYAN + Style.BRIGHT + APP_TITLE)
