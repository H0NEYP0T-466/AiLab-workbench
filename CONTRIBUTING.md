# 🤝 Contributing to AiLab-workbench

First off, thank you for considering contributing to AiLab-workbench! It's people like you that make this project a great learning resource for the AI and Machine Learning community.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Branch Naming Conventions](#branch-naming-conventions)
- [Commit Message Format](#commit-message-format)
- [Pull Request Process](#pull-request-process)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing Requirements](#testing-requirements)

---

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

## Getting Started

### Fork and Clone

1. **Fork the repository** on GitHub by clicking the "Fork" button
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/AiLab-workbench.git
   cd AiLab-workbench
   ```
3. **Add upstream remote** to keep your fork in sync:
   ```bash
   git remote add upstream https://github.com/H0NEYP0T-466/AiLab-workbench.git
   ```

### Keep Your Fork Updated

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

---

## Development Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Git

### Install Dependencies

```bash
# Install required packages
pip install numpy pandas matplotlib

# Optional: Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install numpy pandas matplotlib
```

### Verify Installation

```bash
# Test that dependencies are installed correctly
python -c "import numpy; import pandas; import matplotlib; print('All dependencies installed!')"
```

---

## How to Contribute

### Types of Contributions

- 🐛 **Bug Fixes**: Fix issues or unexpected behavior
- ✨ **New Features**: Add new algorithms, exercises, or functionality
- 📝 **Documentation**: Improve or add documentation
- ♻️ **Refactoring**: Improve code structure without changing behavior
- ⚡ **Performance**: Optimize algorithm performance
- ✅ **Tests**: Add or improve test coverage

### Before You Start

1. **Check existing issues** to see if someone is already working on it
2. **Create an issue** to discuss major changes before implementing them
3. **Comment on the issue** you'd like to work on to avoid duplicate efforts

---

## Branch Naming Conventions

Use descriptive branch names with the following prefixes:

- `feat/` - New features
  - Example: `feat/add-dijkstra-algorithm`
- `fix/` - Bug fixes
  - Example: `fix/bfs-infinite-loop`
- `docs/` - Documentation changes
  - Example: `docs/update-readme-examples`
- `refactor/` - Code refactoring
  - Example: `refactor/simplify-graph-class`
- `test/` - Adding or updating tests
  - Example: `test/add-ucs-unit-tests`
- `perf/` - Performance improvements
  - Example: `perf/optimize-dfs-algorithm`
- `chore/` - Maintenance tasks
  - Example: `chore/update-dependencies`

```bash
# Create a new branch
git checkout -b feat/your-feature-name
```

---

## Commit Message Format

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only changes
- `style`: Code style changes (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```bash
# Simple commit
git commit -m "feat: add A* pathfinding algorithm"

# With scope
git commit -m "fix(graph): resolve infinite loop in DFS traversal"

# With body and footer
git commit -m "feat: add visualization for algorithm comparison

Added matplotlib-based visualization to compare execution times
and path lengths across BFS, DFS, and UCS algorithms.

Closes #42"
```

### Commit Message Guidelines

- Use the imperative mood ("add" not "added" or "adds")
- First line should be 50 characters or less
- Capitalize the first letter
- Don't end the subject line with a period
- Separate subject from body with a blank line
- Wrap the body at 72 characters
- Reference issues and pull requests in the footer

---

## Pull Request Process

### Before Submitting

1. ✅ Ensure your code follows the style guidelines
2. ✅ Update documentation if needed
3. ✅ Add comments for complex logic
4. ✅ Test your changes thoroughly
5. ✅ Update README.md if adding new features
6. ✅ Ensure no merge conflicts with main branch

### Submitting a Pull Request

1. **Push your changes** to your fork:
   ```bash
   git push origin feat/your-feature-name
   ```

2. **Open a Pull Request** on GitHub with:
   - Clear title describing the change
   - Description of what changed and why
   - Reference to related issues
   - Screenshots (if applicable for visual changes)

3. **Fill out the PR template** completely

4. **Wait for review** - maintainers will review your PR and may request changes

5. **Address feedback** - make requested changes and push updates

6. **Celebrate!** 🎉 Once approved, your PR will be merged

### Pull Request Title Format

Follow the same convention as commit messages:

```
feat: add new algorithm implementation
fix: resolve bug in path calculation
docs: update installation instructions
```

---

## Code Style Guidelines

### Python Style Guide

We follow [PEP 8](https://pep8.org/) style guidelines with some project-specific conventions:

#### General Rules

- **Indentation**: Use 4 spaces (not tabs)
- **Line Length**: Maximum 100 characters
- **Imports**: Group standard library, third-party, and local imports separately
- **Naming Conventions**:
  - Classes: `PascalCase` (e.g., `CampusGraph`)
  - Functions/methods: `snake_case` (e.g., `add_location`)
  - Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_DEPTH`)
  - Private methods: prefix with underscore (e.g., `_internal_method`)

#### Code Examples

**Good:**
```python
class PathFinder:
    """Find paths in a graph using various algorithms."""
    
    def __init__(self, graph):
        """Initialize the path finder with a graph."""
        self.graph = graph
        self.visited = set()
    
    def find_shortest_path(self, start, goal):
        """Find the shortest path using BFS."""
        if start not in self.graph or goal not in self.graph:
            raise ValueError("Invalid start or goal node")
        return self._bfs(start, goal)
```

**Bad:**
```python
class pathFinder:
    def __init__(self,g):
        self.g=g
        self.v=set()
    def FindPath(self,s,g):
        return self._bfs(s,g)
```

#### Documentation

- Add docstrings to all public classes and functions
- Use clear, descriptive variable names
- Comment complex algorithms or non-obvious logic
- Include examples in docstrings for complex functions

```python
def uniform_cost_search(graph, start, goal):
    """
    Find the lowest-cost path using Uniform Cost Search.
    
    Args:
        graph (dict): Graph represented as adjacency list with costs
        start (str): Starting node
        goal (str): Target node
    
    Returns:
        tuple: (path, total_cost) or (None, None) if no path exists
    
    Example:
        >>> graph = {'A': [('B', 5), ('C', 2)], 'B': [('D', 1)]}
        >>> path, cost = uniform_cost_search(graph, 'A', 'D')
        >>> print(f"Path: {path}, Cost: {cost}")
        Path: ['A', 'B', 'D'], Cost: 6
    """
    # Implementation here
```

#### Algorithm Implementations

- Add time and space complexity comments
- Include test cases or examples
- Use meaningful variable names
- Add performance metrics where relevant

```python
def depth_first_search(graph, start, goal):
    """
    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V) for the recursion stack
    """
    pass
```

---

## Testing Requirements

### Manual Testing

Before submitting a PR, test your changes:

1. **Run the affected scripts**:
   ```bash
   python Fall-23-BSCS-466-OEL.py
   python Fall-23-BSCS-628-OEL.py
   ```

2. **Verify outputs** are correct and expected

3. **Test edge cases**:
   - Empty inputs
   - Invalid inputs
   - Large datasets
   - Boundary conditions

### Code Validation

```bash
# Check for syntax errors
python -m py_compile your_file.py

# Verify imports work
python -c "import your_module"
```

### What to Test

- ✅ New features work as expected
- ✅ Bug fixes resolve the issue
- ✅ Existing functionality still works
- ✅ Edge cases are handled
- ✅ Error messages are clear and helpful
- ✅ Performance is acceptable

---

## Questions?

Feel free to:
- Open an issue for questions
- Join discussions in existing issues
- Reach out to maintainers

---

## Recognition

Contributors will be recognized in our README.md file. Thank you for helping make AiLab-workbench better!

---

<p align="center">
  <strong>Happy Contributing! 🚀</strong>
</p>
