# 🤖 AiLab-workbench

<p align="center">
  <img src="https://img.shields.io/github/license/H0NEYP0T-466/AiLab-workbench?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/H0NEYP0T-466/AiLab-workbench?style=for-the-badge" alt="Stars">
  <img src="https://img.shields.io/github/forks/H0NEYP0T-466/AiLab-workbench?style=for-the-badge" alt="Forks">
  <img src="https://img.shields.io/github/issues/H0NEYP0T-466/AiLab-workbench?style=for-the-badge" alt="Issues">
  <img src="https://img.shields.io/github/issues-pr/H0NEYP0T-466/AiLab-workbench?style=for-the-badge" alt="Pull Requests">
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/H0NEYP0T-466/AiLab-workbench?style=for-the-badge" alt="Last Commit">
  <img src="https://img.shields.io/github/commit-activity/m/H0NEYP0T-466/AiLab-workbench?style=for-the-badge" alt="Commit Activity">
  <img src="https://img.shields.io/github/languages/top/H0NEYP0T-466/AiLab-workbench?style=for-the-badge" alt="Top Language">
  <img src="https://img.shields.io/github/languages/count/H0NEYP0T-466/AiLab-workbench?style=for-the-badge" alt="Languages Count">
</p>

**AiLab-workbench** is a comprehensive collection of AI and Machine Learning laboratory exercises and implementations. This repository contains practical implementations of fundamental algorithms including graph traversal (BFS, DFS, UCS), data structures, and data analysis projects using Python's scientific computing stack. It serves as a learning workbench for exploring AI concepts through hands-on coding exercises.

<p align="center">
  <a href="#-quick-start"><strong>Quick Start</strong></a> •
  <a href="#-features"><strong>Features</strong></a> •
  <a href="https://github.com/H0NEYP0T-466/AiLab-workbench/issues"><strong>Issues</strong></a> •
  <a href="#-contributing"><strong>Contributing</strong></a>
</p>

---

## 📑 Table of Contents

- [🚀 Quick Start](#-quick-start)
- [✨ Features](#-features)
- [📂 Project Structure](#-project-structure)
- [🛠 Tech Stack](#-tech-stack)
- [📦 Dependencies](#-dependencies)
- [📚 Documentation](#-documentation)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🛡 Security](#-security)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/H0NEYP0T-466/AiLab-workbench.git
   cd AiLab-workbench
   ```

2. **Install dependencies**
   ```bash
   pip install numpy pandas matplotlib
   ```

### Basic Usage

Run any of the lab exercises:

```bash
# Smart Campus Path Finder with BFS, DFS, and UCS algorithms
python Fall-23-BSCS-466-OEL.py

# Alternative path finder implementation
python Fall-23-BSCS-628-OEL.py

# Data analysis and visualization exercises
python LAB-Paper.py
```

---

## ✨ Features

- 🔍 **Graph Traversal Algorithms**: Implementations of BFS, DFS, and Uniform Cost Search
- 🗺️ **Smart Campus Path Finder**: Interactive path-finding system with performance comparison
- 📊 **Data Analysis Tools**: NumPy and Pandas exercises for data manipulation
- 📈 **Visualization**: Matplotlib-based data visualization examples
- 🧮 **Algorithm Practice**: Various computational problems (prime checking, Fibonacci series)
- 📚 **Structured Learning**: Progressive lab exercises from basics to advanced topics
- 🎯 **Performance Metrics**: Algorithm comparison with execution time tracking
- 💾 **Data Processing**: CSV data handling and transformation examples

---

## 📂 Project Structure

```
AiLab-workbench/
├── Fall-23-BSCS-466-OEL.py    # Main path finder with graph algorithms
├── Fall-23-BSCS-628-OEL.py    # Alternative path finder implementation
├── LAB-Paper.py                # Practice exercises (prime, fibonacci, etc.)
├── Lab11.py                    # NumPy basics
├── Lab12.py                    # Advanced data structures
├── Lab12.1.py                  # Additional lab exercises
├── Lab13.py                    # Advanced topics
├── lab#3.py                    # List operations
├── lab#3(TASK#1).py           # List slicing exercises
├── lab#4.py                    # Dictionary operations
├── lab#5.py                    # Student data management
├── lab#5_Task#2.py            # Advanced data structures
├── lab6.py                     # Data manipulation
├── lab7.py                     # Additional exercises
├── processed_sensor_data.csv   # Sample processed data
├── student_practice_data.csv   # Student data samples
└── traversal_history.txt       # Algorithm execution history
```

---

## 🛠 Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib">
</p>

### Core Technologies

- **Language**: Python 3.x
- **Data Processing**: NumPy, Pandas
- **Visualization**: Matplotlib
- **Algorithms**: Graph traversal, search algorithms
- **Data Structures**: Custom graph implementations, heaps, queues

---

## 📦 Dependencies

### Runtime Dependencies

![numpy](https://img.shields.io/pypi/v/numpy?style=for-the-badge&label=numpy&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/pypi/v/pandas?style=for-the-badge&label=pandas&logo=pandas&logoColor=white)
![matplotlib](https://img.shields.io/pypi/v/matplotlib?style=for-the-badge&label=matplotlib&logo=python&logoColor=white)

**Core Libraries:**
- **numpy**: Numerical computing and array operations
- **pandas**: Data manipulation and analysis
- **matplotlib**: Data visualization and plotting

**Standard Library:**
- **heapq**: Priority queue implementation for UCS algorithm
- **collections**: Deque and defaultdict for graph operations
- **datetime**: Timestamp and logging functionality
- **time**: Performance measurement and timing

### Installation

```bash
pip install numpy pandas matplotlib
```

Or using requirements.txt (recommended):

```bash
pip install -r requirements.txt
```

---

## 📚 Documentation

### Graph Traversal Examples

The **Smart Campus Path Finder** demonstrates three fundamental graph traversal algorithms:

#### Breadth-First Search (BFS)
```python
from Fall-23-BSCS-466-OEL import CampusGraph

# Create campus graph
campus = CampusGraph()
campus.add_location("Library")
campus.add_location("Cafeteria")
campus.add_path("Library", "Cafeteria", 5)

# Find path using BFS
path = campus.bfs("Library", "Cafeteria")
```

#### Depth-First Search (DFS)
```python
# Find path using DFS
path = campus.dfs("Library", "Cafeteria")
```

#### Uniform Cost Search (UCS)
```python
# Find optimal path using UCS
path, cost = campus.ucs("Library", "Cafeteria")
print(f"Shortest path cost: {cost}")
```

### Data Analysis Examples

Working with NumPy and Pandas:

```python
import numpy as np
import pandas as pd

# Create arrays and perform operations
arr = np.array([1, 2, 3, 4, 5])

# Load and process CSV data
df = pd.read_csv('student_practice_data.csv')
```

### Algorithm Performance

The path finder includes built-in performance metrics:
- Execution time comparison
- Path length analysis
- Node expansion tracking
- Memory usage monitoring

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:

- How to fork and clone the repository
- Development setup
- Branch naming conventions
- Commit message format
- Pull request process
- Code style guidelines

To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🛡 Security

For information about our security policy and how to report vulnerabilities, please see our [Security Policy](SECURITY.md).

---

<p align="center">
  Made with ❤️ for AI and Machine Learning education
</p>

<p align="center">
  <sub>If you find this project useful, please consider giving it a ⭐️</sub>
</p>
