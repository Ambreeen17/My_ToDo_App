# Feature Specification: Console Todo Foundation

**Feature Branch**: `001-console-todo-foundation`
**Created**: 2026-01-01
**Status**: Draft
**Input**: User description: "PHASE 1 — Console Todo Foundation: Build a pure, deterministic, console-based Todo system that manages todos via CLI with clean business rules, fully spec-driven, with zero UI or web assumptions."

**Parent Law**: Master Project Constitution (Immutable)

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create New Todo (Priority: P1)

User creates a new todo item via console command by providing a required title and optional description. The system assigns a unique deterministic ID, sets status to "Pending", and records creation timestamp.

**Why this priority**: Core functionality - without ability to create todos, system has no purpose. Establishes foundation for all other operations.

**Independent Test**: User can create a todo and see it appear in the list with unique ID, pending status, and timestamps.

**Acceptance Scenarios**:

1. **Given** system is running, **When** user provides valid title "Buy groceries" and description "Milk, eggs, bread", **Then** system creates todo with unique ID, status "Pending", title, description, and current timestamp
2. **Given** system is running, **When** user provides empty title, **Then** system rejects with clear error message "Title cannot be empty"
3. **Given** system is running, **When** user provides title only (no description), **Then** system creates todo with title and empty description

---

### User Story 2 - List All Todos (Priority: P1)

User views all todos in the system via console command. System displays each todo with its ID, title, description, status, and timestamps in a readable, formatted text format.

**Why this priority**: Critical for visibility - user must see all todos to manage them effectively. Primary interface for monitoring state.

**Independent Test**: User can list todos and see complete information for each todo item including ID, title, status, and timestamps.

**Acceptance Scenarios**:

1. **Given** system has 3 todos with mixed statuses, **When** user lists todos, **Then** system displays all 3 todos with full details (ID, title, description, status, timestamps)
2. **Given** system has no todos, **When** user lists todos, **Then** system displays "No todos found" message
3. **Given** system has completed todos, **When** user lists todos, **Then** completed todos appear with "Completed" status visible

---

### User Story 3 - Update Existing Todo (Priority: P2)

User updates an existing todo's title or description by providing todo ID and new values. System validates that todo exists, is not completed, and applies changes with updated timestamp.

**Why this priority**: Important for maintaining accuracy - users often need to correct titles or add details. Lower priority than core creation/listing.

**Independent Test**: User can update a pending todo's title or description and see changes reflected in list.

**Acceptance Scenarios**:

1. **Given** pending todo with ID "1" has title "Buy groceries", **When** user updates title to "Buy groceries and snacks", **Then** system updates title and updates "Updated" timestamp
2. **Given** pending todo with ID "1" has no description, **When** user adds description "Weekly shopping", **Then** system adds description and updates "Updated" timestamp
3. **Given** completed todo with ID "2", **When** user attempts to update title, **Then** system rejects with error "Cannot edit completed todos"
4. **Given** no todo with ID "999", **When** user attempts to update, **Then** system rejects with error "Todo not found"

---

### User Story 4 - Mark Todo as Completed (Priority: P2)

User marks a pending todo as completed by providing its ID. System updates status to "Completed" and records completion timestamp. Once completed, todo becomes immutable.

**Why this priority**: Essential for task completion workflow - users need to track progress. Lower priority than basic CRUD operations.

**Independent Test**: User can mark a pending todo as completed and see status change with completion timestamp.

**Acceptance Scenarios**:

1. **Given** pending todo with ID "1", **When** user marks as completed, **Then** system sets status to "Completed" and records completion timestamp
2. **Given** already completed todo with ID "2", **When** user attempts to mark as completed again, **Then** system either silently succeeds or shows "Todo already completed" message
3. **Given** no todo with ID "999", **When** user attempts to mark as completed, **Then** system rejects with error "Todo not found"

---

### User Story 5 - Delete Todo (Priority: P2)

User permanently removes a todo by providing its ID. System validates todo exists, removes it from repository, and confirms deletion. IDs are never reused.

**Why this priority**: Important for cleanup - users need to remove mistakes or obsolete todos. Lower priority as it's destructive and less frequent.

**Independent Test**: User can delete a todo and confirm it no longer appears in list with ID never reused.

**Acceptance Scenarios**:

1. **Given** todo with ID "1", **When** user deletes it, **Then** system removes todo from repository and shows "Todo deleted" message
2. **Given** deleted todo with ID "1", **When** user lists todos, **Then** todo "1" does not appear
3. **Given** no todo with ID "999", **When** user attempts to delete, **Then** system rejects with error "Todo not found"
4. **Given** todo with ID "1" deleted, **When** user creates new todo, **Then** system assigns next available ID (never "1")

---

### Edge Cases

- What happens when user provides invalid or non-numeric todo ID?
- How does system handle special characters in titles or descriptions?
- What happens when system state is corrupted or inconsistent?
- How does system handle concurrent commands from multiple sessions (if supported)?
- What happens when timestamps cannot be generated or validated?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST create todos with unique, deterministic IDs that are never reused
- **FR-002**: System MUST require non-empty title for todo creation
- **FR-003**: System MUST support optional description field (may be empty)
- **FR-004**: System MUST maintain todo status as either "Pending" or "Completed"
- **FR-005**: System MUST record creation timestamp when todo is created
- **FR-006**: System MUST record updated timestamp when todo is modified
- **FR-007**: System MUST allow listing all todos in human-readable text format
- **FR-008**: System MUST prevent editing completed todos (immutable after completion)
- **FR-009**: System MUST permanently delete todos (no undo/soft delete)
- **FR-010**: System MUST enforce all business rules via logic layer, not UI
- **FR-011**: System MUST provide clear, actionable error messages for invalid operations
- **FR-012**: System MUST be deterministic (same input produces same output)
- **FR-013**: System MUST follow three-tier architecture (CLI, business logic, data repository)

### Key Entities

- **Todo**: Core entity representing a task
  - Attributes: ID (unique, deterministic, never reused), Title (required, non-empty), Description (optional), Status (enum: Pending | Completed), CreatedTimestamp, UpdatedTimestamp
  - Immutable: Once status is "Completed", title and description cannot be modified
  - Lifecycle: Created → (Updated while Pending) → Completed → (No further modifications) or Deleted

- **TodoRepository**: Data tier component
  - Responsibility: In-memory storage and retrieval of todos
  - Operations: Create, Read (by ID or all), Update, Delete
  - Constraint: Must enforce business rules at repository level (no duplicate IDs, no editing completed todos)

- **TodoService**: Application tier component
  - Responsibility: Business logic, validation, and orchestration
  - Operations: Validates inputs, enforces rules, coordinates with repository, provides clean error messages

- **CLIInterface**: Presentation tier component
  - Responsibility: Parse console commands, invoke service layer, format output
  - Constraint: No business logic, must delegate all operations to service layer

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All CRUD operations (Create, Read, Update, Delete) execute correctly for valid inputs
- **SC-002**: System rejects 100% of invalid inputs with clear error messages
- **SC-003**: All business rules (5 immutable rules) are enforced by logic layer without exceptions
- **SC-004**: Unit tests achieve 100% code coverage for all public operations
- **SC-005**: No constitution rule is violated (verified by constitution compliance check)
- **SC-006**: System behaves deterministically (same input produces same output across multiple runs)
- **SC-007**: Three-tier architecture separation is maintained (no layer bypasses another)
- **SC-008**: IDs are never reused (verified across create/delete cycles)

## Constraints *(mandatory)*

### Out-of-Scope (STRICT)

- GUI or Web UI are explicitly forbidden
- Database persistence (file-based or remote) is forbidden
- Authentication and authorization are forbidden
- AI features or intelligent suggestions are forbidden
- Network calls or external API integrations are forbidden
- External libraries (except standard runtime library) are forbidden
- Color output, animations, or UI frameworks are forbidden
- Undo/redo functionality for delete operations is forbidden

### Architectural Constraints

- **AC-001**: Three-tier architecture MUST be enforced: Presentation (CLI), Application (Business Logic), Data (In-Memory Repository)
- **AC-002**: No layer may bypass another (CLI cannot directly access repository, repository cannot invoke business logic)
- **AC-003**: All business rules MUST be enforced in Application tier, not Presentation or Data tiers
- **AC-004**: System MUST use only standard runtime library (no external dependencies)
- **AC-005**: System MUST be spec-driven (no manual code generation or implementation without specification)

### Business Rules (IMMUTABLE AFTER LOCK)

- **BR-001**: Todo title cannot be empty
- **BR-002**: Completed todos cannot be edited (immutable once completed)
- **BR-003**: Deleted todos are permanently removed (no recovery)
- **BR-004**: IDs are never reused (strict monotonic assignment)
- **BR-005**: System behavior must be deterministic (no randomness or hidden state)

## Dependencies & Assumptions

### Dependencies

- Standard runtime library for console I/O, time operations, and data structures
- Command-line interface for user interaction
- In-memory data storage

### Assumptions

- User operates system through console/terminal
- Single-user, single-session operation (no concurrent access)
- System runs in environment with standard runtime library available
- Console supports UTF-8 or compatible encoding for text display

### External Dependencies

None (by design - console-only, in-memory system)

## Acceptance Checklist

Phase 1 is considered COMPLETE only if:

- [ ] All CRUD operations work correctly
- [ ] Invalid input is safely rejected with clear error messages
- [ ] All 5 business rules are enforced by logic, not UI
- [ ] Unit tests cover all operations (100% coverage)
- [ ] No constitution rule is violated
- [ ] Three-tier architecture separation is maintained
- [ ] System behavior is deterministic
- [ ] IDs are never reused
- [ ] Console output is human-readable and formatted
- [ ] No external libraries or frameworks used

## Notes

- This phase establishes absolute foundation. All future phases will extend this logic without modification.
- Completed todos become immutable - this is a core architectural decision supporting future phase extensibility.
- In-memory storage is intentional; persistence will be added in a future phase without modifying core business logic.
- Deterministic ID generation is critical for testability and future integrations (e.g., database persistence in Phase II).
