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

# Insert a specific value into strings
username = "junsik"
password = "12"
print("{0}'s password is {1}".format(username, password))
print(f"{username}'s password is {password}")

# Compound Field Names
SUFFIXES = {
    1000: ["KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"],
    1024: ["KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"],
}

# python syntax work in replacement field
print(SUFFIXES[1000])
print("1000{0[0]} = 1{0[1]}".format(SUFFIXES[1000]))

# Format Specifiers
print("{0:.1f} {1}".format(698.24, "GB"))

# other string method
s = """Finished files are the re-
sult of years of scientif-
ic study combined with the
experience of years."""

print(s.splitlines())
print(s.lower())
print(s.lower().count("f"))

query = "user=pilgrim&database=master&password=PapayaWhip"
a_list = query.split("&")

print(a_list)  # ['user=pilgrim', 'database=master', 'password=PapayaWhip']

a_list_of_lists = [value.split("=", 1) for value in a_list if "=" in value]
print(a_list_of_lists)
a_dict = dict(a_list_of_lists)
print(a_dict)
