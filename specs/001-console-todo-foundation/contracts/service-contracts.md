# Service Contracts: Console Todo System

**Phase**: 1 - Console Todo Foundation
**Date**: 2026-01-01
**Status**: Draft
**Based On**: [data-model.md](./data-model.md), [spec.md](./spec.md)

## Interface Definitions

### ITodoRepository - Data Tier Contract

**Purpose**: In-memory storage and retrieval of Todo entities

**Operations**:

| Method | Input | Output | Business Rules | Exceptions |
|--------|-------|--------|---------------|------------|
| `create(todo: Todo) -> str` | Todo entity | Todo ID (deterministic) | BR-004: ID already exists |
| `read(id: str) -> Optional[Todo]` | Todo ID | Todo entity or None | None if not found |
| `read_all() -> list[Todo]` | None | All todos (empty list if none) | N/A |
| `update(id: str, title: Optional[str], description: Optional[str]) -> None` | ID, title, description | BR-002: Cannot edit completed todo | ValueError if not found or completed |
| `update_status(id: str, status: TodoStatus) -> None` | ID, status | BR-002: Cannot edit completed todo | ValueError if not found or invalid status |
| `delete(id: str) -> None` | Todo ID | BR-003: Permanently remove | ValueError if not found |
| `exists(id: str) -> bool` | Todo ID | N/A | N/A |

**Python Implementation**:

```python
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
```

---

### ITodoService - Application Tier Contract

**Purpose**: Business logic, validation, and orchestration for Todo operations

**Operations**:

| Method | Input | Output | Business Rules | Exceptions |
|--------|-------|--------|---------------|------------|
| `create_todo(title: str, description: Optional[str] = None) -> Todo` | Title, description | Todo entity with ID, status=Pending, timestamps | BR-001: Empty title |
| `list_todos() -> List[Todo]` | None | All todos | N/A |
| `update_todo(id: str, title: Optional[str] = None, description: Optional[str] = None) -> Todo` | ID, title, description | Updated Todo | BR-002: Cannot edit completed, not found |
| `complete_todo(id: str) -> Todo` | Todo ID | Todo with status=Completed | BR-002: Already completed, not found |
| `delete_todo(id: str) -> None` | Todo ID | N/A | BR-003: Permanently remove, not found |

**Python Implementation**:

```python
from abc import ABC, abstractmethod
from typing import Optional, List
from src.application.models.todo import Todo, TodoStatus
from src.infrastructure.repositories.itodo_repository import ITodoRepository
from datetime import datetime

class ITodoService(ABC):
    """Application tier interface for Todo business logic

    Business Rules (enforced by implementation):
    - BR-001: Title cannot be empty
    - BR-002: Completed todos cannot be edited
    - FR-005/FR-006: Auto-generate timestamps
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
```

---

### IIDGenerator - Utility Contract

**Purpose**: Generate unique, deterministic Todo IDs

**Operations**:

| Method | Input | Output | Business Rules | Exceptions |
|--------|-------|--------|---------------|------------|
| `next_id() -> str` | None | Unique ID string | BR-004: Never reuse IDs |

**Python Implementation**:

```python
from abc import ABC, abstractmethod

class IIDGenerator(ABC):
    """ID generator interface

    Business Rules (enforced by implementation):
    - BR-004: IDs are never reused (monotonic increment)
    - SC-006: Deterministic behavior (no randomness)
    """

    @abstractmethod
    def next_id(self) -> str:
        """Generate next unique ID

        Returns:
            str: Next ID (never reused)
        """
        pass
```

## Dependency Flow

### Three-Tier Architecture Flow

```
CLI Layer (Presentation)
    ↓ (parses commands, invokes services)
Application Layer (Business Logic)
    ↓ (validates, enforces rules, orchestrates)
Infrastructure Layer (Data Storage)
```

### Method Call Chain (Example: Create Todo)

```
CLI (command_parser.py)
    create_command(title, description)
        ↓
Service (todo_service.py)
    create_todo(title, description)
        ↓
        validate_title(title)           # Business Rule BR-001
        ↓
        generate_id()                  # BR-004 + FR-001
        ↓
        create_entity(title, description, id, timestamps)  # FR-005, FR-006
        ↓
Repository (in_memory_todo_repository.py)
    create(todo)
        ↓
        validate_id_unique(id)       # Business Rule BR-004
        ↓
        store_in_memory(todo)
```

## Error Handling Strategy

### Error Taxonomy

| Error Type | Use Case | Message Format | HTTP Status (Future Phase) |
|------------|-----------|----------------|--------------------------|
| `ValueError` | Invalid input (empty title, invalid ID) | "Error: {reason}" | 400 |
| `NotFoundError` | Todo not found | "Error: Todo not found" | 404 |
| `ImmutableError` | Attempting to edit completed todo | "Error: Cannot edit completed todos" | 403 |
| `DuplicateIdError` | Attempting to reuse ID | "Error: ID already exists" | 409 |

**Python Implementation**:

```python
class ImmutableError(ValueError):
    """Raised when attempting to edit a completed todo (BR-002)"""
    pass

class DuplicateIdError(ValueError):
    """Raised when attempting to reuse an ID (BR-004)"""
    pass

class NotFoundError(ValueError):
    """Raised when a todo is not found"""
    pass
```

## Testing Contracts

### Repository Contract Tests

```python
# tests/unit/repositories/test_itodo_repository.py

def test_create_returns_id():
    """Contract: create() must return non-empty ID string"""

def test_read_returns_todo_or_none():
    """Contract: read() must return Todo or None"""

def test_read_all_returns_list():
    """Contract: read_all() must return List[Todo]"""

def test_update_rejects_completed_todo():
    """Contract: update() must enforce BR-002"""

def test_delete_is_permanent():
    """Contract: delete() must not allow recovery (BR-003)"""

def test_exists_returns_bool():
    """Contract: exists() must return bool"""

def test_ids_never_reused():
    """Contract: IDs must never be reused (BR-004)"""
```

### Service Contract Tests

```python
# tests/unit/services/test_itodo_service.py

def test_create_todo_enforces_empty_title():
    """Contract: create_todo() must enforce BR-001"""

def test_create_todo_generates_timestamps():
    """Contract: create_todo() must auto-generate timestamps (FR-005, FR-006)"""

def test_update_todo_rejects_completed():
    """Contract: update_todo() must enforce BR-002"""

def test_complete_todo_is_idempotent():
    """Contract: complete_todo() must succeed if already completed"""

def test_delete_todo_is_permanent():
    """Contract: delete_todo() must enforce BR-003"""

def test_all_operations_are_deterministic():
    """Contract: Same inputs produce same outputs (SC-006, BR-005)"""
```

## Extension Points for Future Phases

### Phase II: Persistence Layer

```python
# Extend ITodoRepository with persistence methods

class IPersistableRepository(ITodoRepository):
    """Repository with persistence support"""

    @abstractmethod
    def save_to_file(self, filepath: str) -> None:
        """Save all todos to file"""
        pass

    @abstractmethod
    def load_from_file(self, filepath: str) -> None:
        """Load all todos from file"""
        pass
```

### Phase II: User Ownership

```python
# Extend ITodoService with user ownership

class IUserOwnedService(ITodoService):
    """Service with user ownership support"""

    @abstractmethod
    def create_todo_for_user(self, title: str, description: Optional[str],
                          user_id: str) -> Todo:
        """Create todo for specific user"""
        pass

    @abstractmethod
    def list_todos_for_user(self, user_id: str) -> List[Todo]:
        """List todos for specific user"""
        pass
```

## Notes

- All contracts enforce business rules from spec (BR-001 to BR-005)
- Three-tier separation enforced: CLI → Service → Repository (unidirectional)
- No layer bypass allowed (AC-002)
- Error messages are user-friendly and actionable (FR-011)
- All operations are deterministic (BR-005, SC-006)
