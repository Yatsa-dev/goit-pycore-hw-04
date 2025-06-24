import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def visualize_directory_structure(directory_path: Path, space: int = 0):

    prefix = "    " * space
    if not directory_path.exists():
        print(f"{prefix}{Fore.RED}Error: Path '{directory_path}' does not exist.{Style.RESET_ALL}")
        return
    if not directory_path.is_dir():
        print(f"{prefix}{Fore.RED}Error: '{directory_path}' is not a directory.{Style.RESET_ALL}")
        return

    try:
        for item in directory_path.iterdir():
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
                visualize_directory_structure(item, space + 1)
            elif item.is_file():
                print(f"{prefix}{Fore.GREEN}📄 {item.name}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{prefix}{Fore.RED}❌ An unexpected error occurred while processing '{directory_path.name}': {e}{Style.RESET_ALL}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Please provide the directory path as a command-line argument.{Style.RESET_ALL}")
        sys.exit(1)

    input_path = sys.argv[1]
    target_path = Path(input_path)

    if not target_path.exists():
        print(f"{Fore.RED}Error: Path '{input_path}' does not exist.{Style.RESET_ALL}")
        sys.exit(1)
    
    if not target_path.is_dir():
        print(f"{Fore.RED}Error: Path '{input_path}' is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    visualize_directory_structure(target_path)