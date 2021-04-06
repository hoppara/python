import sys
from pathlib import Path
from subprocess import call

# pdf2txt.py 
py_path = Path(sys.exec_prefix) / "Scripts" / "pdf2txt.py"

# pdf2txt.py call
call(["py", str(py_path), "-o extract-sample.txt", "-p 1", "sample.pdf"])