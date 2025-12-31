"""Output formatter for console display

Provides human-readable formatted output for Todo entities
"""
import sys
from typing import List
from src.application.models.todo import Todo, TodoStatus


def format_todo(todo: Todo) -> str:
    """Format single todo for console output

    Args:
        todo: Todo entity to format

    Returns:
        str: Formatted todo string
    """
    status_marker = "✓" if todo.status == TodoStatus.COMPLETED else "○"

    result = f"{status_marker} [{todo.id}] {todo.title}"

    if todo.description:
        result += f"\n    Description: {todo.description}"
    else:
        result += "\n    Description: (None)"

    result += f"\n    Status: {todo.status.value}"
    result += f"\n    Created: {todo.created_timestamp}"

    return result


def format_todo_list(todos: List[Todo]) -> str:
    """Format multiple todos for console output

    Args:
        todos: List of Todo entities

    Returns:
        str: Formatted list string or "No todos found" message
    """
    if not todos:
        return "No todos found"

    lines = []
    for todo in todos:
        lines.append(format_todo(todo))

    return "\n\n".join(lines)


def format_error(error: str) -> str:
    """Print user-friendly error message to stderr

    Args:
        error: Error message to display
    """
    print(f"Error: {error}", file=sys.stderr)


def print_success(message: str) -> None:
    """Print success message to stdout

    Args:
        message: Success message to display
    """
    print(f"✓ {message}")
