# Tasks: Console Todo Foundation

**Input**: Design documents from `/specs/001-console-todo-foundation/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- **Paths shown below assume single project** - adjust based on plan.md structure

---
## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project directory structure per implementation plan
- [ ] T002 Create virtual environment and install development dependencies (pytest, pytest-cov, coverage)
- [ ] T003 [P] Create pytest.ini configuration file with coverage settings
- [ ] T004 [P] Create main.py entry point with basic CLI structure
- [ ] T005 Create requirements-dev.txt file

**Checkpoint**: Setup complete - ready for foundational work

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 Create TodoStatus enum in src/application/models/todo.py
- [ ] T007 Create Todo dataclass with validation in src/application/models/todo.py
- [ ] T008 Create IIDGenerator interface and InMemoryIDGenerator in src/application/services/id_generator.py
- [ ] T009 Create ITodoRepository interface in src/infrastructure/repositories/itodo_repository.py
- [ ] T010 Implement InMemoryTodoRepository in src/infrastructure/repositories/in_memory_todo_repository.py
- [ ] T011 Create ITodoService interface in src/application/services/itodo_service.py
- [ ] T012 Create TodoService with business logic in src/application/services/todo_service.py
- [ ] T013 Create CLI command parser in src/presentation/cli/command_parser.py
- [ ] T014 Create output formatter in src/presentation/cli/output_formatter.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create New Todo & List All Todos (Priority: P1) 🎯 MVP

**Goal**: Implement core CRUD operations (create and list) to establish basic functionality

**Independent Test**: User can create todos and list all todos with unique IDs and timestamps

### Implementation for User Story 1

- [ ] T015 [US1] Implement create command in src/presentation/cli/command_parser.py
- [ ] T016 [US1] Implement list command in src/presentation/cli/command_parser.py
- [ ] T017 [US1] Wire create command to TodoService in src/presentation/cli/command_parser.py
- [ ] T018 [US1] Wire list command to TodoService in src/presentation/cli/command_parser.py
- [ ] T019 [US1] Implement output formatting for single todo in src/presentation/cli/output_formatter.py
- [ ] T020 [US1] Implement output formatting for todo list in src/presentation/cli/output_formatter.py
- [ ] T021 [US1] Add error handling for empty title in TodoService.create_todo (BR-001)
- [ ] T022 [US1] Ensure unique ID generation in InMemoryIDGenerator.next_id (BR-004, FR-001)

**Checkpoint**: At this point, User Story 1 (Create & List) should be fully functional

---

## Phase 4: User Story 3 - Update Existing Todo (Priority: P2)

**Goal**: Enable users to modify pending todo titles and descriptions

**Independent Test**: User can update pending todos and see changes reflected

### Implementation for User Story 3

- [ ] T023 [P] [US3] Implement update command in src/presentation/cli/command_parser.py
- [ ] T024 [US3] Wire update command to TodoService in src/presentation/cli/command_parser.py
- [ ] T025 [US3] Add validation to prevent editing completed todos in TodoService.update_todo (BR-002)
- [ ] T026 [US3] Add Todo not found error handling in TodoService.update_todo (FR-011)

**Checkpoint**: At this point, User Stories 1 AND 3 should both work independently

---

## Phase 5: User Story 4 - Mark Todo as Completed (Priority: P2)

**Goal**: Enable users to mark todos as completed (immutable after completion)

**Independent Test**: User can mark pending todos as completed and see status change

### Implementation for User Story 4

- [ ] T027 [P] [US4] Implement complete command in src/presentation/cli/command_parser.py
- [ ] T028 [US4] Wire complete command to TodoService in src/presentation/cli/command_parser.py
- [ ] T029 [US4] Add Todo not found error handling in TodoService.complete_todo (FR-011)
- [ ] T030 [US4] Ensure idempotent completion (succeed if already completed) in TodoService.complete_todo

**Checkpoint**: At this point, User Stories 1, 3, AND 4 should all work independently

---

## Phase 6: User Story 5 - Delete Todo (Priority: P2)

**Goal**: Enable users to permanently remove todos (IDs never reused)

**Independent Test**: User can delete todos and confirm IDs are never reused

### Implementation for User Story 5

- [ ] T031 [P] [US5] Implement delete command in src/presentation/cli/command_parser.py
- [ ] T032 [US5] Wire delete command to TodoService in src/presentation/cli/command_parser.py
- [ ] T033 [US5] Add Todo not found error handling in TodoService.delete_todo (FR-011)
- [ ] T034 [US5] Ensure permanent deletion (no soft delete) in InMemoryTodoRepository.delete (BR-003)

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T035 [P] Add README.md with quickstart instructions
- [ ] T036 [P] Verify no external runtime dependencies (AC-004 compliance)
- [ ] T037 [P] Verify no colors/animations in CLI output (out-of-scope check)
- [ ] T038 Add UTF-8 encoding support for cross-platform compatibility in main.py
- [ ] T039 [P] Ensure deterministic behavior across multiple runs (BR-005, SC-006)
- [ ] T040 Verify three-tier architecture separation (no layer bypasses)
- [ ] T041 [P] Validate all business rules enforced in Application tier
- [ ] T042 Run quickstart.md validation steps

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P2 → P2)
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US3 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US3/US4 but should be independently testable

### Within Each User Story

- Models before services
- Services before CLI commands
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T003, T004, T005)
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Tasks T015-T020 (US1 implementation) can run in parallel
- Tasks T023, T027, T031 (CLI commands for US3, US4, US5) can run in parallel
- All Polish tasks marked [P] can run in parallel

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Create & List)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 3 → Test independently → Deploy/Demo
4. Add User Story 4 → Test independently → Deploy/Demo
5. Add User Story 5 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Create & List)
   - Developer B: User Story 3 (Update)
   - Developer C: User Story 4 (Complete)
   - Developer D: User Story 5 (Delete)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Tasks are reusable templates for future phases
- All business rules (BR-001 to BR-005) must be enforced
- Constitution compliance (AC-001 to AC-005) must be maintained
- No external runtime dependencies allowed (AC-004)
- Three-tier architecture must be enforced (no layer bypasses)
