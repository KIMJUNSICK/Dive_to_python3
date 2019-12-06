# Comprehensions

# handle file & directory

import os
import glob

# handle current work directory
current_path = os.getcwd()
print(current_path)
os.chdir  # change directory

# handle directory name
print(os.path.join(current_path, "junsik"))
print(os.path.join(current_path, "\junsik"))
print(os.path.expanduser("~"))  # path to user's home # /home/junsik
print(
    os.path.join(current_path, "junsik", "jeongmin", "sewon")
)  # no limit for number of args

# split file from dir
print(os.path.split(current_path))
# put two args into tuple at once
current_path_plus_extension = os.getcwd() + "/conprehensions.py"
print(current_path_plus_extension)
(dirname, filename) = os.path.split(current_path_plus_extension)
print(dirname)
print(filename)

# split filename from extension
(shortname, extension) = os.path.splitext(filename)
print(shortname)
print(extension)

# Read dir
print(os.getcwd())  # /home/junsik/projects/dive_to_python3
print(glob.glob("*.py"))

