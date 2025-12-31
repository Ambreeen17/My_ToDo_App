#!/usr/bin/env python3
"""Console Todo System - Main Entry Point

Phase 1: Console Todo Foundation
Spec-driven, agentic, AI-native system

Three-Tier Architecture:
- Presentation Tier (CLI)
- Application Tier (Services, Models)
- Data Tier (Repository)
"""

from src.presentation.cli.command_parser import main as cli_main


if __name__ == "__main__":
    cli_main()
