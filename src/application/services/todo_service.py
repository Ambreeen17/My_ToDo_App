from abc import ABC, abstractmethod
from typing import Optional, List
from datetime import datetime
from src.application.models.todo import Todo, TodoStatus
from src.infrastructure.repositories.itodo_repository import ITodoRepository
from src.infrastructure.repositories.in_memory_todo_repository import NotFoundError, ImmutableError


class ITodoService(ABC):
    """Application tier interface for Todo business logic

    Business Rules (enforced by implementation):
    - BR-001: Title cannot be empty
    - BR-002: Completed todos cannot be edited
    - FR-005: Auto-generate timestamps
    - FR-006: Auto-generate updated_timestamp
    - SC-006: Deterministic behavior (no randomness)
    """

    @abstractmethod
    def create_todo(self, title: str, description: Optional[str] = None) -> Todo:
        """Create a new todo with auto-generated ID and timestamps

        Business Rules:
        - BR-001: Title cannot be empty
        - FR-001: Unique, deterministic ID generation
        - FR-005: Auto-generate created_timestamp
        - FR-006: Auto-generate updated_timestamp

        Raises:
            ValueError: If title is empty
        """
        pass

    @abstractmethod
    def list_todos(self) -> List[Todo]:
        """List all todos

        Returns:
            List[Todo]: All todos (empty list if none)
        """
        pass

    @abstractmethod
    def update_todo(self, id: str, title: Optional[str] = None,
                  description: Optional[str] = None) -> Todo:
        """Update todo title and/or description

        Business Rules:
        - BR-002: Cannot edit completed todos (immutable)

        Raises:
            ValueError: If todo not found or status is Completed
        """
        pass

    @abstractmethod
    def complete_todo(self, id: str) -> Todo:
        """Mark todo as completed

        Business Rules:
        - BR-002: Cannot edit completed todos (idempotent if already completed)

        Raises:
            ValueError: If todo not found
        """
        pass

    @abstractmethod
    def delete_todo(self, id: str) -> None:
        """Delete a todo

        Business Rules:
        - BR-003: Deleted todos are permanently removed

        Raises:
            ValueError: If todo not found
        """
        pass


class TodoService(ITodoService):
    """Business logic and validation for Todo operations"""

    def __init__(self, repository: ITodoRepository, id_generator):
        """
        Initialize service with dependencies

        Args:
            repository: Data tier for storage/retrieval
            id_generator: Component for generating unique IDs
        """
        self._repository = repository
        self._id_generator = id_generator

    def create_todo(self, title: str, description: Optional[str] = None) -> Todo:
        """Create a new todo with auto-generated ID and timestamps

        Business Rules:
        - BR-001: Title cannot be empty
        - FR-001: Unique, deterministic ID generation
        - FR-005: Auto-generate created_timestamp
        - FR-006: Auto-generate updated_timestamp

        Raises:
            ValueError: If title is empty (BR-001)
        """
        # BR-001: Title cannot be empty
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        # FR-001: Generate unique, deterministic ID
        id = self._id_generator.next_id()

        # FR-005: Auto-generate created_timestamp
        created_timestamp = datetime.now()

        # FR-006: Auto-generate updated_timestamp
        updated_timestamp = created_timestamp

        # Create todo entity
        todo = Todo(
            id=id,
            title=title,
            description=description,
            status=TodoStatus.PENDING,
            created_timestamp=created_timestamp,
            updated_timestamp=updated_timestamp
        )

        # Store in repository
        stored_id = self._repository.create(todo)

        return todo

    def list_todos(self) -> List[Todo]:
        """List all todos

        Returns:
            List[Todo]: All todos (empty list if none)
        """
        return self._repository.read_all()

    def update_todo(self, id: str, title: Optional[str] = None,
                  description: Optional[str] = None) -> Todo:
        """Update todo title and/or description

        Business Rules:
        - BR-002: Cannot edit completed todos (immutable)

        Raises:
            NotFoundError: If todo not found (FR-011)
            ImmutableError: If status is Completed (BR-002)
        """
        # Read todo
        todo = self._repository.read(id)
        if not todo:
            raise NotFoundError(f"Todo not found: {id}")

        # BR-002: Cannot edit completed todos
        if not todo.can_edit():
            raise ImmutableError("Cannot edit completed todos")

        # Update fields
        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description

        # FR-006: Auto-generate updated_timestamp
        todo.updated_timestamp = datetime.now()

        # Store updated todo
        self._repository.update(id, title, description)

        return todo

    def complete_todo(self, id: str) -> Todo:
        """Mark todo as completed

        Business Rules:
        - BR-002: Cannot edit completed todos (idempotent if already completed)

        Raises:
            NotFoundError: If todo not found (FR-011)
        """
        # Read todo
        todo = self._repository.read(id)
        if not todo:
            raise NotFoundError(f"Todo not found: {id}")

        # BR-002: Idempotent - if already completed, succeed silently
        if todo.status == TodoStatus.COMPLETED:
            return todo

        # Update status
        self._repository.update_status(id, TodoStatus.COMPLETED)

        # Return updated todo
        todo = self._repository.read(id)
        return todo

    def delete_todo(self, id: str) -> None:
        """Delete a todo

        Business Rules:
        - BR-003: Deleted todos are permanently removed

        Raises:
            NotFoundError: If todo not found (FR-011)
        """
        self._repository.delete(id)
