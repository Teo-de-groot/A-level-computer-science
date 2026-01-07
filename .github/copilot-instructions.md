# Copilot Instructions for A-level-computer-science

## Project Overview
This repository contains a collection of Python scripts and exercises for A-level Computer Science, organized as standalone files. There is no complex architecture or multi-module structure; each file is generally self-contained and focused on a specific topic or exercise.

## Key Patterns and Conventions
- **File Naming:** Files are named after the topic or exercise (e.g., `Mastermind.py`, `mutability.py`, `list task.py`). Spaces and underscores are used inconsistently; match the style of existing files when adding new ones.
- **No Central Entry Point:** There is no main application or package structure. Each script can be run independently.
- **Data Files:** Some scripts (e.g., `leaderboard.csv`) use CSV files for data storage. Read/write operations are typically simple and use Python's built-in `csv` module.
- **Notebook Usage:** Jupyter notebooks may be used for interactive exercises and list comprehension problems. Follow the style of existing notebooks for educational content.

## Developer Workflows
- **Running Code:** Run scripts directly with Python 3 (e.g., `python3 Mastermind.py`).
- **Testing:** There is no formal test suite. Test scripts manually by running them and observing output.
- **Dependencies:** No external dependencies are required beyond the Python standard library.

## Examples
- **List Comprehension Patterns:** See `Untitled.ipynb` for examples and exercises on list comprehensions, including filtering and transforming lists.
- **CSV Handling:** Scripts that interact with `leaderboard.csv` demonstrate basic file I/O and CSV parsing.

## Contribution Guidelines for AI Agents
- When adding new scripts, follow the naming and structural conventions of existing files.
- Keep each script self-contained unless cross-file interaction is required for the exercise.
- Prefer clear, educational code with comments explaining key steps, as this codebase is used for learning.
- If adding new data files, document their format and usage in the script or a markdown file.

## Reference Files
- `README.md`: High-level project overview (currently minimal).
- `Untitled.ipynb`: List comprehension exercises and solutions.
- `leaderboard.csv`: Example data file for leaderboard-related scripts.

---
For more details or updates, consult the README or review individual script files for context-specific patterns.
