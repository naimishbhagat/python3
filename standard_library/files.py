from pathlib import Path
from time import ctime
import shutil

path = Path("../ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
print(path.stat())
print(ctime(path.stat().st_ctime))
print(path.read_text())
with open("__init__.py", "r") as file:
    print("File opened")
path.write_text("...")
# path.write_bytes()

source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"
shutil.copy(source, target)
# target.write_text(source.read_text())
