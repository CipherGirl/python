import os # Provides strings for paths which is hard to use
from pathlib import Path # Provides objects for PATH (Less prone errors)

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = Path(__file__).resolve().parent.parent

# print(BASE_DIR)

# print(Path.cwd())

# for p in Path().iterdir():
#     print(p)

my_dir = Path('module_2')
my_file = Path('os_pathlib.py')

print(my_dir.name, my_file.name)

print(my_dir.suffix, my_file.suffix)

print(my_dir.stem, my_file.stem)

new_file = my_dir / "new.py" # my_dir.joinpath('new.py')

print(new_file)

print(my_dir.exists())
print(new_file.exists())

print(my_dir.parent)
print(new_file.parent)

print(my_dir.parent.absolute())
print(my_dir.absolute().parent)
print(my_dir.absolute())


dot_dot = Path('..').resolve() # Path(__file__).resolve()
print(dot_dot)

home = Path.home()  #Path('~').expanduser()

dotfiles = Path.home() / "Code" #Path('~/dotfiles').expanduser()

print(dotfiles)

for p in dotfiles.rglob("coverage-final.json"):
    print(p)

