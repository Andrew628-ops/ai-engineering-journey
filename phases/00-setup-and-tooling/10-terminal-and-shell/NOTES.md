# Lesson 10: Terminal & Shell

Date: 2026-10-24
Shell: zsh (`/bin/zsh`)
Quiz: first attempt **2/3**; retake **3/3**.

## Terminal and shell

The terminal is the interface where I type commands. The shell interprets them.

```bash
echo "$SHELL"
pwd
```

`$SHELL` showed my configured login shell, `/bin/zsh`. `pwd` showed the current directory.

My practice folder is `phases/00-setup-and-tooling/10-terminal-and-shell`.

## Reading and filtering logs

I created [fake_train.log](fake_train.log) with these initial lines:

```text
epoch 1 loss: 0.90
epoch 2 loss: 0.65
WARNING learning rate is high
epoch 3 loss: 0.42
ERROR dataset file missing
```

```bash
cat fake_train.log
grep "loss" fake_train.log
grep "loss" fake_train.log | wc -l
```

- `cat` prints the file.
- `grep` selects matching lines.
- `|` sends stdout from one command to stdin of the next.
- `wc -l` counts newline characters; these matching log lines produced a count of **3**.

The trailing `%` initially shown by zsh indicated that the file lacked a final newline; it was not log content.

## Extracting fields

```bash
grep "loss" fake_train.log | awk '{print $NF}'
```

`awk` splits each input line into fields. `$NF` selects its last field.

Observed output:

```text
0.90
0.65
0.42
```

## Overwriting and appending

```bash
grep "loss" fake_train.log | awk '{print $NF}' > losses.txt
cat losses.txt
echo "0.30" >> losses.txt
```

| Operator | Meaning |
|----------|---------|
| `>` | Redirect stdout to a file, replacing existing contents |
| `>>` | Append stdout to a file |
| `2>` | Redirect stderr to a file |
| `2>&1` | Send stderr to stdout's current destination |

After appending `0.30`, `losses.txt` contained four lines.

## stdout and stderr

My [streams.py](streams.py) exercise used:

```python
import sys

print("Training started")
print("Dataset missing", file=sys.stderr)
```

Separate streams:

```bash
python streams.py > output.log 2> errors.log
```

- `output.log` contained `Training started`.
- `errors.log` contained `Dataset missing`.

Combined streams:

```bash
python streams.py > combined.log 2>&1
cat combined.log
```

Both messages appeared in `combined.log`. Their order can differ because stdout and stderr may be buffered differently. Redirect order matters: first redirect stdout to the file, then send stderr to that destination.

## Watching a growing log

```bash
tail -n 2 fake_train.log
tail -f fake_train.log
```

`tail -n 2` prints the last two lines. `tail -f` keeps watching for appended content.

In a second terminal in the same directory, I ran:

```bash
echo "epoch 4 loss: 0.30" >> fake_train.log
```

The appended line appeared in the log-watching terminal. **Ctrl+C** stops the watcher without deleting the file. An accidental `Run tail -` fragment appeared in the reported log output; cleanup was suggested but not verified.

## Background jobs and process IDs

```bash
sleep 60 &
jobs
```

Observed output included:

```text
[1] 315801
[1]  + running    sleep 60
```

- `&` starts a command in the background.
- `[1]` was the shell's job number.
- `315801` was that process's PID; future runs have different PIDs.
- `jobs` lists jobs tracked by the current shell.

I brought the job into the foreground:

```bash
fg %1
```

After stopping it with **Ctrl+C**, I confirmed that `jobs` was empty.

Backgrounding with `&` does not reliably protect a program when the terminal closes.

## nohup and tmux

Example, discussed rather than executed:

```bash
nohup python train.py > train.log 2>&1 &
```

`nohup` protects against the hangup signal. Output can be inspected in a log, but it does not provide an interactive session to reattach to.

tmux supports persistent interactive sessions and multiple panes:

```bash
tmux new -s training
tmux attach -t training
```

In tmux, **Ctrl+B**, then **d**, detaches without stopping the running program. Reattaching returns to the session. This does not protect against machine shutdown, restart, or other termination.

`command -v tmux` and `command -v htop` returned no paths. Attempting to start tmux gave `command not found`. Because my student account lacks sudo, these tools were not installed during the lesson. tmux was traced conceptually, not tested.

`top` was suggested as a possible available process monitor, with **q** to exit; execution was not confirmed.

## Remote file transfers

These commands were traced only; they require an authorized remote server.

Copy a local file to a server:

```bash
scp metrics.json student@server:~/results/
```

Copy a remote file to my current local directory:

```bash
scp student@server:~/results/metrics.json .
```

The final `.` means the current directory. Read these commands as **source → destination**.

Synchronize a directory:

```bash
rsync -av ./data/ student@server:~/data/
```

rsync can avoid retransferring unchanged files. Here, the trailing slash on `./data/` means copy the directory's contents.

## SSH local port forwarding

```bash
ssh -L 8888:localhost:8888 user@gpu-box
```

This forwards local port **8888** through SSH to **localhost:8888 as seen from the remote server**. While the connection is open, my browser can use `http://localhost:8888` to reach a remote Jupyter server, subject to its authentication and configuration.

`-L` is the local-forwarding option. `--forward-port` is not the syntax used here. No remote SSH connection or forwarding was tested.

## Session aliases

I defined a shortcut:

```bash
alias here='pwd'
```

At the next prompt:

```bash
alias here
```

Output: `here=pwd`.

Running `here` at a new prompt then printed:

```text
/home/student/ai/ai-engineering-journey/phases/00-setup-and-tooling/10-terminal-and-shell
```

The first attempt reported `command not found`; defining and invoking the alias at separate prompts worked. This alias lasts for the current shell session. No persistent `.zshrc` edit was performed.

## Quiz and reflection

- First attempt: **2/3**. I correctly answered tmux and combined redirection, but missed SSH forwarding syntax.
- Retake: **3/3**. I correctly recalled all three concepts, including `ssh -L`.
- The quiz review item was cleared; the original attempt remains in the learning log.
- I practised log filtering, pipes, field extraction, redirects, log watching, background jobs, and aliases locally.
- Results were learner-reported. tmux, remote transfers, and SSH forwarding remain practical follow-up work when tools and authorized access are available.

Next lesson: **Linux for AI**.
