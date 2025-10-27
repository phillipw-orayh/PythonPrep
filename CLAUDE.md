# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

This is a Python interview preparation project that generates coding challenge files for practice. The workflow simulates real interview conditions:
1. Generate a new challenge from the question bank
2. Solve the problem with time pressure (25 min timer)
3. Run auto-generated unit tests
4. Get AI-powered feedback on complexity, optimization, and approach

## Architecture

The project follows a modular structure with clear separation of concerns:

- **questions/** - Question bank organized by difficulty (easy/medium/hard)
  - `meta.json` tracks question metadata (frequency, difficulty, tags)

- **sessions/** - Generated challenge files where solutions are written
  - Each file is named `session_NNN_<problem_name>.py`
  - Contains: problem statement, hints, solution space, unit tests, self-review checklist

- **utils/** - Core logic for generating and evaluating challenges
  - `question_generator.py` - Creates new challenge files from question bank
  - `template.py` - Standard format/boilerplate for each challenge file
  - `test_runner.py` - Executes tests on completed solutions
  - `ai_feedback.py` - (Optional) Integration for automated code review

- **data/** - Tracking and analytics
  - `solved_log.json` - Records completed problems with notes and metrics

## Development Workflow

Since this codebase is in early stages, when implementing:

1. Start by creating the `utils/` modules in this order:
   - `template.py` first (defines the challenge file structure)
   - `question_generator.py` second (depends on template)
   - `test_runner.py` third (needs generated files to test)

2. Create the question bank structure in `questions/` with at least a few sample problems before testing the generator

3. The timer feature for interview simulation should be implemented in `question_generator.py` with optional hint reveal at the midpoint

4. Test generation should be flexible - allow both manual test writing and auto-generation from expected outputs
