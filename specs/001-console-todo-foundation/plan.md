# Implementation Plan: Console Todo Foundation

**Branch**: `001-console-todo-foundation` | **Date**: 2026-01-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-console-todo-foundation/spec.md`

**Note**: This plan translates Phase 1 specification into ordered, agent-driven execution strategy following constitution principles.

## Summary

Build a pure, deterministic, console-based Todo system following strict three-tier architecture. System manages todos via CLI with immutable business rules enforced in Application tier. Foundation for future phases with no external dependencies, in-memory storage, and 100% test coverage required.

## Technical Context

**Language/Version**: Python 3.11+ (LTS support until 2027)
**Primary Dependencies**: pytest 7.x, coverage.py 7.x (development only - no runtime dependencies per AC-004)
**Storage**: In-memory repository (Python `collections` module - Phase 1, extendable to persistent storage)
**Testing**: pytest 7.x + coverage.py 7.x (100% coverage target with HTML reports)
**Target Platform**: Cross-platform (Windows, Linux, macOS) - UTF-8 encoding via Python 3+ stdlib
**Project Type**: Single project (console application)
**Performance Goals**: <100ms operation response time (deterministic behavior - SC-006)
**Constraints**: Single-user, single-session (spec assumption), no external runtime libraries (AC-004), no colors/animations (out-of-scope)
**Scale/Scope**: In-memory (10k+ todos supported by standard collections)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Pre-Design Evaluation

- ✅ **Spec-Driven Development**: Specification created and approved before implementation (Constitution Principle 1)
- ✅ **Constitution Before Specification**: Constitution ratified (v1.0.0) before Phase 1 spec (Constitution Principle 2)
- ✅ **Specification Before Code**: Plan generation precedes implementation (Constitution Principle 3)
- ✅ **Manual Coding Prohibited**: All implementation delegated to Claude Code (Constitution Principle 4)
- ✅ **Three-Tier Architecture**: Enforced in Technical Context (Constitution Principle 4, AC-001)
- ✅ **Phase Evolution**: Phase 1 defined as foundation with additive evolution (Constitution Principle 6)
- ✅ **No External Dependencies**: Standard library only (Constitution Principle 8, AC-004)
- ✅ **UI Quality**: Console output must be human-readable and formatted (Constitution Principle 11)
- ✅ **Security**: No data integrity violations, no insecure shortcuts (Constitution Principle 12)
- ✅ **Phase Locking**: Business rules will become immutable after lock (Constitution Principle 8, Phase 1 Section 8)

**Status**: ✅ PASSED - Ready for Phase 0 research

---

## Project Structure

### Documentation (this feature)

```text
specs/001-console-todo-foundation/
├── spec.md               # Feature specification (completed)
├── plan.md               # This file (current)
├── research.md           # Phase 0 output (to be generated)
├── data-model.md         # Phase 1 output (to be generated)
├── quickstart.md         # Phase 1 output (to be generated)
├── contracts/            # Phase 1 output (to be generated)
│   └── service-contracts.md
└── checklists/
    └── requirements.md  # Spec quality checklist (completed)
```

### Source Code (repository root)

```text
src/
├── presentation/
│   └── cli/
│       ├── command_parser.py    # CLI command parsing
│       └── output_formatter.py  # Console output formatting
├── application/
│   ├── services/
│   │   ├── todo_service.py   # Business logic and validation
│   │   └── id_generator.py   # Deterministic ID generation
│   └── models/
│       └── todo.py           # Todo entity definition
└── infrastructure/
    └── repositories/
        └── in_memory_todo_repository.py  # In-memory storage

tests/
├── unit/
│   ├── models/
│   │   └── test_todo.py
│   ├── services/
│   │   ├── test_todo_service.py
│   │   └── test_id_generator.py
│   └── repositories/
│       └── test_in_memory_todo_repository.py
└── integration/
    └── test_cli_workflows.py

main.py                   # CLI entry point
```

**Structure Decision**: Single project structure chosen with explicit three-tier separation. Presentation tier (CLI) delegates to Application tier (Services/Models), which coordinates with Infrastructure tier (Repository). This enforces AC-002 and ensures no layer bypass violations.

## Complexity Tracking

> No constitution violations present - no complexity tracking required

## Agent Execution Sequence

### STEP 0 — SPEC VALIDATION (BLOCKING)

**Responsible Agent**: SystemGovernorAgent

**Actions**:
- ✅ Verify constitution compliance (PASSED - see Constitution Check above)
- ✅ Verify Phase 1 /sp.specify completeness (PASSED - all mandatory sections completed)
- ✅ Freeze scope boundaries (enforced: out-of-scope items clearly defined)

**Exit Condition**: ✅ Spec approved - proceed to Step 1

---

### STEP 1 — SPEC REFINEMENT

**Responsible Agent**: SpecAuthorAgent

**Subagents**:
- RequirementClarifierSubagent
- EdgeCaseIdentifierSubagent

**Actions**:
- Review spec for remaining ambiguities (5 edge cases identified in spec.md:94-100)
- Normalize terminology (ensure consistent use of "todo", "ID", "status", etc.)
- Finalize acceptance criteria (all 8 success criteria defined and measurable)

**Outputs**: Refined internal spec (no scope changes - spec approved)

**Status**: ✅ COMPLETE - spec passed quality validation (checklists/requirements.md)

---

### STEP 2 — ARCHITECTURE DESIGN

**Responsible Agent**: ArchitectureAgent

**Subagents**:
- BackendArchitectureSubagent
- DataArchitectureSubagent

**Actions**:
- Enforce three-tier architecture (Presentation → Application → Infrastructure)
- Define module boundaries (clear separation: cli/, services/, models/, repositories/)
- Select patterns: Repository Pattern (in-memory implementation), Service Layer (business logic)

**Outputs**:
- Architecture blueprint (defined in Project Structure above)
- Dependency flow: CLI → TodoService → TodoRepository (unidirectional, no circular dependencies)

**Status**: ✅ COMPLETE - three-tier architecture enforced, module boundaries defined

---

### STEP 3 — DOMAIN & BUSINESS LOGIC

**Responsible Agent**: BusinessLogicAgent

**Subagents**:
- DomainModelSubagent
- ValidationSubagent
- WorkflowSubagent

**Actions**:
- Define Todo entity (attributes: ID, Title, Description, Status, CreatedTimestamp, UpdatedTimestamp)
- Encode business rules (5 immutable rules: BR-001 to BR-005)
- Define workflows for CRUD (Create, Read, Update, Complete, Delete)

**Outputs**:
- Domain model (Todo entity with validation)
- Service contracts (ITodoRepository, ITodoService interfaces)

**Status**: ⏳ PENDING - To be generated in Phase 1 (data-model.md, contracts/)

---

### STEP 4 — PRESENTATION (CLI)

**Responsible Agent**: BusinessLogicAgent

**Subagent**: WorkflowSubagent

**Actions**:
- Define CLI commands (create, list, update, complete, delete)
- Map commands to services (CLI → TodoService methods)
- Handle input/output formatting (human-readable text, error messages)

**Outputs**:
- CLI interaction flow (command parser, output formatter)

**Status**: ⏳ PENDING - To be generated in Phase 1 (quickstart.md)

---

### STEP 5 — TESTING & QUALITY

**Responsible Agent**: QualityAssuranceAgent

**Subagents**: UnitTestSubagent

**Actions**:
- Write unit tests for all operations (TodoService, TodoRepository, IDGenerator, CLI workflows)
- Validate edge cases (5 edge cases from spec.md:94-100)
- Ensure deterministic behavior (same input produces same output)

**Outputs**:
- Test suite (unit tests for models, services, repositories)
- Coverage report (target: 100% for all public operations - SC-004)

**Status**: ⏳ PENDING - To be generated in Phase 1

---

### STEP 6 — CODE GENERATION

**Responsible Agent**: Claude Code

**Input**:
- Locked specs (spec.md - immutable after Phase 0 validation)
- Architecture blueprint (plan.md - Project Structure)
- Test requirements (100% coverage, deterministic behavior)

**Actions**:
- Generate full implementation (src/ structure with three tiers)
- Generate tests (tests/ with unit and integration tests)
- Generate run instructions (quickstart.md)

**Outputs**:
- Runnable console application (main.py with CLI interface)
- Test suite (100% coverage of public operations)
- Quickstart guide (step-by-step execution instructions)

**Status**: ⏳ PENDING - To be executed after Phase 1 design complete

---

### STEP 7 — PHASE VALIDATION

**Responsible Agent**: SystemGovernorAgent

**Actions**:
- Validate acceptance criteria (SC-001 to SC-008 all met)
- Validate test pass status (100% coverage, all tests passing)
- Verify no forbidden features exist (no GUI, no persistence, no external libs)

**Exit Condition**:
- Phase approved (all criteria met) OR rejected (violations found)

**Status**: ⏳ PENDING - To be executed after code generation

---

### STEP 8 — PHASE LOCKING

**Responsible Agent**: SystemGovernorAgent

**Actions**:
- Lock entity definitions (Todo entity structure becomes immutable)
- Lock business rules (5 business rules become immutable after Phase 1 lock)
- Mark Phase 1 immutable (cannot be modified by future phases)

**Result**: Phase 1 becomes permanent foundation

**Status**: ⏳ PENDING - To be executed after Phase 7 validation passes

---

## Parallelization Rules

- **Steps 3 & 4** may partially overlap (domain model and CLI workflows can be designed in parallel)
- **No overlap allowed** with Step 0 (blocking validation) or Step 8 (final locking)
- **Conflicts resolved** by SystemGovernorAgent (constitution compliance check)

---

## Failure & Resume Plan

If interrupted:

- **Resume from last completed step** (document step completion status in plan.md)
- **Reload specs** (spec.md is immutable - always valid)
- **Regenerate code if needed** (Claude Code can regenerate from locked specs)

**No manual fixes allowed** (Constitution Principle 9 - Failure & Recovery Rule)

---

## Deliverable Checklist

- [x] Spec validated (Constitution Check PASSED)
- [x] Architecture defined (three-tier blueprint complete)
- [ ] Business rules enforced (to be implemented in code)
- [ ] CLI functional (to be generated)
- [ ] Tests passing (to be generated and executed)
- [ ] Phase locked (to be executed after validation)

---

## Phase 0 Research Complete ✅

### Technical Decisions Resolved

All NEEDS CLARIFICATION items resolved via [research.md](./research.md):

1. ✅ **Runtime Language**: Python 3.11+ (LTS until 2027)
   - Rationale: Rich standard library, excellent testing ecosystem, direct path to future phases

2. ✅ **Testing Framework**: pytest 7.x + coverage.py 7.x
   - Rationale: Industry standard, 100% coverage measurement, fixture system, CLI testing support

3. ✅ **Target Platform**: Cross-platform (Windows, Linux, macOS)
   - Rationale: Python UTF-8 support, standard library argparse + sys for I/O, zero external dependencies

### Research Summary

**See [research.md](./research.md)** for detailed analysis:
- 3 runtime language candidates evaluated (Python ✅, TypeScript ❌, Rust ❌)
- 2 testing frameworks evaluated (pytest ✅, unittest ❌)
- 2 I/O strategies evaluated (standard lib ✅, rich ❌)

All alternatives documented with rationale. No technical ambiguities remain.

---

**PHASE 1 /sp.plan STATUS**: READY FOR PHASE 1 DESIGN

Phase 0 research complete. Ready to generate data-model.md, contracts/, and quickstart.md.
