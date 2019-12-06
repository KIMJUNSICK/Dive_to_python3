# Comprehensions

# handle file & directory

import os


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

