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
