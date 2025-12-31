from abc import ABC, abstractmethod
from typing import Optional, List
from src.application.models.todo import Todo, TodoStatus


class ITodoRepository(ABC):
    """Data tier interface for Todo storage

    Business Rules (enforced by implementation):
    - BR-003: Deleted todos are permanently removed (no soft delete)
    - BR-004: IDs are never reused
    """

    @abstractmethod
    def create(self, todo: Todo) -> str:
        """Create a new todo and return its ID

        Raises:
            ValueError: If ID already exists (BR-004)
        """
        pass

    @abstractmethod
    def read(self, id: str) -> Optional[Todo]:
        """Read a todo by ID

        Returns:
            Todo: If found
            None: If not found
        """
        pass

    @abstractmethod
    def read_all(self) -> List[Todo]:
        """Read all todos

        Returns:
            List[Todo]: All todos (empty list if none)
        """
        pass

    @abstractmethod
    def update(self, id: str, title: Optional[str] = None,
              description: Optional[str] = None) -> None:
        """Update todo title and/or description

        Business Rules:
        - BR-002: Cannot edit completed todos

        Raises:
            ValueError: If todo not found or status is Completed
        """
        pass

    @abstractmethod
    def update_status(self, id: str, status: TodoStatus) -> None:
        """Update todo status

        Raises:
            ValueError: If todo not found
        """
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        """Delete a todo

        Business Rules:
        - BR-003: Deleted todos are permanently removed

        Raises:
            ValueError: If todo not found
        """
        pass

    @abstractmethod
    def exists(self, id: str) -> bool:
        """Check if todo exists

        Returns:
            bool: True if exists, False otherwise
        """
        pass
