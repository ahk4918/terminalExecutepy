# terminalexecutepy

`terminalexecutepy` provides a high‑level Python interface for running terminal commands, managing shells, executing scripts, and performing common developer tasks such as pip operations, directory navigation, and environment inspection. It wraps Python’s `subprocess` module with a cleaner, more ergonomic API and includes OS‑aware shell selection for Windows and Unix systems.

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
- Works on Windows, macOS, and Linux
- No external dependencies

---

## Installation

Install from PyPI:

```bash
pip install terminalexecutepy
```

## Usage

Basic Example:

```python
from terminalexecutepy import Terminal, Shells

term = Terminal()
term.echo("Hello from terminalexecutepy!")
```

Selecting a Shell:

```python
# Windows
term.shell = Shells.CMD
# or
term.shell = Shells.POWERSHELL

# Unix
term.shell = Shells.BASH

```

Using the pip command:

```python
term.pip("install", "requests")
term.pip("list")
term.pip("upgrade", "pip")
term.pip("uninstall", "somepackage")
```

Directory tools:

```python
term.list_dir()
term.chdir("..")
term.get_cwd()
```

Running Scripts:

```python
term.run_script("myscript.sh")
```
