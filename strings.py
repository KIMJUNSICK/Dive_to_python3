# Strings

# natural lang -> encoding with method like unicode ->
# decoding -> natural lang again

# UTF-32 = 8*4 bit = 4byte(1byte = 8bit)
# but UTF-32 is so heavy for encoding natural lang

# so we human invented UTF-8
# this is variable-length unicode system.
# so when strings is longer, it takes a lot of time for operation.
# but because of extension of this system, better than UTF-32

# basic
string1 = "準植 Python"
print(len(string1))  # 9
print(string1[0])  # "準"
print(string1 + "3")  # "準植 Python3"
