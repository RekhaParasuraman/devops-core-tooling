
# GitHub Actions CI Pipeline – Architecture

## 1. Overview

This project uses GitHub Actions to automate Python code quality checks and unit testing.

The CI workflow is defined in:

`.github/workflows/ci.yml`

The workflow automatically executes when:
- Code is pushed to the main branch.
- A Pull Request is opened targeting the main branch.
- New commits are pushed to an existing Pull Request targeting main.

The purpose is to identify coding errors and test failures early, before changes are merged into the main branch.


## 2. Runner Execution

GitHub Actions uses a GitHub-hosted Ubuntu runner to execute the CI workflow.

The runner is configured using:

`runs-on: ubuntu-latest`

A runner is a virtual machine provided by GitHub. It executes the workflow jobs in an isolated environment.

The `build` job contains the following steps:

1. **Checkout repository:** Uses `actions/checkout@v4` to download the repository code onto the runner.

2. **Set up Python:** Uses `actions/setup-python@v5` to install Python 3.11.

3. **Dependency caching:** Enables pip caching to reduce dependency installation time in future workflow runs.

4. **Install dependencies:** Installs the Python packages listed in `requirements.txt`, including pytest and flake8.

5. **Run Flake8:** Checks Python source code for style and formatting issues.

6. **Run Pytest:** Executes unit tests to verify application functionality.

The steps execute sequentially by default. The next step runs only if the previous step succeeds.


## 3. Failure Handling and Branch Protection

GitHub Actions monitors the exit status of every workflow step.

- An exit code of `0` indicates success.
- A non-zero exit code indicates failure.

If Flake8 detects coding style issues or Pytest reports a failed test, the corresponding workflow step fails.

By default, GitHub Actions stops executing subsequent steps after a failure.

The overall job is marked as failed, and GitHub displays the failure status in the Pull Request's Checks section.

### Branch Protection

Branch protection rules can be configured on the main branch to require successful CI status checks before merging.

When the CI job is configured as a required status check:

- If CI passes, the Pull Request can be merged, subject to other repository rules.
- If CI fails, the normal Pull Request merge is blocked until the required check passes.

This helps prevent code that has failed automated validation from being merged into the main branch.

## 4. Conclusion

GitHub Actions automates code validation and testing, reduces manual effort, and helps maintain code quality.

Combining CI workflows with branch protection provides an additional safeguard against merging untested or broken code.
