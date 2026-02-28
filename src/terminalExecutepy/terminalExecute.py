import subprocess
import os
import sys
from enum import Enum
from typing import Optional, Literal

# 1. OS-Specific Shell Enum for Autocomplete
# Modern IDEs (VS Code, PyCharm) evaluate these blocks for dynamic suggestions.
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
        # Defaults to CMD on Windows, BASH on Unix
        self.shell = shell or (Shells.CMD if os.name == 'nt' else Shells.BASH)

    def run(self, cmd: str):
        """Runs any command in the chosen shell."""
        # PowerShell requires an explicit executable path on Windows for best results
        is_powershell = (
            (isinstance(self.shell, str) and self.shell.lower() == "powershell") or 
            (hasattr(self.shell, "name") and self.shell.name == "POWERSHELL")
        )
        
        exe = "powershell.exe" if is_powershell else None
        
        try:
            # shell=True allows executing strings with pipes and environment variables
            subprocess.run(cmd, shell=True, check=True, executable=exe)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
    def echo(self, message: str):
        """Convenience method for echoing messages."""
        self.run(f'echo {message}')

    def pip(self, action: Literal["install", "uninstall", "list", "upgrade"], pkg: str = ""):
        """
        Simplified pip manager.
        The action parameter provides dropdown options in 2026 IDEs.
        """
        flags = "-y" if action == "uninstall" else ""
        if action == "upgrade":
            pip_cmd = f"install --upgrade {pkg}"
        else:
            pip_cmd = f"{action} {pkg}"
            
        self.run(f'"{sys.executable}" -m pip {pip_cmd} {flags}')

    def clear(self):
        """Clears the terminal screen."""
        self.run("cls" if os.name == 'nt' else "clear")
    
    def list_dir(self, path: str = "."):
        """Lists directory contents."""
        self.run(f'dir {path}' if os.name == 'nt' else f'ls {path}')
    
    def chdir(self, path: str):
        """Changes the current working directory."""
        os.chdir(path)
        self.echo(f"Changed directory to {path}")
    
    def get_cwd(self):
        """Prints the current working directory."""
        self.echo(os.getcwd())
    
    def run_script(self, script_path: str):
        """Runs a script file."""
        if not os.path.isfile(script_path):
            print(f"Error: {script_path} does not exist.")
            return
        
        self.run(f'"{script_path}"')
# --- Usage Example ---
if __name__ == "__main__":
    term = Terminal()

    # 1. Autocomplete works here: type 'Shells.' to see OS-specific options
    term.shell = Shells.CMD  # Autocomplete suggests "CMD" and "POWERSHELL" on Windows, "BASH", "ZSH", "SH" on Unix
    term.echo("Easy Mode Active")

    # 2. Assigning by string also works
    # term.shell = "powershell" 

    # 3. Pip is now a single consolidated method
    # IDE suggests: "install", "uninstall", "list", "upgrade"
    term.pip("list")