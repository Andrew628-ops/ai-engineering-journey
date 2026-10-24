# Lesson 06: Python Environments

Date: 2026-10-24
Quiz: **3/3**

## Why environments matter

A virtual environment gives a project its own Python packages. Different projects can use different versions without overwriting each other's installations.

I verified these environments during the lesson:

| Environment | NumPy version |
|-------------|---------------|
| Repository `.venv` | 2.5.4 |
| Lesson `.venv-practice` | 1.26.4 |
| Lesson `.venv` managed by uv | 2.5.4 |

Installing NumPy 1.26.4 in the practice environment did not change the repository environment's NumPy 2.5.4.

## Checking which Python runs

```bash
which python
python -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
```

- `which python` shows the interpreter selected by the shell.
- `sys.executable` shows the running interpreter's path.
- `sys.prefix != sys.base_prefix` is `True` inside a standard virtual environment.

Check the installed package and its location:

```bash
python -c "import numpy; print(numpy.__version__); print(numpy.__file__)"
```

The location helps confirm which environment supplied the package.

## Creating a separate practice environment

From the repository root:

```bash
mkdir -p phases/00-setup-and-tooling/06-python-environments
cd phases/00-setup-and-tooling/06-python-environments
uv venv .venv-practice
source .venv-practice/bin/activate
uv pip install numpy==1.26.4
python -c "import numpy; print(numpy.__version__); print(numpy.__file__)"
```

The output showed NumPy 1.26.4 inside the lesson's `.venv-practice` directory.

Creating an environment does not activate it. Activation changes the current shell's environment so plain `python` selects that environment's interpreter.

From the lesson directory, I returned to the repository environment with:

```bash
deactivate
source ../../../.venv/bin/activate
python -c "import numpy; print(numpy.__version__); print(numpy.__file__)"
```

The output still showed NumPy 2.5.4 inside the repository's `.venv`.

## Describing the project

My [pyproject.toml](pyproject.toml):

```toml
[project]
name = "environment-practice"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["numpy>=1.26"]
```

The field names matter: use `requires-python` and `dependencies`. Dependencies are written as a list, even when there is only one.

`numpy>=1.26` permits both 1.26.4 and 2.5.4. It does not select one exact version for everyone.

## Locking and installing dependencies

From the lesson directory:

```bash
uv lock
```

This resolved dependencies and created [uv.lock](uv.lock). It selected NumPy **2.5.4**. Locking alone did not install the packages.

| File | Purpose |
|------|---------|
| `pyproject.toml` | Describes the project and allowed dependency requirements |
| `uv.lock` | Records exact resolved versions, including transitive dependencies |

Install from the lockfile:

```bash
uv sync --locked
```

This created the lesson project's `.venv` and installed NumPy 2.5.4. `--locked` requires the lockfile to remain current without changing it.

Verify with:

```bash
uv run --locked python -c "import sys, numpy; print(sys.executable); print(numpy.__version__)"
```

Observed interpreter:

```text
/home/student/ai/ai-engineering-journey/phases/00-setup-and-tooling/06-python-environments/.venv/bin/python
```

Observed NumPy version: `2.5.4`.

A lockfile helps reproduce dependency selections. Operating system, hardware, and other runtime differences can still affect behavior.

## Plain python versus uv run

During this exercise, the repository environment remained activated in my shell. From the lesson directory:

| Command | Environment used |
|---------|------------------|
| `python` | Activated repository `.venv` |
| `uv run --locked python` | Lesson project's `.venv` |

Changing directories does not automatically activate another environment. Both environments are called `.venv`, so check the full path.

uv warned that the active repository environment did not match the lesson project's environment. It used the project environment as intended. The `/usr/bin/python3` line during setup identified the base interpreter; it did not mean NumPy was installed globally.

## Direct and transitive dependencies

```text
My project → pandas → NumPy
```

In this example, pandas is a direct dependency. NumPy is a transitive dependency because it is needed through pandas. A lockfile includes both direct and transitive dependency selections.

## What belongs in Git

Commit `pyproject.toml` and `uv.lock`. Recreate environment directories locally instead of committing them.

Ensure these directories are ignored:

```gitignore
.venv/
.venv-practice/
```

Check from the lesson directory:

```bash
git check-ignore .venv/ .venv-practice/
```

The ignore-check output was not supplied during the lesson, so this check remains to be confirmed. Ignore rules do not remove files that Git already tracks.

## Troubleshooting concepts

- **pip and Conda:** pip can change packages outside Conda's dependency solver, which can cause conflicts. Follow the package's environment instructions when using Conda.
- **GPU compatibility:** a CUDA-enabled PyTorch build needs a compatible NVIDIA driver. A CPU-only PyTorch installation also cannot use CUDA. Virtual environments themselves do not block GPU access.
- **Unexpected package version:** check the running interpreter and package path before changing installations.

## What I corrected

- A package installation in one environment does not change another environment.
- `pyproject.toml` requirements can allow multiple versions; `uv.lock` records the selected versions.
- Plain `python` and `uv run python` can select different environments.
- A dependency of a dependency is transitive, rather than direct.

## Completion

I scored **3/3** on interpreter selection, pip/Conda dependency tracking, and CUDA-driver compatibility. Command outputs were shared during the lesson.

The official setup script, optional dependency groups, and PyTorch/Anthropic installation exercises were not performed. I practised with isolated environments rather than installing packages globally.

Next lesson: **Docker for AI**.
