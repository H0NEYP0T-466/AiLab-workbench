# Contributing to AI Workbench

First off, thank you for considering contributing to AI Workbench! It's people like you that make this project such a great tool for learning and implementing AI algorithms.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
  - [Pull Requests](#pull-requests)
- [Style Guidelines](#style-guidelines)
  - [Git Commit Messages](#git-commit-messages)
  - [Python Style Guide](#python-style-guide)
  - [Documentation Style Guide](#documentation-style-guide)
- [Testing Guidelines](#testing-guidelines)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible using our [bug report template](.github/ISSUE_TEMPLATE/bug_report.yml).

**Good Bug Reports** include:

- A clear and descriptive title
- Exact steps to reproduce the problem
- Expected behavior vs. actual behavior
- Screenshots (if applicable)
- Your environment details (OS, Python version, etc.)
- Any relevant logs or error messages

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please use our [feature request template](.github/ISSUE_TEMPLATE/feature_request.yml) and include:

- A clear and descriptive title
- A detailed description of the proposed enhancement
- Explain why this enhancement would be useful
- List any alternatives you've considered
- Include code examples if applicable

### Your First Code Contribution

Unsure where to begin? You can start by looking through issues tagged with:

- `good first issue` - Issues suitable for newcomers
- `help wanted` - Issues that need attention

### Pull Requests

1. **Fork the Repository**
   ```bash
   git clone https://github.com/H0NEYP0T-466/ai_workbench.git
   cd ai_workbench
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
   
   Use descriptive branch names:
   - `feature/add-dijkstra-algorithm`
   - `fix/bfs-infinite-loop`
   - `docs/update-readme`

3. **Make Your Changes**
   - Write clean, readable code
   - Follow the style guidelines below
   - Add comments for complex logic
   - Update documentation as needed

4. **Test Your Changes**
   - Run existing tests to ensure nothing breaks
   - Add new tests for new features
   - Verify your algorithm implementations with test cases

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add Dijkstra's algorithm implementation"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Use our [pull request template](.github/pull_request_template.md)
   - Link any related issues
   - Provide a clear description of the changes
   - Request review from maintainers

## Style Guidelines

### Git Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` - A new feature
- `fix:` - A bug fix
- `docs:` - Documentation only changes
- `style:` - Code style changes (formatting, missing semicolons, etc.)
- `refactor:` - Code refactoring without changing functionality
- `perf:` - Performance improvements
- `test:` - Adding or updating tests
- `build:` - Build system or dependency changes
- `ci:` - CI configuration changes
- `chore:` - Other changes that don't modify src or test files

**Examples:**
```
feat: add A* pathfinding algorithm
fix: resolve infinite loop in DFS implementation
docs: update installation instructions
refactor: optimize BFS queue operations
```

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) - the official Python style guide:

**Key Points:**

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 79 characters for code, 72 for comments
- Use snake_case for function and variable names
- Use PascalCase for class names
- Use UPPER_CASE for constants

**Docstrings:**

```python
def find_path(graph, start, goal):
    """
    Find a path between two nodes using BFS.
    
    Args:
        graph (dict): The graph represented as an adjacency list
        start (str): Starting node
        goal (str): Target node
    
    Returns:
        list: Path from start to goal, or None if no path exists
    
    Example:
        >>> graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        >>> find_path(graph, 'A', 'D')
        ['A', 'B', 'D']
    """
    # Implementation here
    pass
```

**Imports:**

```python
# Standard library imports
import heapq
import time
from collections import deque, defaultdict
from datetime import datetime

# Third-party imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Local imports (if applicable)
from utils import helper_function
```

### Documentation Style Guide

- Use clear, concise language
- Include code examples where appropriate
- Update README.md when adding new features
- Document all public functions and classes
- Keep documentation up-to-date with code changes

## Testing Guidelines

### Running Tests

```bash
# Run a specific lab file to test
python lab#3.py

# Test pathfinding algorithms
python Fall-23-BSCS-466-OEL.py
```

### Writing Tests

When adding new features:

1. **Test Edge Cases**
   - Empty graphs
   - Single node graphs
   - Disconnected graphs
   - Very large graphs

2. **Test Algorithm Correctness**
   - Verify path validity
   - Check optimality (for UCS, A*)
   - Confirm traversal order (for BFS, DFS)

3. **Test Performance**
   - Measure time complexity
   - Monitor memory usage
   - Compare algorithm performance

### Example Test

```python
def test_bfs_finds_shortest_path():
    """Test that BFS finds the shortest path"""
    graph = CampusGraph()
    graph.add_path("A", "B", 1)
    graph.add_path("A", "C", 1)
    graph.add_path("B", "D", 1)
    graph.add_path("C", "D", 1)
    
    path = graph.bfs("A", "D")
    assert len(path) == 3, "BFS should find path of length 3"
```

## Documentation Updates

When making changes that affect functionality:

1. Update README.md if needed
2. Update inline code comments
3. Update docstrings
4. Add examples for new features
5. Update the changelog (if present)

## Review Process

1. Maintainers will review your PR within a few days
2. Address any requested changes
3. Once approved, your PR will be merged
4. Your contribution will be recognized in the project

## Recognition

All contributors will be recognized in our project. Thank you for helping make AI Workbench better!

## Questions?

Feel free to:
- Open an issue with the `question` label
- Reach out to the maintainers
- Check existing documentation

---

Thank you for contributing to AI Workbench! 🎉
