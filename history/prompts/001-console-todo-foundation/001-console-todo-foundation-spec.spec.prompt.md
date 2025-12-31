---
id: 001
title: console todo foundation spec
stage: spec
date: 2026-01-01
surface: agent
model: claude-sonnet-4.5-20250929
feature: 001-console-todo-foundation
branch: 001-console-todo-foundation
user: user
command: /sp.specify
labels: ["phase1", "console", "specification"]
links:
  spec: specs/001-console-todo-foundation/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-console-todo-foundation/spec.md
  - specs/001-console-todo-foundation/checklists/requirements.md
tests:
  - N/A (specification phase)
---

## Prompt

# /sp.specify

## PHASE 1 — Console Todo Foundation

---

## 1. PHASE IDENTITY

* **Phase Number:** 1
* **Phase Name:** Console Todo Foundation
* **Phase Status:** Specification Stage
* **Parent Law:** Master Project Constitution (Immutable)

This phase establishes the **absolute foundation** of the system.
All future phases will extend this logic without modification.

---

## 2. PHASE GOAL (NON-NEGOTIABLE)

Build a **pure, deterministic, console-based Todo system** that:

* Manages todos via CLI
* Has clean business rules
* Is fully spec-driven
* Contains zero UI or web assumptions

This phase proves architectural discipline.

---

## 3. IN-SCOPE FEATURES

### 3.1 Todo Entity

Each Todo MUST have:

* Unique ID (deterministic)
* Title (required)
* Description (optional)
* Status (Pending | Completed)
* Created Timestamp
* Updated Timestamp

---

### 3.2 Core Operations

The system MUST support:

1. Create Todo
2. List Todos
3. Update Todo
4. Mark Todo as Completed
5. Delete Todo

All operations must be reversible via future phases.

---

### 3.3 Input & Output

* Input via console commands
* Output via formatted console text
* No colors, no animations, no UI frameworks

---

## 4. OUT-OF-SCOPE (STRICT)

The following are explicitly forbidden:

* GUI or Web UI
* Database persistence
* Authentication
* AI features
* Network calls
* External libraries (except standard runtime)

---

## 5. ARCHITECTURAL CONSTRAINTS

### 5.1 Three-Tier Enforcement

Even in console mode, structure MUST exist:

* **Presentation Tier:** CLI Interface
* **Application Tier:** Business Logic
* **Data Tier:** In-memory repository

No layer may bypass another.

---

## 6. AGENT ASSIGNMENTS

### 6.1 Governing Agent

* `SystemGovernorAgent`

  * Validates constitution compliance

---

### 6.2 Active Phase Agents

* `SpecAuthorAgent`
* `ArchitectureAgent`
* `BusinessLogicAgent`
* `QualityAssuranceAgent`

---

### 6.3 Subagents Mapping

* CLI Handling → `WorkflowSubagent`
* Validation Rules → `ValidationSubagent`
* Entity Design → `DomainModelSubagent`
* Testing → `UnitTestSubagent`

---

## 7. REQUIRED SKILLS

This phase MUST use:

* `SpecRefinementSkill`
* `DomainModelingSkill`
* `ValidationRuleSkill`
* `PhaseLockVerificationSkill`

No new skills introduced unless justified.

---

## 8. BUSINESS RULES (IMMUTABLE AFTER LOCK)

1. Todo title cannot be empty
2. Completed todos cannot be edited
3. Deleted todos are permanently removed
4. IDs are never reused
5. System behavior must be deterministic

---

## 9. ACCEPTANCE CRITERIA

Phase 1 is considered COMPLETE only if:

* All CRUD operations work correctly
* Invalid input is safely rejected
* All rules are enforced by logic, not UI
* Unit tests cover all operations
* No constitution rule is violated

---

## 10. LOCK CONDITIONS

Once approved:

* Business rules become immutable
* Entity structure is locked
* Future phases may only extend behavior

Violation breaks the system.

---

## 11. FAILURE RECOVERY

If execution stops:

* Resume from this spec
* Regenerate code via Claude Code
* No manual edits allowed

---

## 12. OUTPUT EXPECTATION

Claude Code MUST output:

* Clean, readable code
* Clear separation of layers
* Console-run instructions
* Test execution steps

---

**PHASE 1 /sp.specify STATUS:** READY FOR `/sp.plan`

This specification is final once approved.

## Response snapshot

Successfully created Phase 1 specification for Console Todo Foundation.

**Branch Created**: `001-console-todo-foundation`
**Spec File**: `specs/001-console-todo-foundation/spec.md`
**Checklist**: `specs/001-console-todo-foundation/checklists/requirements.md`

**Specification Summary**:
- 5 User Stories defined (P1: Create/List, P2: Update/Complete/Delete)
- 13 Functional Requirements (FR-001 to FR-013)
- 5 Immutable Business Rules (BR-001 to BR-005)
- 8 Success Criteria (SC-001 to SC-008)
- Three-tier architecture constraints enforced
- Clear out-of-scope boundaries defined
- All constitution rules aligned

**Quality Validation**: ✅ PASSED
- No [NEEDS CLARIFICATION] markers
- All requirements testable and unambiguous
- Success criteria measurable and technology-agnostic
- User scenarios comprehensively cover CRUD operations

**Status**: READY FOR `/sp.plan`

## Outcome

- ✅ Impact: Foundation specification established for Phase 1 Console Todo system
- 🧪 Tests: N/A (specification phase)
- 📁 Files: spec.md and requirements.md checklist created
- 🔁 Next prompts: Run `/sp.plan` to generate implementation plan
- 🧠 Reflection: Specification successfully captures all user requirements while maintaining strict constitutional alignment. Three-tier architecture and immutable business rules provide clear foundation for future phases.

## Evaluation notes (flywheel)

- Failure modes observed: None - initial specification creation
- Graders run and results (PASS/FAIL): N/A (specification phase)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Execute `/sp.plan` to generate detailed implementation plan and validate constitution compliance
