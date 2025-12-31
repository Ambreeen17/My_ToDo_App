---
id: 001
title: master constitution ratification
stage: constitution
date: 2026-01-01
surface: agent
model: claude-sonnet-4.5-20250929
feature: none
branch: master
user: user
command: /sp.constitution
labels: ["constitution", "governance", "setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - N/A (constitution change)
---

## Prompt

# MASTER PROJECT CONSTITUTION
Evolution of Todo – Spec-Driven, Agentic, AI-Native System

================================================================

1. PURPOSE & VISION

This constitution defines the permanent governing law for the
"Evolution of Todo" project.

The project evolves phase-by-phase from a simple console app into
a full cloud-native, AI-powered system.

This constitution is written once and must never be rewritten.
Future work is done by adding phase-specific addendums.

================================================================

2. CORE PHILOSOPHY (IMMUTABLE)

1. Spec-Driven Development is mandatory
2. Constitution comes before specification
3. Specification comes before code
4. Manual coding is prohibited
5. Claude Code is the sole code generator
6. Phases evolve additively
7. Completed phases are locked
8. Reusable intelligence is mandatory

These principles apply to all current and future phases.

================================================================

3. ENGINEER ROLE

The engineer is not a syntax writer.

The engineer acts as:
- System architect
- Spec author
- Agent orchestrator
- Quality governor

The engineer refines specs until Claude Code produces
correct, production-quality output.

================================================================

4. SYSTEM ARCHITECTURE (GLOBAL RULE)

All phases must respect Three-Tier Architecture.

Presentation Tier
- UI
- User interaction
- Visual feedback

Application Tier
- Business logic
- Validation
- API orchestration
- Agent coordination

Data Tier
- Storage
- Persistence
- Security

================================================================

5. AI GOVERNANCE MODEL

Claude Code
- Generates all implementation code
- Responds only to approved specifications

Agents
- Own high-level responsibilities
- Interpret specifications
- Delegate work to subagents

Subagents
- Handle focused tasks
- UI, API, DB, testing, deployment, etc.

Skills
- Reusable intelligence units
- Portable across phases
- Continuously refined

================================================================

6. AGENT & SKILL RULES (GLOBAL)

- Every agent must have a clear scope
- Subagents may not exceed their assigned domain
- Skills must be reusable across phases
- No agent may bypass the constitution
- No agent may modify locked phases

================================================================

7. PHASE MODEL (GLOBAL)

The project is divided into numbered phases.

Each phase:
- Has its own scope
- Has its own specification
- May introduce new agents, subagents, and skills

Each phase is added via a Phase Addendum.
The master constitution remains unchanged.

================================================================

8. PHASE LOCKING RULE

When a phase is completed and approved:

- Its logic becomes immutable
- No future phase may alter it
- Future phases may only integrate or extend

Violating this rule breaks the system and is not allowed.

================================================================

9. FAILURE & RECOVERY RULE

If development stops, crashes, or restarts:

- Specifications remain the source of truth
- Claude Code resumes from last valid spec
- No logic is rewritten
- No manual fixes are allowed

================================================================

10. GITHUB GOVERNANCE (GLOBAL)

- main branch represents stable, locked work
- Active phase work happens in phase-specific branches
- Merge to main only after phase completion

Repository history must reflect phase evolution clearly.

================================================================

11. UI & QUALITY EXPECTATIONS (GLOBAL)

All UI introduced in any phase must:
- Be modern and production-grade
- Use consistent design language
- Include responsive behavior
- Use clean animations and transitions
- Feel like a real product, not a demo

UI quality is not optional.

================================================================

12. SECURITY & DATA RULES (GLOBAL)

- No phase may weaken data integrity
- No insecure shortcuts
- Authentication and authorization evolve by phase
- Earlier security guarantees must not be broken

================================================================

13. FUTURE PHASE COMPATIBILITY

This constitution is designed to support:
- Phase I: Console foundation
- Phase II: Full-stack web + modern UI
- Phase III: AI chatbot & agents
- Phase IV: Kubernetes & local cloud-native deployment
- Phase V: Event-driven & production cloud deployment

No rewrite should ever be required.

================================================================

14. AMENDMENT PROCESS (STRICT)

- This master constitution is never rewritten
- New phases are added as separate addendums
- Addendums may not contradict this constitution

If a conflict exists, this constitution wins.

================================================================

15. FINAL GUARANTEE

If this constitution is followed strictly:
- No architectural drift
- No agent confusion
- No phase collision
- No hackathon-time failure

This document is the single source of truth.

================================================================

END OF MASTER CONSTITUTION

## Response snapshot

Successfully created MASTER PROJECT CONSTITUTION at `.specify/memory/constitution.md` with version 1.0.0.

**Key outcomes:**
- Established immutable governance framework for Evolution of Todo project
- Defined 15 core sections covering philosophy, architecture, agent rules, phase model, and governance
- Set strict phase locking and failure recovery rules
- Established Three-Tier Architecture as global rule
- Defined AI governance hierarchy (Claude Code → Agents → Subagents → Skills)
- Created roadmap for 5 phases (Console → Full-stack web → AI chatbot → K8s → Event-driven cloud)
- Version: 1.0.0, Ratified: 2026-01-01

PHR created at: `history/prompts/constitution/001-master-constitution-ratification.constitution.prompt.md`

## Outcome

- ✅ Impact: Foundation governance established for entire project lifecycle
- 🧪 Tests: N/A (constitution change)
- 📁 Files: .specify/memory/constitution.md created
- 🔁 Next prompts: Phase I specification (/sp.spec) recommended
- 🧠 Reflection: Constitution provides immutable foundation with clear phase evolution model. Key innovation: additive phase system via addendums without rewriting master constitution.

## Evaluation notes (flywheel)

- Failure modes observed: None - initial constitution creation
- Graders run and results (PASS/FAIL): N/A (constitution change)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin Phase I specification to test constitution in practice
