# AI Workbench

<p align="center">
  <!-- Core -->
  <img src="https://img.shields.io/github/license/H0NEYP0T-466/ai_workbench?style=for-the-badge&color=brightgreen" alt="GitHub License">
  <img src="https://img.shields.io/github/stars/H0NEYP0T-466/ai_workbench?style=for-the-badge&color=yellow" alt="GitHub Stars">
  <img src="https://img.shields.io/github/forks/H0NEYP0T-466/ai_workbench?style=for-the-badge&color=blue" alt="GitHub Forks">
  <img src="https://img.shields.io/github/issues/H0NEYP0T-466/ai_workbench?style=for-the-badge&color=red" alt="GitHub Issues">
  <img src="https://img.shields.io/github/issues-pr/H0NEYP0T-466/ai_workbench?style=for-the-badge&color=orange" alt="GitHub Pull Requests">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge" alt="Contributions Welcome">
  
  <!-- Activity -->
  <img src="https://img.shields.io/github/last-commit/H0NEYP0T-466/ai_workbench?style=for-the-badge&color=purple" alt="Last Commit">
  <img src="https://img.shields.io/github/commit-activity/m/H0NEYP0T-466/ai_workbench?style=for-the-badge&color=teal" alt="Commit Activity">
  <img src="https://img.shields.io/github/repo-size/H0NEYP0T-466/ai_workbench?style=for-the-badge&color=blueviolet" alt="Repo Size">
  <img src="https://img.shields.io/github/languages/code-size/H0NEYP0T-466/ai_workbench?style=for-the-badge&color=indigo" alt="Code Size">
  
  <!-- Languages -->
  <img src="https://img.shields.io/github/languages/top/H0NEYP0T-466/ai_workbench?style=for-the-badge&color=critical" alt="Top Language">
  <img src="https://img.shields.io/github/languages/count/H0NEYP0T-466/ai_workbench?style=for-the-badge&color=success" alt="Languages Count">
  
  <!-- Community -->
  <img src="https://img.shields.io/badge/Documentation-Available-green?style=for-the-badge&logo=readthedocs&logoColor=white" alt="Documentation">
  <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=for-the-badge" alt="Open Source Love">
</p>

## 📖 About

AI Workbench is a comprehensive collection of artificial intelligence algorithms and data structures implementations, focusing on graph traversal algorithms (BFS, DFS, UCS), pathfinding solutions, and data analysis tools. This repository contains lab assignments and practical implementations for AI and computer science coursework.

## 🔗 Quick Links

- [Issues](https://github.com/H0NEYP0T-466/ai_workbench/issues) - Report bugs or request features
- [Contributing](CONTRIBUTING.md) - Learn how to contribute
- [Security](SECURITY.md) - Report security vulnerabilities
- [Code of Conduct](CODE_OF_CONDUCT.md) - Community guidelines

## 📑 Table of Contents

- [About](#-about)
- [Quick Links](#-quick-links)
- [Installation](#-installation)
- [Usage](#-usage)
- [Features](#-features)
- [Folder Structure](#-folder-structure)
- [Tech Stack](#-tech-stack)
- [Dependencies & Packages](#-dependencies--packages)
- [Contributing](#-contributing)
- [License](#-license)
- [Security](#-security)
- [Code of Conduct](#-code-of-conduct)

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/H0NEYP0T-466/ai_workbench.git
   cd ai_workbench
   ```

2. **Install dependencies**
   ```bash
   pip install numpy pandas matplotlib
   ```

3. **Verify installation**
   ```bash
   python --version
   ```

## ⚡ Usage

### Running Path Finding Algorithms

```bash
# Run the comprehensive campus pathfinder (BFS, DFS, UCS)
python Fall-23-BSCS-466-OEL.py

# Run the alternative pathfinder implementation
python Fall-23-BSCS-628-OEL.py
```

### Running Lab Exercises

```bash
# Lab 3 - Basic graph operations
python lab#3.py

# Lab 4 - Advanced graph algorithms
python lab#4.py

# Lab 5 - Data structures and algorithms
python lab#5.py

# Lab 6 - Search algorithms
python lab6.py

# Lab 7 - Optimization techniques
python lab7.py

# Lab 11 - Advanced topics
python Lab11.py

# Lab 12 - Complex algorithms
python Lab12.py

# Lab 13 - Final implementations
python Lab13.py
```

### Example Usage

```python
from collections import deque, defaultdict
import heapq

# Create a campus graph
graph = CampusGraph()

# Add locations
graph.add_location("Library")
graph.add_location("Cafeteria")

# Add paths with costs
graph.add_path("Library", "Cafeteria", 150)

# Find path using BFS
path = graph.bfs("Library", "Cafeteria")
print(f"Path found: {path}")
```

## ✨ Features

- **Smart Campus Path Finder**: Comprehensive pathfinding system with multiple algorithms
- **BFS (Breadth-First Search)**: Optimal for unweighted graphs
- **DFS (Depth-First Search)**: Memory-efficient exploration
- **UCS (Uniform Cost Search)**: Optimal pathfinding for weighted graphs
- **Performance Comparison**: Side-by-side algorithm analysis
- **Interactive CLI**: User-friendly command-line interface
- **Graph Visualization**: Visual representation of paths and nodes
- **Data Analysis Tools**: CSV processing and sensor data handling
- **Algorithm Metrics**: Time complexity and space complexity tracking
- **Traversal History**: Complete logging of algorithm execution

## 📂 Folder Structure

```
ai_workbench/
├── Fall-23-BSCS-466-OEL.py        # Smart Campus Path Finder (comprehensive)
├── Fall-23-BSCS-628-OEL.py        # Alternative pathfinder implementation
├── LAB-Paper.py                    # Lab paper implementation
├── Lab11.py                        # Lab 11 exercises
├── Lab12.1.py                      # Lab 12 part 1
├── Lab12.py                        # Lab 12 main exercises
├── Lab13.py                        # Lab 13 exercises
├── lab#3(TASK#1).py               # Lab 3 Task 1
├── lab#3.py                        # Lab 3 exercises
├── lab#4.py                        # Lab 4 exercises
├── lab#5.py                        # Lab 5 exercises
├── lab#5_Task#2.py                # Lab 5 Task 2
├── lab6.py                         # Lab 6 exercises
├── lab7.py                         # Lab 7 exercises
├── processed_sensor_data.csv       # Processed sensor data
├── student_practice_data.csv       # Student practice dataset
├── traversal_history.txt           # Algorithm traversal logs
├── README.md                       # This file
├── LICENSE                         # MIT License
├── CONTRIBUTING.md                 # Contribution guidelines
├── SECURITY.md                     # Security policy
└── CODE_OF_CONDUCT.md             # Community guidelines
```

## 🛠 Tech Stack

### Languages
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Libraries & Frameworks
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)

### Tools & Development
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

## 📦 Dependencies & Packages

This project uses Python's standard library along with a few essential data science packages for numerical computing, data manipulation, and visualization.

### Runtime Dependencies

<details open>
<summary>Click to expand</summary>

[![NumPy](https://img.shields.io/pypi/v/numpy?style=for-the-badge&label=numpy&logo=numpy&color=013243)](https://pypi.org/project/numpy/)
**numpy** - Fundamental package for scientific computing with Python, providing support for arrays, matrices, and mathematical functions.

[![Pandas](https://img.shields.io/pypi/v/pandas?style=for-the-badge&label=pandas&logo=pandas&color=150458)](https://pypi.org/project/pandas/)
**pandas** - Powerful data analysis and manipulation library for structured data operations.

[![Matplotlib](https://img.shields.io/pypi/v/matplotlib?style=for-the-badge&label=matplotlib&color=11557c)](https://pypi.org/project/matplotlib/)
**matplotlib** - Comprehensive library for creating static, animated, and interactive visualizations in Python.

</details>

### Standard Library Modules

The project also leverages Python's built-in standard library modules:
- `collections` - Container datatypes (deque, defaultdict)
- `heapq` - Heap queue algorithm (priority queue)
- `queue` - Synchronized queue classes
- `time` - Time access and conversions
- `datetime` - Basic date and time types

> **Note**: No external dependencies file (requirements.txt) is currently present. To install the required packages, run:
> ```bash
> pip install numpy pandas matplotlib
> ```

## 🤝 Contributing

We welcome contributions from the community! Please read our [Contributing Guidelines](CONTRIBUTING.md) to learn about our development process, coding standards, and how to submit pull requests.

### Quick Start for Contributors

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🛡 Security

We take security seriously. If you discover a security vulnerability, please review our [Security Policy](SECURITY.md) for instructions on how to report it responsibly.

## 📏 Code of Conduct

This project adheres to the Contributor Covenant [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

<p align="center">Made with ❤️ by H0NEYP0T-466</p>
