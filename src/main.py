from colorama import init, Fore, Style
init(autoreset=True)

APP_TITLE = "=== PYTHON TASK MANAGER v2.0 (Feature Edition) ==="

def show_header():
    print(Fore.CYAN + Style.BRIGHT + APP_TITLE)
