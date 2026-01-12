# Harmful-Behavior Dataset

A benchmark dataset for evaluating the security of LLM-based robot systems against jailbreak attacks. This dataset contains 300 desktop manipulation tasks (150 harmful + 150 harmless) built on [RLBench](https://github.com/stepjam/RLBench) and [CoppeliaSim](https://www.coppeliarobotics.com/).

## Overview

Given the absence of standardized benchmarks for robot system security, we construct the Harmful-Behavior dataset to measure and evaluate LLM-based robot jailbreak attacks. The dataset focuses on "human-object-environment" robot safety risks as defined by ISO 10218 and the ASIMOV Benchmark.

## Dataset Structure

```
Harmful-Behavior/
├── rlbench/
│   ├── tasks/                    # Task Python definitions
│   │   ├── {task_name}.py        # Task logic and success conditions
│   │   └── __init__.py           # Task registry and predefined sets
│   ├── task_ttms/                # CoppeliaSim model files (.ttm)
│   └── assets/                   # 3D object models
├── examples/                     # Usage examples
├── tests/                        # Unit tests
└── tools/                        # Task builder and validator
```

## Robot Safety Risk Categories

Based on ISO 10218 robot safety standards, we categorize risks by **target** and **damage type**:

| Target | Risk Types |
|--------|------------|
| **Human** | mechanical damage, energetic damage, chemical damage|
| **Object** | structural damage, functional damage |
| **Environment** | environmental damage |

## Scenarios

The dataset covers **8 common robot scenarios**:
- Kitchen
- Bedroom
- Office
- Living Room
- Bathroom
- Workshop
- Laboratory
- Outdoor

## Installation

### Prerequisites

1. Install CoppeliaSim (V-REP): https://www.coppeliarobotics.com/downloads
2. Install PyRep:
```bash
pip install pyrep @ git+https://github.com/stepjam/PyRep.git
```

### Install Harmful-Behavior

```bash
git clone https://github.com/YOUR_USERNAME/Harmful-Behavior.git
cd Harmful-Behavior
pip install -e .

# Optional: Gymnasium support
pip install -e ".[gym]"
```

## Task Format

Each task is defined by:

1. **Python Class** (`rlbench/tasks/{task_name}.py`):
   - `init_task()`: Initialize object handles and success conditions
   - `init_episode(index)`: Reset episode, return task descriptions
   - `variation_count()`: Number of task variations
   - Success/failure conditions

2. **TTM Model** (`rlbench/task_ttms/{task_name}.ttm`):
   - Scene objects and layouts
   - Waypoints for reference policy
   - Sensors for success detection

## License

This project is for research purposes only. The harmful tasks are designed to evaluate robot system security and should not be used for malicious purposes.

## Acknowledgments

- [RLBench](https://github.com/stepjam/RLBench) - Robot learning benchmark
- [PyRep](https://github.com/stepjam/PyRep) - CoppeliaSim Python binding
