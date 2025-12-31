from typing import Optional, List, Dict
from datetime import datetime
from src.infrastructure.repositories.itodo_repository import ITodoRepository
from src.application.models.todo import Todo, TodoStatus
from src.application.services.id_generator import IIDGenerator, InMemoryIDGenerator
import sys


class DuplicateIdError(ValueError):
    """Raised when attempting to reuse an ID (BR-004)"""
    pass


class NotFoundError(ValueError):
    """Raised when a todo is not found"""
    pass


class ImmutableError(ValueError):
    """Raised when attempting to edit a completed todo (BR-002)"""
    pass


class InMemoryTodoRepository(ITodoRepository):
    """In-memory storage and retrieval of Todo entities

    Implementation enforces:
    - BR-003: Deleted todos are permanently removed (no soft delete)
    - BR-004: IDs are never reused (monotonic increment)
    """

    def __init__(self, id_generator: Optional[IIDGenerator] = None):
        self._todos: Dict[str, Todo] = {}
        self._id_generator = id_generator or InMemoryIDGenerator()

    def create(self, todo: Todo) -> str:
        """Create a new todo and return its ID

        Raises:
            DuplicateIdError: If ID already exists (BR-004)
        """
        # Check if ID already exists (BR-004)
        if self._todos.get(todo.id):
            raise DuplicateIdError(f"ID already exists: {todo.id}")

        # Store todo
        self._todos[todo.id] = todo
        return todo.id

    def read(self, id: str) -> Optional[Todo]:
        """Read a todo by ID

        Returns:
            Todo: If found
            None: If not found
        """
        return self._todos.get(id)

    def read_all(self) -> List[Todo]:
        """Read all todos

        Returns:
            List[Todo]: All todos (empty list if none)
        """
        return list(self._todos.values())

    def update(self, id: str, title: Optional[str] = None,
              description: Optional[str] = None) -> None:
        """Update todo title and/or description

        Business Rules:
        - BR-002: Cannot edit completed todos

        Raises:
            NotFoundError: If todo not found
            ImmutableError: If status is Completed
        """
        # Check if todo exists
        todo = self._todos.get(id)
        if not todo:
            raise NotFoundError(f"Todo not found: {id}")

        # BR-002: Cannot edit completed todos
        if todo.status == TodoStatus.COMPLETED:
            raise ImmutableError("Cannot edit completed todos")

        # Update fields
        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description
        todo.updated_timestamp = datetime.now()

    def update_status(self, id: str, status: TodoStatus) -> None:
        """Update todo status

        Raises:
            NotFoundError: If todo not found
        """
        # Check if todo exists
        todo = self._todos.get(id)
        if not todo:
            raise NotFoundError(f"Todo not found: {id}")

        # Update status
        todo.status = status
        todo.updated_timestamp = datetime.now()

    def delete(self, id: str) -> None:
        """Delete a todo

        Business Rules:
        - BR-003: Deleted todos are permanently removed

        Raises:
            NotFoundError: If todo not found
        """
        # Check if todo exists
        if id not in self._todos:
            raise NotFoundError(f"Todo not found: {id}")

        # BR-003: Permanently remove (no soft delete)
        del self._todos[id]

    def exists(self, id: str) -> bool:
        """Check if todo exists

        Returns:
            bool: True if exists, False otherwise
        """
        return id in self._todos
