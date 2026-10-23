# Lesson 02: Git & Collaboration

Status: completed. Quiz: **3/3**. Recorded lesson date: 2026-10-23.

## What I did

- Inspected my repository status and commit history.
- Edited the README, inspected its diff, staged it, committed it, and pushed it.
- Created `practice/git-notes`, committed a README explanation on it, and switched back to `main`.
- Merged the practice branch into `main` and pushed the result.
- Added ignore patterns for model checkpoints and checked the patterns.

My remote repository is [ai-engineering-journey](https://github.com/Andrew628-ops/ai-engineering-journey).

## What I learned

Git tracks project history on my computer. GitHub hosts a remote repository. Saving a file in the editor does not stage, commit, or upload it.

```text
Edited files → git add → staging area
Staging area → git commit → local commit history
Local commits → git push → remote repository
```

The staging area selects changes for the next commit. A commit records a project snapshot. A branch names a line of development, so I can record experiments separately from `main`. Merging combines histories locally; it does not upload them. Branches do not guarantee conflict-free merges.

## Commands I practised

```bash
git status
git status --short
git --no-pager log --oneline --all -4
git show --stat f6e5343
git diff -- README.md
git add README.md
git diff --cached -- README.md
git commit -m "Document Git staging in README"
git push
git switch -c practice/git-notes
git switch main
git merge practice/git-notes
git check-ignore model.pt checkpoint.pth weights.safetensors
```

The branch commands above describe the exercise I already completed. Creating that same branch again would fail if it still exists.

`git diff` shows unstaged changes to tracked files. `git diff --cached` shows staged changes. Press `q` to leave Git's scrolling viewer; `--no-pager` avoids it for a command.

## Evidence from my practice

- Commit `f6e5343` added two lines to `hello_ai.py`.
- Commit `9a36a5e` documented staging in the README.
- Commit `0dd1b38` documented branches on `practice/git-notes` before I merged it into `main`.
- After committing locally, status said I was ahead of `origin/main` by one commit. After pushing, it said the branches were up to date.
- `git check-ignore` printed all three checkpoint filenames, confirming the patterns matched.

## Mistakes and corrections

- `git add` stages changes; it does not create a commit or send files to GitHub.
- A merge stays local until I push. A pull brings remote changes into my local branch; it is not the upload step.
- `.pt` matches that exact name; `*.pt` also matches names such as `model.pt`.
- Untracked files are not automatically included in a commit. I saw `.agents/` and `skills-lock.json` remain untracked during practice.

## Model-file ignore rules

```gitignore
*.pt
*.pth
*.safetensors
```

Model checkpoints can be large and are usually stored separately from ordinary Git history. Ignore rules do not stop tracking files that are already tracked.

Self-check: can I explain where a change lives after saving, adding, committing, and pushing?
