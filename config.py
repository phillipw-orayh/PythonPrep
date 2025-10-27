"""Configuration settings for Python Interview Prep project."""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent

# Directory paths
QUESTIONS_DIR = PROJECT_ROOT / "questions"
SESSIONS_DIR = PROJECT_ROOT / "sessions"
DATA_DIR = PROJECT_ROOT / "data"
UTILS_DIR = PROJECT_ROOT / "utils"

# Question difficulty levels
EASY_DIR = QUESTIONS_DIR / "easy"
MEDIUM_DIR = QUESTIONS_DIR / "medium"
HARD_DIR = QUESTIONS_DIR / "hard"

# Data files
META_FILE = QUESTIONS_DIR / "meta.json"
SOLVED_LOG_FILE = DATA_DIR / "solved_log.json"
STATS_FILE = DATA_DIR / "stats.json"

# Session settings
SESSION_TIME_LIMIT_MINUTES = 25
HINT_REVEAL_TIME_MINUTES = 12

# Difficulty levels
DIFFICULTY_LEVELS = ["easy", "medium", "hard"]

# Common topics/tags
TOPICS = [
    "arrays",
    "strings",
    "linked_lists",
    "trees",
    "graphs",
    "dynamic_programming",
    "recursion",
    "sorting",
    "searching",
    "hash_tables",
    "stacks",
    "queues",
    "heaps",
    "bit_manipulation",
    "math",
    "two_pointers",
    "sliding_window",
    "backtracking",
    "greedy",
    "bfs",
    "dfs"
]
