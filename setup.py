import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="NG-Naviguide",
    version="1.0",
    description="Facilitador de busca de Arquivos",
    options = {"build_exe": build_exe_options}, 
    executables = [Executable("caminhos.py", base=base)]
)
