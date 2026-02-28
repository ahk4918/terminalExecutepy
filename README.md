# terminalExecutepy

`terminalExecutepy` is a lightweight Python utility for executing terminal or shell commands directly from Python with clean output handling and optional error management. It simplifies subprocess usage and provides a straightforward API for running commands programmatically across Windows, macOS, and Linux.

---

## Features

- Execute terminal commands with a single function call.
- Capture output, errors, and return codes.
- Cross‑platform support.
- No external dependencies.
- Ideal for automation, scripting, and CLI tool integration.

---

## Installation

Install from PyPI:

```bash
pip install terminalExecutepy
```
Or install it from source:

```bash
pip install git+https://github.com/ahk4918/terminalExecutepy.git
```

## Usage:


Basic example:

```python
from terminalExecutepy import terminalExecute

result = terminalExecute("echo Hello World")
print(result.output)
```

Example with error handling

```python
from terminalExecutepy import terminalExecute

cmd = "dir"  # or 'ls' on Linux/macOS
result = terminalExecute(cmd)

if result.success:
    print("Command output:")
    print(result.output)
else:
    print("Command failed:")
    print(result.error)
```
