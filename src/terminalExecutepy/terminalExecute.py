import subprocess
import os
import sys
from enum import Enum
from typing import Optional, Literal

# OS-Specific Shell Enum
if os.name == 'nt':
    class Shells(str, Enum):
        CMD = "cmd"
        POWERSHELL = "powershell"
else:
    class Shells(str, Enum):
        BASH = "bash"
        ZSH = "zsh"
        SH = "sh"

class Terminal:
    def __init__(self, shell: Optional[Shells] = None):
        self.shell = shell or (Shells.CMD if os.name == 'nt' else Shells.BASH)

    def run(self, cmd: str):
        is_powershell = (
            (isinstance(self.shell, str) and self.shell.lower() == "powershell") or 
            (hasattr(self.shell, "name") and self.shell.name == "POWERSHELL")
        )
        exe = "powershell.exe" if is_powershell else None

        try:
            subprocess.run(cmd, shell=True, check=True, executable=exe)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    # -------------------------
    # BASIC COMMANDS
    # -------------------------
    def echo(self, message: str):
        self.run(f'echo {message}')

    def clear(self):
        self.run("cls" if os.name == 'nt' else "clear")

    def list_dir(self, path: str = "."):
        self.run(f'dir {path}' if os.name == 'nt' else f'ls {path}')

    def chdir(self, path: str):
        os.chdir(path)
        self.echo(f"Changed directory to {path}")

    def get_cwd(self):
        self.echo(os.getcwd())

    def run_script(self, script_path: str):
        if not os.path.isfile(script_path):
            print(f"Error: {script_path} does not exist.")
            return
        self.run(f'"{script_path}"')

    # -------------------------
    # PIP COMMANDS
    # -------------------------
    def pip(self, action: Literal["install", "uninstall", "list", "upgrade"], pkg: str = ""):
        flags = "-y" if action == "uninstall" else ""
        if action == "upgrade":
            pip_cmd = f"install --upgrade {pkg}"
        else:
            pip_cmd = f"{action} {pkg}"
        self.run(f'"{sys.executable}" -m pip {pip_cmd} {flags}')

    # -------------------------
    # NEW: FILE & DIRECTORY UTILITIES
    # -------------------------
    def make_dir(self, name: str):
        os.makedirs(name, exist_ok=True)
        self.echo(f"Created directory: {name}")

    def remove_file(self, path: str):
        if os.path.isfile(path):
            os.remove(path)
            self.echo(f"Deleted file: {path}")
        else:
            print(f"Error: {path} does not exist.")

    def remove_dir(self, path: str):
        if os.path.isdir(path):
            os.rmdir(path)
            self.echo(f"Deleted directory: {path}")
        else:
            print(f"Error: {path} does not exist.")

    def copy_file(self, src: str, dst: str):
        if os.path.isfile(src):
            import shutil
            shutil.copy(src, dst)
            self.echo(f"Copied {src} → {dst}")
        else:
            print(f"Error: {src} does not exist.")

    def move(self, src: str, dst: str):
        import shutil
        shutil.move(src, dst)
        self.echo(f"Moved {src} → {dst}")

    # -------------------------
    # NEW: SYSTEM INFORMATION
    # -------------------------
    def whoami(self):
        self.run("whoami" if os.name != 'nt' else "echo %USERNAME%")

    def env(self):
        self.run("env" if os.name != 'nt' else "set")

    def cpu_info(self):
        if os.name == 'nt':
            self.run("wmic cpu get name")
        else:
            self.run("lscpu")

    def memory_info(self):
        if os.name == 'nt':
            self.run("wmic memorychip get capacity")
        else:
            self.run("free -h")

    # -------------------------
    # NEW: NETWORK COMMANDS
    # -------------------------
    def ping(self, host: str):
        self.run(f"ping {host}")

    def ipconfig(self):
        self.run("ipconfig" if os.name == 'nt' else "ifconfig")

    def curl(self, url: str):
        self.run(f"curl {url}")

    # -------------------------
    # NEW: GIT COMMANDS
    # -------------------------
    def git_clone(self, repo: str):
        self.run(f"git clone {repo}")

    def git_status(self):
        self.run("git status")

    def git_pull(self):
        self.run("git pull")

    def git_commit(self, message: str):
        self.run(f'git commit -am "{message}"')

    def git_push(self):
        self.run("git push")


# Example usage
if __name__ == "__main__":
    term = Terminal()
    term.echo("Terminal Ready")
