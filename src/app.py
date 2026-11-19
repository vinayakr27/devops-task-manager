from config import APP_NAME
from database import get_tasks

def main():
    print(f"Welcome to {APP_NAME}")

    tasks = get_tasks()

    print("\nAvailable Tasks:")
    for task in tasks:
        print(f"- {task}")

if __name__ == "__main__":
    main()
