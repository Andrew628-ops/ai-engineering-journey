# Lesson 01: Dev Environment

Status: completed. Quiz: **2/3**. Recorded lesson date: 2026-10-22.

## What I did

- Checked Python, Git, and my current folder on Linux.
- Installed `uv`, created `.venv`, and activated it.
- Installed NumPy and ran my own Python exercises.
- Selected the project interpreter in my editor to address missing-import warnings.
- Recorded dependencies in `requirements.txt`, excluded `.venv` from Git, and wrote setup instructions.
- Wrote a script to report Python, NumPy, and virtual-environment activation.

Reported versions during this lesson: Python 3.12.3, Git 2.43.0, uv 0.13.5, and NumPy 2.5.4. My project folder is `/home/student/ai/ai-engineering-journey`.

## What I learned

An editor is where I write code. Python is a language; the Python interpreter runs its code. The terminal lets me issue commands, and `pwd` prints its current folder.

A virtual environment separates a project's Python packages from other projects. Two projects can need different versions of the same package. Activation changes which Python the terminal finds; it does not give the computer GPU access.

The operating system and shell must work before I can use a package manager. Libraries such as NumPy are installed into a Python environment.

## Commands I practised

Run these from the repository root. Creation and installation are setup steps; I do not need to recreate an existing environment every session.

```bash
python3 --version
git --version
pwd
uv --version
uv venv
source .venv/bin/activate
which python
uv pip install numpy
uv pip freeze
uv pip freeze > requirements.txt
uv pip install -r requirements.txt
```

`freeze` lists installed packages and versions. It does not store the packages. The `>` operator saves that list to a file and replaces any existing contents. Other people can use that file to install dependencies into their own environment.

## My exercises and results

- [hello_ai.py](hello_ai.py): printed my career goal and the result of `3 + 4`, which was `7`.
- [check_numpy.py](check_numpy.py): converted prices from thousands of dollars to dollars: `[120, 180, 250]` became `[120000, 180000, 250000]`.
- [verify_setup.py](verify_setup.py): printed Python and NumPy versions; `sys.prefix != sys.base_prefix` returned `True` inside `.venv`.

## Mistakes and corrections

- `print(3 + 4)` calculates `7`; `print("3 + 4")` prints text.
- Multiplying a Python list repeats it: `[1, 2, 3] * 2` gives `[1, 2, 3, 1, 2, 3]`.
- Multiplying a NumPy array multiplies each element. It doubles the elements only when the multiplier is 2.
- An import can work in the terminal while the editor checks a different interpreter.
- Markdown command blocks need opening and closing fences on separate lines.

## Review and follow-up

- Review why the system foundation comes before package managers; this was my missed quiz topic.
- Share `requirements.txt`, not `.venv`, on GitHub.
- PyTorch was installed later in Lesson 03. The official course preflight has not yet been recorded as run.

Self-check: can I explain why installing a package in one environment does not make it available in every interpreter?
