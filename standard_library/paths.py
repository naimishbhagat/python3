from pathlib import Path
# absolute path windows
Path(r"C:\Program Files\Microsoft")
# absolute path mac
Path("/usr/local/bin")
# current folder
Path()
Path("ecommerce/__init__.py")
# combine path
Path() / "ecommerce" / "__init__.py"
# home directory of user
print(Path.home())

path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)  # __init__.py
print(path.stem)  # __init__
print(path.suffix)  # .py
print(path.parent)  # ecommerce
path = path.with_name("file.txt")
print(path)
print(path.absolute())  # /Users/naimish/Sites/HelloWorld/ecommerce/file.txt
path = path.with_suffix(".txt")
print(path)
