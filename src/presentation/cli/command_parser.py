import argparse
import sys
from typing import Optional, Tuple
from src.application.services.todo_service import TodoService
from src.infrastructure.repositories.in_memory_todo_repository import InMemoryTodoRepository
from src.application.services.id_generator import IIDGenerator, InMemoryIDGenerator


def create_parser() -> argparse.ArgumentParser:
    """Create and return CLI argument parser

    Returns:
        argparse.ArgumentParser: Configured parser
    """
    parser = argparse.ArgumentParser(
        description="Console Todo System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py create "Buy groceries" --description "Milk, eggs, bread"
  python main.py list
  python main.py update 1 --title "Buy groceries and snacks"
  python main.py complete 1
  python main.py delete 1
        """
    )

    # Create subparsers for commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # create command
    create_parser = subparsers.add_parser("create", help="Create a new todo")
    create_parser.add_argument("title", help="Todo title")
    create_parser.add_argument("--description", help="Optional description")

    # list command
    list_parser = subparsers.add_parser("list", help="List all todos")

    # update command
    update_parser = subparsers.add_parser("update", help="Update a todo")
    update_parser.add_argument("id", help="Todo ID to update")
    update_parser.add_argument("--title", help="New title")
    update_parser.add_argument("--description", help="New description")

    # complete command
    complete_parser = subparsers.add_parser("complete", help="Mark todo as completed")
    complete_parser.add_argument("id", help="Todo ID to complete")

    # delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a todo")
    delete_parser.add_argument("id", help="Todo ID to delete")

    return parser


def handle_error(error: str) -> None:
    """Print user-friendly error message to stderr and exit

    Args:
        error: Error message to display

    Returns:
        None (program exits)
    """
    print(f"Error: {error}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    """Main CLI entry point

    Parses commands and delegates to TodoService
    """
    # Initialize dependencies
    repository = InMemoryTodoRepository()
    id_generator = InMemoryIDGenerator()
    service = TodoService(repository, id_generator)

    # Create parser and parse arguments
    parser = create_parser()
    args = parser.parse_args()

    # Delegate to service based on command
    try:
        if args.command == "create":
            todo = service.create_todo(args.title, args.description)
            print("Todo created successfully")
            print(f"[{todo.id}] {todo.title}")
            if todo.description:
                print(f"    Description: {todo.description}")
            print(f"    Status: {todo.status.value}")
            print(f"    Created: {todo.created_timestamp}")

        elif args.command == "list":
            todos = service.list_todos()
            if not todos:
                print("No todos found")
            else:
                for todo in todos:
                    status_marker = "X" if todo.status.value == "Completed" else "O"
                    print(f"{status_marker} [{todo.id}] {todo.title}")
                    if todo.description:
                        print(f"    Description: {todo.description}")
                    print(f"    Status: {todo.status.value}")
                    print(f"    Created: {todo.created_timestamp}")

        elif args.command == "update":
            todo = service.update_todo(args.id, args.title, args.description)
            print("Todo updated successfully")
            print(f"[{todo.id}] {todo.title}")
            if todo.description:
                print(f"    Description: {todo.description}")
            print(f"    Status: {todo.status.value}")
            print(f"    Updated: {todo.updated_timestamp}")

        elif args.command == "complete":
            todo = service.complete_todo(args.id)
            print("Todo completed successfully")
            print(f"[{todo.id}] {todo.title}")
            if todo.description:
                print(f"    Description: {todo.description}")
            print(f"    Status: {todo.status.value}")
            print(f"    Created: {todo.created_timestamp}")
            print(f"    Updated: {todo.updated_timestamp}")

        elif args.command == "delete":
            service.delete_todo(args.id)
            print("Todo deleted successfully")

        else:
            print("Error: No command specified", file=sys.stderr)
            sys.exit(1)

    except ValueError as e:
        handle_error(str(e))
    except Exception as e:
        handle_error(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    main()
