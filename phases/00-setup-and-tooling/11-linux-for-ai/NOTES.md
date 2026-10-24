# Lesson 11: Linux for AI

Date: 2026-10-24
Quiz: first attempt **1/3**; retake **3/3**.

## Filesystem and navigation

Linux organizes files under the root directory `/`. My home directory is `/home/student`, also written as `~`.

| Command | Purpose |
|---------|---------|
| `pwd` | Print the current directory |
| `cd ..` | Move to the parent directory |
| `cd ~` | Move to my home directory |
| `ls -la` | List entries, including hidden ones, with details |
| `mkdir -p path/to/folder` | Create a folder and any missing parents |
| `touch file.txt` | Create an empty file if absent, or update its timestamps if present |

I created `notes.txt`, `config.txt`, and `results.txt` in this lesson folder. All initially had size **0 bytes**, with owner and group `student`.

## Reading permissions

The initial permission string was:

```text
-rw-rw-r--
```

Read it as:

```text
- | rw- | rw- | r--
    owner group others
```

- The first `-` indicates a regular file; `d` indicates a directory.
- `r` means read.
- `w` means write.
- `x` means execute for a regular file.
- A dash means that permission is absent.

For this file, owner and group could read and write. Others could read but could not modify it. Directory permissions have different roles: for example, directory execute permission allows traversal.

## Changing permissions on my file

```bash
chmod 644 notes.txt
ls -l notes.txt
```

Observed permissions:

```text
-rw-r--r--
```

Numeric permission values are `r=4`, `w=2`, and `x=1`:

| Digit | Permissions |
|-------|-------------|
| 6 | Read + write (`rw-`) |
| 4 | Read only (`r--`) |
| 7 | Read + write + execute (`rwx`) |
| 5 | Read + execute (`r-x`) |

`644` gives the owner read/write access and everyone else read-only access. I could change permissions because I owned the file; sudo was not needed.

## Making a script executable

My [hello.sh](hello.sh) exercise contained:

```sh
#!/bin/sh
echo "Hello from Linux"
```

The first line is a **shebang**, specifying the interpreter for direct execution.

Initially, the file was empty and had no execute permission. Running it directly reported `permission denied`. I saved the contents and ran:

```bash
chmod u+x hello.sh
ls -l hello.sh
./hello.sh
```

`u+x` adds execute permission for the owner. The permission string became `-rwxrw-r--`, and the file size was 33 bytes.

Observed output:

```text
Hello from Linux
```

I also typed `./hello.s` once and got `no such file or directory`. Correcting the filename to `./hello.sh` fixed that error.

These errors have different causes. Missing execute permission can be fixed on an appropriate file I own. A wrong path needs correction. Not every permission error is solved by `chmod +x`; Docker engine access still requires administrator authorization on this machine.

## Copying and renaming

The exercise commands were:

```bash
cp hello.sh hello-backup.sh
mv hello-backup.sh hello-copy.sh
ls -l hello*.sh
```

- `cp` creates a copy.
- `mv` moves or renames a file.
- The original `hello.sh` remains because only its copy is renamed.

The lesson folder contains `hello.sh` and `hello-copy.sh`; command output for this exercise was not supplied during the lesson.

## Disk capacity versus folder usage

```bash
df -h .
du -sh .
```

| Command | Answers |
|---------|---------|
| `df` | How much capacity and free space does the filesystem have? |
| `du` | How much disk space do these files and directories use? |

The `-h` option displays human-readable units. For `du`, `-s` requests a summary.

My reported filesystem output:

```text
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p2  233G   31G  191G  14% /
```

The current lesson folder used **8.0K** at that time. Disk allocation and directory metadata can exceed the visible contents of tiny files. Available space may also differ from total capacity minus displayed usage because of filesystem reservations and rounding.

To check whether a model download will fit, use `df`. To measure a dataset folder, use `du`.

## Finding large directories

```bash
du -h --max-depth=1 . | sort -hr | head -n 20
```

1. `du` measures usage for the current directory and its immediate subdirectories.
2. `sort -hr` sorts human-readable sizes from largest to smallest.
3. `head -n 20` keeps the first 20 lines.

The total for `.` can appear in the results. `ls -la` lists entries and permissions; it does not calculate the total contents of each directory. This pipeline was explained, but its execution output was not supplied.

## Inspecting processes

```bash
ps -u student -o pid,comm,%mem --sort=-%mem | head -n 6
```

This lists my user's processes, sorted by descending memory percentage. `PID` identifies a process, `COMMAND` names it, and `%MEM` shows its percentage of physical memory.

Among the reported rows, VS Code process **197851** used the most memory at **11.2%**. An application can have multiple processes, so a single row does not represent the application's total usage. These values are a snapshot and will change.

No listed process was stopped during this exercise.

## System packages and Python packages

| Tool | Role |
|------|------|
| `apt` | Manages Ubuntu system packages |
| `uv` | Manages Python projects, environments, and packages |

Example system operation, traced only:

```bash
sudo apt install htop
```

My student account lacks sudo access, so no system package installation was attempted in this lesson. To install NumPy in a project environment, use the appropriate uv workflow instead.

## GNU sed versus macOS BSD sed

`sed` transforms text. The `-i` option edits a file in place.

GNU sed, commonly used on Linux:

```bash
sed -i 's/old/new/g' file.txt
```

Default BSD sed on macOS:

```bash
sed -i '' 's/old/new/g' file.txt
```

The macOS form requires a backup-suffix argument after `-i`. An empty string means no backup suffix. GNU sed permits `-i` without that separate argument.

Both support regular expressions and in-place editing. These commands were traced only; no files were modified with sed during the lesson.

## Quiz and reflection

- First attempt: **1/3**. Execute permission was correct; directory-size commands and sed portability needed review.
- Retake: **3/3**. I correctly recalled all three topics.
- The Linux quiz review item was cleared; the original attempt remains in the learning log.
- I corrected my interpretation of others' write permissions and the difference between `df` and `du`.
- Practical results were learner-reported. System-package installation, tmux, remote transfers, and service management were not performed.

Next lesson: **Debugging & Profiling**.
