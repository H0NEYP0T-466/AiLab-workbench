# Contributing to AiLab-workbench

First off, thank you for considering contributing to AiLab-workbench! It's people like you that make this project a great learning resource for the community.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
  - [Pull Requests](#pull-requests)
- [Style Guidelines](#style-guidelines)
  - [Python Style Guide](#python-style-guide)
  - [Git Commit Messages](#git-commit-messages)
  - [Documentation Style](#documentation-style)
- [Testing Guidelines](#testing-guidelines)
- [Additional Notes](#additional-notes)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the [issue tracker](https://github.com/H0NEYP0T-466/AiLab-workbench/issues) to avoid duplicates. When you create a bug report, include as many details as possible:

**Use our bug report template** which includes:
- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior vs. actual behavior
- Your environment (OS, Python version, etc.)
- Screenshots if applicable
- Any relevant logs or error messages

### Suggesting Enhancements

Enhancement suggestions are tracked as [GitHub issues](https://github.com/H0NEYP0T-466/AiLab-workbench/issues). When creating an enhancement suggestion:

**Use our feature request template** which includes:
- A clear and descriptive title
- Detailed description of the proposed feature
- Explanation of why this enhancement would be useful
- Possible implementation approaches
- Any alternative solutions you've considered

### Your First Code Contribution

Unsure where to begin? You can start by looking through issues labeled:
- `good first issue` - Issues that should only require a few lines of code
- `help wanted` - Issues that may be more involved but are great for contributors

### Pull Requests

1. **Fork the Repository**
   ```bash
   git clone https://github.com/H0NEYP0T-466/AiLab-workbench.git
   cd AiLab-workbench
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

3. **Make Your Changes**
   - Write clear, commented code
   - Follow the style guidelines below
   - Add or update documentation as needed
   - Test your changes thoroughly

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add amazing new feature"
   ```

5. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request**
   - Use our pull request template
   - Link any related issues
   - Provide a clear description of changes
   - Add screenshots for UI changes

## Style Guidelines

### Python Style Guide

This project follows [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

- **Indentation**: Use 4 spaces (no tabs)
- **Line Length**: Maximum 100 characters (PEP 8 recommends 79, but we allow 100)
- **Imports**: 
  - Group imports: standard library, third-party, local
  - Use absolute imports when possible
  - One import per line
  
  ```python
  # Good
  import os
  import sys
  from collections import deque
  
  import numpy as np
  import pandas as pd
  
  from my_module import my_function
  ```

- **Naming Conventions**:
  - `snake_case` for functions and variables
  - `PascalCase` for classes
  - `UPPER_CASE` for constants
  
  ```python
  MAX_SIZE = 100
  
  class CampusGraph:
      def find_shortest_path(self):
          pass
  ```

- **Documentation**:
  - Use docstrings for all public modules, functions, classes, and methods
  - Follow Google or NumPy docstring style
  
  ```python
  def find_path(start, end, algorithm='bfs'):
      """
      Find a path between two nodes using the specified algorithm.
      
      Args:
          start (str): Starting node
          end (str): Target node
          algorithm (str): Algorithm to use ('bfs', 'dfs', or 'ucs')
      
      Returns:
          list: Path from start to end, or empty list if no path exists
      """
      pass
  ```

- **Comments**:
  - Write meaningful comments for complex logic
  - Avoid obvious comments
  - Use inline comments sparingly
  
  ```python
  # Good
  # Normalize the data to prevent overflow in exponential calculations
  normalized_data = (data - data.mean()) / data.std()
  
  # Bad
  # Increment i by 1
  i += 1
  ```

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

**Commit Message Format**:
```
<type>: <subject>

<body>

<footer>
```

**Types**:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that don't affect code meaning (formatting, etc.)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Changes to build process or auxiliary tools

**Examples**:
```
feat: add Dijkstra's algorithm implementation

Implements Dijkstra's shortest path algorithm with performance
optimizations for large graphs.

Closes #123
```

```
fix: correct BFS traversal order

The previous implementation didn't maintain proper FIFO order.
Fixed by using deque instead of list.

Fixes #456
```

### Documentation Style

- Use Markdown for all documentation
- Use emojis consistently (as shown in README.md)
- Keep language clear, concise, and friendly
- Include code examples where appropriate
- Update README.md if your changes affect usage

## Testing Guidelines

While this repository focuses on educational lab assignments, we still value testing:

1. **Manual Testing**:
   - Run your code with various inputs
   - Test edge cases (empty inputs, large datasets, etc.)
   - Verify algorithm correctness with known examples

2. **Code Review**:
   - All submissions require review before merging
   - Address review comments promptly
   - Be open to suggestions and improvements

3. **Performance Testing**:
   - For algorithm implementations, compare performance
   - Document time complexity in comments or docstrings
   - Include performance comparison outputs if relevant

## Additional Notes

### Issue and Pull Request Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested
- `wontfix` - This will not be worked on
- `duplicate` - This issue or pull request already exists
- `invalid` - This doesn't seem right

### Recognition

Contributors will be recognized in:
- GitHub's contributor list
- Special mentions in release notes for significant contributions
- Potential addition to a CONTRIBUTORS.md file in the future

### Questions?

Feel free to:
- Open a [discussion](https://github.com/H0NEYP0T-466/AiLab-workbench/discussions) for general questions
- Contact the maintainers through [issues](https://github.com/H0NEYP0T-466/AiLab-workbench/issues)
- Review closed issues for similar questions

---

Thank you for contributing to AiLab-workbench! Your efforts help make this a better learning resource for everyone. 🎉
