# terminalexecutepy

`terminalexecutepy` provides a high‑level Python interface for running terminal commands, managing shells, executing scripts, and performing common developer tasks. It wraps Python’s `subprocess` module with a clean, ergonomic API and includes OS‑aware shell selection for Windows and Unix systems.

---

## Features

- OS‑aware shell selection (`cmd`, `powershell`, `bash`, `zsh`, `sh`)
- Execute any terminal command with automatic error handling
- Convenience helpers:
  - `echo()` for quick output
  - `pip()` for install, uninstall, list, upgrade
  - `clear()` for screen clearing
  - `list_dir()` for directory listing
  - `chdir()` and `get_cwd()` for navigation
  - `run_script()` for executing script files
- File and directory utilities:
  - `make_dir()`, `remove_file()`, `remove_dir()`, `copy_file()`, `move()`
- System information:
  - `whoami()`, `env()`, `cpu_info()`, `memory_info()`
- Network helpers:
  - `ping()`, `ipconfig()`, `curl()`
- Git helpers:
  - `git_clone()`, `git_status()`, `git_pull()`, `git_commit()`, `git_push()`
- Works on Windows, macOS, and Linux
- No external dependencies

---

## Installation

Install from PyPI:

```bash
pip install terminalexecutepy
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/ahk4918/terminalExecutepy.git
```

## Usage

Importing

```python
from terminalExecutepy.terminalExecute import Terminal, Shells
```

Basic Example:

```python
term = Terminal()
term.echo("Hello from terminalexecutepy!")
```

Selecting a Shell:
```python
# Windows
term.shell = Shells.CMD
term.shell = Shells.POWERSHELL

# Unix
term.shell = Shells.BASH
```

Running Commands:

```python
term.run("echo Running a command")
```

Using the pip command:

```python
term.pip("install", "requests")
term.pip("list")
term.pip("upgrade", "pip")
term.pip("uninstall", "somepackage")
```

Directory Tools:

```python
term.list_dir()
term.chdir("..")
term.get_cwd()
term.make_dir("newfolder")
term.copy_file("a.txt", "backup/a.txt")
term.move("backup/a.txt", "a.txt")
term.remove_file("old.txt")
```

System Info:

```python
term.whoami()
term.env()
term.cpu_info()
term.memory_info()
```

Network Commands:

```python
term.ping("google.com")
term.ipconfig()
term.curl("https://example.com")
```

Git Commands:

```python
term.git_clone("https://github.com/user/repo.git")
term.git_status()
term.git_pull()
term.git_commit("Updated project")
term.git_push()
```

Running Scripts:

```python
term.run_script("myscript.sh")
```
