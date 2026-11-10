from colorama import init, Fore, Style
init(autoreset=True)

APP_TITLE = "=== СИСТЕМА УПРАВЛЕНИЯ ЗАДАЧАМИ (Main Release) ==="

def show_header():
    print(Fore.CYAN + Style.BRIGHT + APP_TITLE)
