from pathlib import Path

path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

print(path.iterdir())
for p in path.iterdir():
    print(p)

# list generator
paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob("*.py")]
print(py_files)
print(paths)
# recursive files
py_files = [p for p in path.rglob("*.py")]
print(py_files)
