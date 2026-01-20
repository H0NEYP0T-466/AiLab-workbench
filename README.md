# AiLab-workbench

<p align="center">

  <!-- Core -->
  ![GitHub License](https://img.shields.io/github/license/H0NEYP0T-466/AiLab-workbench?style=for-the-badge&color=brightgreen)  
  ![GitHub Stars](https://img.shields.io/github/stars/H0NEYP0T-466/AiLab-workbench?style=for-the-badge&color=yellow)  
  ![GitHub Forks](https://img.shields.io/github/forks/H0NEYP0T-466/AiLab-workbench?style=for-the-badge&color=blue)  
  ![GitHub Issues](https://img.shields.io/github/issues/H0NEYP0T-466/AiLab-workbench?style=for-the-badge&color=red)  
  ![GitHub Pull Requests](https://img.shields.io/github/issues-pr/H0NEYP0T-466/AiLab-workbench?style=for-the-badge&color=orange)  
  ![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)  

  <!-- Activity -->
  ![Last Commit](https://img.shields.io/github/last-commit/H0NEYP0T-466/AiLab-workbench?style=for-the-badge&color=purple)  
  ![Commit Activity](https://img.shields.io/github/commit-activity/m/H0NEYP0T-466/AiLab-workbench?style=for-the-badge&color=teal)  
  ![Repo Size](https://img.shields.io/github/repo-size/H0NEYP0T-466/AiLab-workbench?style=for-the-badge&color=blueviolet)  
  ![Code Size](https://img.shields.io/github/languages/code-size/H0NEYP0T-466/AiLab-workbench?style=for-the-badge&color=indigo)  

  <!-- Languages -->
  ![Top Language](https://img.shields.io/github/languages/top/H0NEYP0T-466/AiLab-workbench?style=for-the-badge&color=critical)  
  ![Languages Count](https://img.shields.io/github/languages/count/H0NEYP0T-466/AiLab-workbench?style=for-the-badge&color=success)  

  <!-- Community -->
  ![Documentation](https://img.shields.io/badge/Docs-Available-green?style=for-the-badge&logo=readthedocs&logoColor=white)  
  ![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=for-the-badge)  

</p>

## 📖 Description

**AiLab-workbench** is a comprehensive collection of AI and data science laboratory assignments implemented in Python. This repository contains practical implementations of fundamental algorithms including path-finding algorithms (BFS, DFS, UCS), data processing, machine learning concepts, and algorithmic problem-solving techniques. Perfect for students and practitioners looking to understand core AI concepts through hands-on coding exercises.

## 🔗 Quick Links

- 📚 [Documentation](#-table-of-contents)
- 🐛 [Report Issues](https://github.com/H0NEYP0T-466/AiLab-workbench/issues)
- 🤝 [Contributing Guidelines](./CONTRIBUTING.md)
- 🛡️ [Security Policy](./SECURITY.md)
- 📏 [Code of Conduct](./CODE_OF_CONDUCT.md)

## 📑 Table of Contents

- [Description](#-description)
- [Quick Links](#-quick-links)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Folder Structure](#-folder-structure)
- [Tech Stack](#-tech-stack)
- [Dependencies & Packages](#-dependencies--packages)
- [Contributing](#-contributing)
- [License](#-license)
- [Security](#-security)
- [Code of Conduct](#-code-of-conduct)

## ✨ Features

- 🧭 **Smart Campus Path Finder** - Implementation of BFS, DFS, and UCS algorithms for optimal path finding
- 📊 **Data Analysis & Visualization** - Practical examples using NumPy, Pandas, and Matplotlib
- 🧮 **Algorithm Implementations** - Queue operations, heap structures, and graph traversal algorithms
- 📈 **Performance Comparison** - Detailed analysis and comparison of different algorithmic approaches
- 🔄 **Graph Operations** - Comprehensive graph manipulation including add, remove, and modify operations
- 📝 **Well-Documented Code** - Clear comments and explanations for educational purposes

## 🚀 Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (usually comes with Python)

### Setup Steps

1. **Clone the repository**

```bash
git clone https://github.com/H0NEYP0T-466/AiLab-workbench.git
cd AiLab-workbench
```

2. **Install required dependencies**

```bash
pip install numpy pandas matplotlib
```

3. **Verify installation**

```bash
python --version
pip list | grep -E "numpy|pandas|matplotlib"
```

## ⚡ Usage

### Running Lab Assignments

Each lab file can be executed independently. Here are some examples:

#### Smart Campus Path Finder (Lab 466 OEL)

```bash
python Fall-23-BSCS-466-OEL.py
```

This will run the campus path-finding system with interactive features including:
- Add/remove campus locations
- Find paths using BFS, DFS, and UCS
- Compare algorithm performance
- Visualize traversal history

#### Data Analysis Labs

```bash
# Run data processing lab
python Lab12.py

# Run pandas operations
python Lab13.py

# Run visualization lab
python LAB-Paper.py
```

#### Algorithm Implementation Labs

```bash
# Queue operations
python lab6.py

# Heap operations
python lab7.py

# NumPy operations
python Lab11.py
```

### Example Code Snippet

```python
from collections import deque

# Simple BFS implementation example
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
    
    return visited
```

## 📂 Folder Structure

```
AiLab-workbench/
├── Fall-23-BSCS-466-OEL.py      # Smart Campus Path Finder (BFS, DFS, UCS)
├── Fall-23-BSCS-628-OEL.py      # Advanced algorithm implementations
├── LAB-Paper.py                  # Data visualization and plotting exercises
├── Lab11.py                      # NumPy operations and arrays
├── Lab12.py                      # NumPy advanced operations
├── Lab12.1.py                    # Pandas and NumPy integration
├── Lab13.py                      # Pandas data processing
├── lab#3.py                      # Basic algorithm exercises
├── lab#3(TASK#1).py             # Specific task implementations
├── lab#4.py                      # Intermediate algorithms
├── lab#5.py                      # Data structures
├── lab#5_Task#2.py              # Advanced data structure tasks
├── lab6.py                       # Queue implementations
├── lab7.py                       # Heap and priority queue operations
├── processed_sensor_data.csv    # Sample data file for exercises
├── student_practice_data.csv    # Practice dataset
├── traversal_history.txt        # Graph traversal logs
├── README.md                     # This file
├── LICENSE                       # MIT License
├── CONTRIBUTING.md              # Contribution guidelines
├── SECURITY.md                  # Security policy
├── CODE_OF_CONDUCT.md          # Code of conduct
└── .github/                     # GitHub-specific files
    ├── ISSUE_TEMPLATE/          # Issue templates
    │   ├── bug_report.yml
    │   ├── feature_request.yml
    │   └── config.yml
    └── pull_request_template.md # PR template
```

## 🛠 Tech Stack

### Languages

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Frameworks & Libraries

![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)

### Development Tools

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

## 📦 Dependencies & Packages

This project uses Python's standard library along with essential data science packages.

### Runtime Dependencies

<details open>
<summary>Click to expand</summary>

[![NumPy](https://img.shields.io/pypi/v/numpy?style=for-the-badge&label=numpy&color=013243)](https://pypi.org/project/numpy/)
- Fast numerical computing library for array operations and mathematical functions

[![Pandas](https://img.shields.io/pypi/v/pandas?style=for-the-badge&label=pandas&color=150458)](https://pypi.org/project/pandas/)
- Powerful data manipulation and analysis library for structured data

[![Matplotlib](https://img.shields.io/pypi/v/matplotlib?style=for-the-badge&label=matplotlib&color=11557c)](https://pypi.org/project/matplotlib/)
- Comprehensive library for creating static, animated, and interactive visualizations

</details>

### Standard Library Dependencies

This project also uses Python standard library modules (included with Python):

- `collections` - Container datatypes (deque, defaultdict)
- `heapq` - Heap queue algorithm (priority queue)
- `queue` - Queue implementations
- `time` - Time access and conversions
- `datetime` - Date and time manipulation

### Installation

Install all runtime dependencies with:

```bash
pip install numpy pandas matplotlib
```

Or install specific versions for compatibility:

```bash
pip install numpy>=1.20.0 pandas>=1.3.0 matplotlib>=3.4.0
```

## 🤝 Contributing

We welcome contributions from the community! Please read our [Contributing Guidelines](./CONTRIBUTING.md) before submitting pull requests.

Quick contribution steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🛡 Security

For security concerns, please review our [Security Policy](./SECURITY.md) and report vulnerabilities responsibly.

## 📏 Code of Conduct

This project adheres to the Contributor Covenant [Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

---

<p align="center">Made with ❤️ by H0NEYP0T-466</p>
