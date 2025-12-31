![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Phase 1](https://img.shields.io/badge/phase-foundation-orange.svg)](specs/001-console-todo-foundation)
[![Spec-Driven Development](https://img.shields.io/badge/methodology-spec--driven-blueviolet.svg)](.specify/memory/constitution.md)

# Evolution of Todo

> A modern, spec-driven Todo application demonstrating phased software development from console to cloud-native deployment.

## Overview

**MyTodo App** is a production-grade application that evolves through five distinct phases, demonstrating best practices in software architecture, testing, and deployment. This project showcases how to build maintainable, scalable systems using **Spec-Driven Development (SDD)** methodology.

### Current Phase: Phase 1 - Console Foundation

The project starts with a solid console-based foundation, then evolves into a full-stack web application, adds AI capabilities, transitions to Kubernetes, and finally becomes an event-driven cloud-native system.

## Key Features

### Phase 1 Features (Current)
- **Complete CRUD Operations**: Create, Read, Update, Delete todos
- **Immutable Business Rules**: 5 enforced rules at the application layer
- **Deterministic Behavior**: Unique IDs that are never reused, no randomness
- **Clean Architecture**: Three-tier separation (Presentation → Application → Data)
- **Zero External Dependencies**: Built with Python standard library only
- **Production Quality**: Comprehensive error handling, user-friendly output, cross-platform support

### Development Methodology
- **Spec-Driven Development**: Every feature starts with specifications
- **Constitution Governance**: Master document guides all development decisions
- **Phase-Locking**: Completed phases become immutable foundations
- **AI-Generated Code**: Manual coding prohibited, ensuring consistency
- **Three-Tier Architecture**: Strict separation of concerns

## Quick Start

### Prerequisites

- Python 3.11 or higher
- Virtual environment (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/Ambreeen17/My_ToDo_App.git
cd My_ToDo_App

# Create and activate virtual environment
python -m venv .venv

# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Install development dependencies
pip install -r requirements-dev.txt
```

### Usage Examples

```bash
# Create a new todo
python main.py create "Buy groceries" --description "Milk, eggs, bread"

# List all todos
python main.py list

# Update a pending todo
python main.py update 1 --title "Buy groceries and snacks"

# Mark todo as completed
python main.py complete 1

# Delete a todo
python main.py delete 1
```

## CLI Reference

| Command | Arguments | Description | Example |
|---------|-----------|-------------|---------|
| `create` | `<title>` `--description` (optional) | Create a new todo | `python main.py create "Buy groceries" --description "Milk, eggs"` |
| `list` | None | List all todos | `python main.py list` |
| `update` | `<id>` `--title` (optional) `--description` (optional) | Update pending todo | `python main.py update 1 --title "Updated title"` |
| `complete` | `<id>` | Mark todo as completed | `python main.py complete 1` |
| `delete` | `<id>` | Permanently delete todo | `python main.py delete 1` |

## Architecture

### Three-Tier Architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│ Presentation Tier (CLI)                                                │
│ - Parses commands (argparse)                                            │
│ - Formats output (f-strings)                                            │
│ - No business logic                                                     │
└──────────────────────────────────────────────────────────────────────────┘
                                    │
                    validates, enforces rules, orchestrates
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────┐
│ Application Tier (Service)                                             │
│ - Business logic (TodoService)                                         │
│ - Validation (title, status, immutability)                              │
│ - Entity management (Todo dataclass)                                    │
└──────────────────────────────────────────────────────────────────────────┘
                                    │
                    stores, retrieves, deletes
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────┐
│ Data Tier (Repository)                                                   │
│ - In-memory storage (collections)                                        │
│ - CRUD operations (Create, Read, Update, Delete)                        │
└──────────────────────────────────────────────────────────────────────────┘
```

### Project Structure

```
My_ToDo_App/
├── src/
│   ├── application/
│   │   ├── models/
│   │   │   └── todo.py              # Todo entity with validation
│   │   └── services/
│   │       ├── id_generator.py      # Deterministic ID generation
│   │       └── todo_service.py      # Business logic & validation
│   ├── infrastructure/
│   │   └── repositories/
│   │       ├── itodo_repository.py  # Repository interface
│   │       └── in_memory_todo_repository.py  # In-memory storage
│   └── presentation/
│       └── cli/
│           ├── command_parser.py    # CLI command parsing
│           └── output_formatter.py  # Console output formatting
├── specs/
│   └── 001-console-todo-foundation/
│       ├── spec.md                  # Feature specification
│       ├── plan.md                  # Implementation plan
│       ├── research.md              # Technical decisions
│       ├── data-model.md            # Entity definitions
│       ├── contracts/
│       │   └── service-contracts.md
│       ├── tasks.md                # Task list
│       └── quickstart.md           # Quick start guide
├── history/
│   ├── prompts/                    # Prompt History Records
│   └── adr/                       # Architecture Decision Records
├── .specify/
│   └── memory/
│       └── constitution.md         # Master governance document
├── main.py                         # CLI entry point
├── requirements-dev.txt            # Development dependencies
├── pytest.ini                      # Test configuration
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

## Business Rules

The system enforces these **immutable business rules**:

| Rule ID | Description | Enforcement Point |
|---------|-------------|-------------------|
| **BR-001** | Title cannot be empty | Todo entity + TodoService validation |
| **BR-002** | Completed todos cannot be edited | Todo.can_edit() check + service validation |
| **BR-003** | Deleted todos are permanently removed | No soft delete in repository |
| **BR-004** | IDs are never reused | Monotonic increment in ID generator |
| **BR-005** | System behavior is deterministic | No randomness, no hidden state |

## Documentation

### Core Documentation

- **[Master Constitution](.specify/memory/constitution.md)** - The supreme governing document that guides all development decisions. Contains 15 sections covering purpose, principles, architecture, governance, and amendment processes.

- **[Phase 1 Specification](specs/001-console-todo-foundation/spec.md)** - Complete feature requirements with 5 user stories, 13 functional requirements, and 8 success criteria.

- **[Phase 1 Implementation Plan](specs/001-console-todo-foundation/plan.md)** - Technical architecture, decisions, and implementation strategy.

- **[Phase 1 Research](specs/001-console-todo-foundation/research.md)** - Technical decisions including language selection (Python 3.11+), testing framework (pytest 7.x), and cross-platform strategy.

### Technical Documentation

- **[Data Model](specs/001-console-todo-foundation/data-model.md)** - Entity definitions, state transitions, and business rule enforcement points.

- **[Service Contracts](specs/001-console-todo-foundation/contracts/service-contracts.md)** - Interface definitions for repository, service, and ID generator layers.

- **[Quickstart Guide](specs/001-console-todo-foundation/quickstart.md)** - 5-minute tutorial covering all CLI commands with examples.

- **[Task List](specs/001-console-todo-foundation/tasks.md)** - 40 atomic tasks organized by user story with dependencies and MVP strategy.

### Development History

- **[Prompt History Records](history/prompts/)** - Complete record of all development conversations and decisions.
- **[Architecture Decision Records](history/adr/)** - Significant architectural decisions with rationale and tradeoffs (future phases).

## Phase 1 Deliverables

### Completed Artifacts

- ✅ **Specification**: Feature requirements and acceptance criteria
- ✅ **Implementation Plan**: Technical decisions and architecture
- ✅ **Research**: Python 3.11+, pytest 7.x, cross-platform strategy
- ✅ **Data Model**: Todo entity with validation rules
- ✅ **Service Contracts**: Interfaces for repository and service layers
- ✅ **Quickstart Guide**: Step-by-step tutorial
- ✅ **Task List**: 40 atomic tasks organized by user story
- ✅ **Implementation**: Full working console application
- ✅ **Documentation**: Comprehensive README and inline docs
- ✅ **Constitution**: Master governance document (v1.0.0)

### Acceptance Criteria Met

- ✅ All CRUD operations work correctly
- ✅ Invalid input is safely rejected with clear error messages
- ✅ All business rules (5 immutable rules) are enforced by logic layer
- ✅ No constitution rule is violated
- ✅ System behaves deterministically
- ✅ Three-tier architecture separation is maintained
- ✅ IDs are never reused
- ✅ Zero external dependencies (Python stdlib only)

## Roadmap

### Phase 1: Console Foundation ✅
- **Status**: Complete
- **Focus**: CLI interface, in-memory storage
- **Branch**: `001-console-todo-foundation`
- **Deliverables**: 49 files, 5,143 lines of code and documentation

### Phase 2: Full-Stack Web + Modern UI (Planned)
- **Focus**: Web API, responsive UI, persistent storage
- **Technologies**: FastAPI, React/Vue, PostgreSQL
- **Features**: REST API, Database persistence, Authentication

### Phase 3: AI Chatbot & Agents (Planned)
- **Focus**: AI-powered suggestions, conversational interface
- **Technologies**: LangChain, OpenAI API, Vector databases
- **Features**: Natural language processing, Smart task suggestions, Context-aware recommendations

### Phase 4: Kubernetes & Local Cloud (Planned)
- **Focus**: Containerization, orchestration, deployment
- **Technologies**: Docker, Kubernetes, Helm, Prometheus
- **Features**: Container orchestration, Auto-scaling, Monitoring & logging

### Phase 5: Event-Driven & Production Cloud (Planned)
- **Focus**: Event streaming, message queues, cloud deployment
- **Technologies**: Kafka, RabbitMQ, AWS/GCP, Event Sourcing
- **Features**: Event-driven architecture, Microservices, Cloud-native deployment

## Development

### Running Tests

```bash
# Run all tests with coverage
pytest --cov=src --cov-report=html --cov-report=term

# Open coverage report
# Windows:
start htmlcov/index.html
# Linux/macOS:
open htmlcov/index.html
```

### Dependencies

**Development Dependencies**:
- `pytest>=7.4.0` - Testing framework
- `pytest-cov>=4.1.0` - Coverage plugin
- `coverage>=7.3.0` - Coverage reporting

**Runtime Dependencies**: None (Python standard library only)

### Project Philosophy

This project is built using **Spec-Driven Development** principles:

1. **Constitution Before Specification**: Governance first, always
2. **Specification Before Code**: Design before implementation
3. **Manual Coding Prohibited**: AI-generated code only
4. **Phased Evolution**: Incremental, additive growth
5. **Immutable Phases**: Locked foundation, extensible future

### Constitution Principles

The [Master Constitution](.specify/memory/constitution.md) establishes these core principles:

- **Spec-Driven Development**: All work must be specification-first
- **Three-Tier Architecture Enforced**: Presentation, Application, Data separation mandatory
- **Phase Locking Rules**: Completed phases become immutable
- **AI Code Generation**: Manual coding prohibited
- **GitHub Governance**: Branch-per-feature strategy
- **UI Quality Requirements**: Human-readable, accessible output
- **Security & Data Rules**: No secrets, defensive programming
- **Failure & Recovery Rule**: Phase failure requires amendment, not rewrite
- **Versioning**: Semantic versioning for constitution

## Contributing

Contributions are welcome! This project follows a spec-driven development methodology.

### Contribution Guidelines

1. **Read the Constitution**: Start with the [Master Constitution](.specify/memory/constitution.md)
2. **Review Specifications**: Understand existing [Feature Specifications](specs/)
3. **Follow Plans**: Adhere to [Implementation Plans](specs/001-console-todo-foundation/plan.md)
4. **Create Issues**: Use [GitHub Issues](https://github.com/Ambreeen17/My_ToDo_App/issues) for discussion
5. **Submit PRs**: Follow the spec-driven workflow for all changes

### Development Workflow

1. Create a new branch from `master`
2. Follow `/sp.specify` → `/sp.plan` → `/sp.tasks` → `/sp.implement` workflow
3. Ensure all constitution principles are followed
4. Create appropriate Prompt History Records
5. Document significant architectural decisions with ADRs
6. Submit pull request for review

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Repository**: https://github.com/Ambreeen17/My_ToDo_App
- **Issues**: https://github.com/Ambreeen17/My_ToDo_App/issues
- **Discussions**: https://github.com/Ambreeen17/My_ToDo_App/discussions

---

**Phase 1 Implementation Complete — Ready for Lock** 🎉

Built with ❤️ using Spec-Driven Development principles.
