# Comprehensions

# handle file & directory

import os
import glob
import time
from approximate_size import approximate_size

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
print(glob.glob("*.py"))  # find out .py in dive_to_python3

# Read meta_data of file
metadata = os.stat("comprehensions.py")
print(metadata.st_mtime)
print(time.localtime(metadata.st_mtime))
print(metadata.st_size)
print(approximate_size(metadata.st_size))

# Get absolute path of file
print(os.getcwd())
print(os.path.realpath("comprehensions.py"))

# List Comprehensions
# mapping
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 8]
print([element * 3 for element in a_list])
print(a_list)
a_list = [element * 3 for element in a_list]
print(a_list)

result_glob = glob.glob("*.py")
print([os.path.realpath(f) for f in result_glob])

# filter
print([f for f in result_glob if os.stat(f).st_size > 5000])  # ['data_type.py]
print([(os.stat(f).st_size, os.path.realpath(f)) for f in result_glob])
print(
    [(approximate_size(os.stat(f).st_size), os.path.realpath(f)) for f in result_glob]
)

# Dict comprehension
# mapping
metadata_dict = {f: os.stat(f) for f in result_glob}
print(type(metadata_dict))
print(list(metadata_dict.keys()))
print(metadata_dict["comprehensions.py"].st_size)

# filter
humansize_dict = {
    os.path.splitext(f)[0]: approximate_size(meta.st_size)
    for f, meta in metadata_dict.items()
    if meta.st_size > 1000
}
print(list(humansize_dict.keys()))
print(humansize_dict["comprehensions"])

# exchange value for key
# only if immutable data
a_dict = {"a": 1, "b": 2, "c": 3}
print({value: key for key, value in a_dict.items()})

# b_dict = {"a": [1, 2, 3], "b": 4, "c": 5}
# {value: key for key, value in b_dict.items()}
# TypeError: unhashable type: 'list'

# Set comprehensions
a_set = set(range(10))
print(a_set)

print({x ** 2 for x in a_set})
print({x for x in a_set if x % 2 == 0})
print({2 ** x for x in range(10)})  # not only set

