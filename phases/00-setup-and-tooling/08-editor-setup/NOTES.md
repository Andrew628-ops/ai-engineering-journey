# Lesson 08: Editor Setup

Date: 2026-10-24
Editor: VS Code
Notebook interface: Google Colab
Quiz: first attempt **2/3**; retake **3/3**.

## My setup

I reported installing these VS Code extensions:

| Extension | Purpose |
|-----------|---------|
| Python (Microsoft) | Python editing, interpreter selection, and execution support |
| Pylance (Microsoft) | Type checking, autocomplete, and code diagnostics |
| Black Formatter (Microsoft) | Consistent Python formatting |
| Ruff (Astral) | Linting, including unused-import checks |

I chose to keep using Google Colab for notebooks, so the VS Code Jupyter extension was deferred.

Practice file: [editor_practice.py](editor_practice.py).

## Selecting the interpreter

1. Press **Ctrl+Shift+P**.
2. Choose **Python: Select Interpreter**.
3. Select the repository's interpreter:

```text
/home/student/ai/ai-engineering-journey/.venv/bin/python
```

If needed, use **Enter interpreter path…** to select it explicitly. Check the full path rather than relying only on the environment's display name.

The selected interpreter tells Python tooling which environment to use. An existing terminal may still have a different environment activated. Notebook kernels are selected separately.

## Basic type checking with Pylance

To enable it:

1. Open Settings with **Ctrl+,**.
2. Search for `@id:python.analysis.typeCheckingMode`.
3. Set the value to **basic**.

I tested:

```python
def double(value: int) -> int:
    return value * 2


answer = double("hello")
```

Pylance reported that `Literal['hello']` could not be assigned to the `int` parameter `value`.

I corrected the call:

```python
answer = double(10)
```

The expected value of `answer` is `20`.

Type annotations help a checker identify likely mistakes; Python does not automatically enforce them at runtime. Basic type checking also does not generally verify arbitrary tensor shapes.

## Formatting with Black

My initial line was:

```python
numbers=[1,2,3]
```

Saving initially left it unchanged. I selected Black explicitly for the Python file:

1. Open the Command Palette with **Ctrl+Shift+P**.
2. Choose **Format Document With…**.
3. Choose **Configure Default Formatter… → Black Formatter**.
4. Run **Format Document** to test it.

Black changed the line to:

```python
numbers = [1, 2, 3]
```

Then I enabled automatic formatting:

1. Open Settings.
2. Search for `@id:editor.formatOnSave`.
3. Enable the checkbox.
4. Make the spacing uneven again and press **Ctrl+S**.

I confirmed that saving automatically reformatted the line. Formatting controls code layout; it does not fix incorrect logic or argument types.

## Linting with Ruff

I added an unused import:

```python
import math
```

Ruff reported:

```text
math imported but unused
Ruff F401
```

**F401** identifies an unused import. A suggested fix can be opened by placing the cursor on the diagnostic and pressing **Ctrl+.**, then selecting **Remove unused import**. The diagnostic was observed; applying the quick fix was not explicitly confirmed during the session.

## Choosing the right tool

| Situation | Tool |
|-----------|------|
| Passing a string where an integer is expected | Pylance |
| Inconsistent spaces or code layout | Black Formatter |
| An import that is never used | Ruff |

Ruff also offers formatting features, but this session used Black for formatting and Ruff for linting.

## Notebooks and output scrolling

I will use **VS Code for Python scripts** and **Google Colab for notebooks**.

For future VS Code notebook work, `notebook.output.scrolling` keeps long cell output in a scrollable area. This prevents thousands of training-log lines from making a cell extremely tall.

It does **not** enable smooth-scrolling animations. This setting was explained, but not configured or tested because I chose Colab.

## Remote SSH

The **Remote SSH** extension lets VS Code open files, run terminals, and debug on an authorized remote machine, such as a GPU server.

The editor interface is on my computer, but the remote Python script runs on the **remote server**. The remote machine needs its own suitable environment and dependencies.

Remote SSH was discussed conceptually. No remote connection or extension installation was verified in this session.

## Quiz and reflection

- First attempt: **2/3**. I confused notebook output scrolling with smooth-scrolling animations.
- Retake: **3/3**. I correctly identified Remote SSH, output scrolling, and basic type checking.
- Editor Setup's quiz review item was cleared; the original attempt remains in the learning log.
- Manual formatting worked before format-on-save was verified. Selecting the Python formatter explicitly helped resolve the issue.

These practice results were reported during the lesson; editor settings were not inspected directly.

Next lesson: **Data Management**.
