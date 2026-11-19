
# Git Merge Strategy Evaluation Memo

## 1. Purpose

This document evaluates three GitHub Pull Request merge strategies and recommends a suitable approach for a fast-paced microservices engineering team.

## 2. Merge Strategy Comparison

### A. Create a Merge Commit

**How it works:**
- Preserves all individual commits from the feature branch.
- Creates an additional merge commit on the target branch.
- Maintains the original branch history.

**Advantages:**
- Complete development history is preserved.
- Easy to identify when a feature branch was merged.

**Disadvantages:**
- Can make Git history more complex.
- Multiple merge commits may clutter the main branch.

### B. Squash and Merge

**How it works:**
- Combines all commits from a feature branch into one commit.
- Adds that single commit to the target branch.

**Advantages:**
- Keeps the main branch history clean.
- Makes feature-level changes easier to understand.
- Simplifies reverting an entire feature.

**Disadvantages:**
- Individual feature branch commits are not preserved in main's history.
- Detailed development history is less visible on the main branch.

### C. Rebase and Merge

**How it works:**
- Replays feature branch commits onto the target branch.
- Creates a linear Git history.
- Does not create a merge commit.

**Advantages:**
- Maintains individual commits.
- Produces a clean, linear history.
- Makes commit-by-commit tracking possible.

**Disadvantages:**
- Rewrites commit history.
- Can cause confusion if developers do not understand rebasing.
- Requires care when working with shared branches.

## 3. Recommendation for a Fast-Paced Microservices Team

**Recommended Strategy: Squash and Merge**

Reasons:
1. Developers frequently create multiple commits while implementing a feature.
2. Each Pull Request can be represented by one meaningful commit.
3. The main branch remains easier to read and maintain.
4. Feature-level changes can be reviewed and reverted more easily.
5. It supports a consistent Pull Request-based development workflow.

## 4. Conclusion

All three strategies are useful depending on team requirements.

For this practice project, Squash and Merge was selected because it combines related feature changes into one commit while maintaining a clean main branch history.

The final choice should follow the engineering team's agreed Git workflow.
