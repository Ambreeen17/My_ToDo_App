from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum


class TodoStatus(Enum):
    """Todo status enum - mutually exclusive states"""
    PENDING = "Pending"
    COMPLETED = "Completed"


@dataclass
class Todo:
    """Core entity representing a task

    Business Rules (from spec BR-001 to BR-005):
    - BR-001: Title cannot be empty
    - BR-002: Completed todos cannot be edited
    - BR-003: Deleted todos are permanently removed
    - BR-004: IDs are never reused
    - BR-005: System behavior must be deterministic
    """

    id: str  # Unique, deterministic, never reused (BR-004)
    title: str  # Required, non-empty (BR-001, FR-002)
    description: Optional[str]  # Optional (FR-003)
    status: TodoStatus  # Enum: Pending | Completed (FR-004)
    created_timestamp: datetime  # Auto-generated (FR-005)
    updated_timestamp: datetime  # Auto-generated on modification (FR-006)

    def __post_init__(self):
        """Validate business rules after initialization"""
        # BR-001: Title cannot be empty
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty")

        # FR-004: Status must be valid enum value
        if not isinstance(self.status, TodoStatus):
            raise ValueError(f"Invalid status: {self.status}")

        # FR-005: created_timestamp must be set
        if not self.created_timestamp:
            raise ValueError("created_timestamp is required")

        # FR-006: updated_timestamp must be set
        if not self.updated_timestamp:
            raise ValueError("updated_timestamp is required")

    def can_edit(self) -> bool:
        """Check if todo can be edited (BR-002)"""
        return self.status == TodoStatus.PENDING

    def is_completed(self) -> bool:
        """Check if todo is completed"""
        return self.status == TodoStatus.COMPLETED
