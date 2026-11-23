# DevOps Core Tooling

![Build Status](https://github.com/RekhaParasuraman/devops-core-tooling/actions/workflows/ci.yml/badge.svg)

## Overview

DevOps Core Tooling is a Python-based project demonstrating
software engineering practices and DevOps fundamentals.

The project includes Git-based version control, GitHub
collaboration workflows, automated testing, and continuous
integration using GitHub Actions.

## Features

- Python application with a simple entry point.
- User dashboard functionality.
- Git branching, merging, and pull request workflows.
- Automated code linting using flake8.
- Automated unit testing using pytest.
- Continuous Integration using GitHub Actions.

## Architecture Overview

The project follows a simple development and CI workflow:

1. Developers make changes to the source code.
2. Changes are pushed to the GitHub repository.
3. Pull requests trigger the GitHub Actions workflow.
4. GitHub Actions runs code linting and unit tests.
5. The changes can be merged when the required checks pass.

### System Architecture Diagram

<!-- TODO: Add the system architecture diagram here. -->

## Technologies

- Python
- Git
- GitHub
- GitHub Actions
- pytest
- flake8

## Prerequisites

Before getting started, install:

- Git
- Python 3.11 or later
- pip

## Installation and Environment Setup

### 1. Clone the repository

```bash
git clone https://github.com/RekhaParasuraman/devops-core-tooling.git
```

### 2. Navigate to the project directory

```bash
cd devops-core-tooling
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

On Linux or macOS:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```


## Usage

### Run the main application

Execute the following command from the project directory:

    python main.py

Expected output:

    Welcome to DevOps Core Tooling!

### Run the user dashboard

Execute:

    python user_dashboard.py

The application displays the user dashboard information.


## Testing and Code Quality

### Run unit tests

The project uses pytest for automated testing.

Execute:

    python -m pytest

### Run code linting

The project uses flake8 to check Python code quality.

Execute:

    python -m flake8 --exclude=.venv .

Both commands should complete successfully before submitting code changes.

## Continuous Integration

GitHub Actions automatically runs the CI workflow when:

- Code is pushed to the main branch.
- A pull request is opened targeting the main branch.

The workflow performs:

- Python environment setup.
- Dependency installation.
- Code linting using flake8.
- Unit testing using pytest.

The required CI status check must pass before changes can be merged into the protected main branch.


## Contributing

Contributions are welcome!

To contribute to this project:

1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new feature branch.
4. Make your changes.
5. Run the unit tests and code linting checks.
6. Commit and push your changes.
7. Open a pull request against the main branch.
8. Provide a clear description of your changes in the pull request.

Please follow the existing coding conventions and ensure that all required CI checks pass before requesting a merge.

## Code of Conduct

All contributors are expected to communicate respectfully and maintain a welcoming and collaborative environment.

Please follow the guidelines in the project's [Code of Conduct](CODE_OF_CONDUCT.md).
