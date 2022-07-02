"""
STRING CONCATENATION

String concatenation involves joining two or more strings together.

02-07-2022

Read more: https://realpython.com/python-f-strings/

"""

import time

string_1 = "Human"
string_2 = "Body"

def add(string1, string2):
    return string1 + " " + string2

def join(string1, string2):
    return " ".join([string1, string2])

def per_format(string1, string2):
    return "%s %s" %(string1, string2)

def str_format(string1, string2):
    return "{} {}".format(string1, string2)

def f_string_format(string1, string2):
    return f"{string1} {string2}"


start_1 = time.perf_counter()
function_1 = add(string_1, string_2)
end_1 = time.perf_counter()

start_2 = time.perf_counter()
function_2 = join(string_1, string_2)
end_2 = time.perf_counter()

start_3 = time.perf_counter()
function_3 = per_format(string_1, string_2)
end_3 = time.perf_counter()

start_4 = time.perf_counter()
function_4 = str_format(string_1, string_2)
end_4 = time.perf_counter()

start_5 = time.perf_counter()
function_5 = str_format(string_1, string_2)
end_5 = time.perf_counter()

print(function_1, ": OPERATION: (+)               " f"executed in {end_1 - start_1} seconds")
print(function_2, ": OPERATION: (join)            " f"executed in {end_2 - start_2} seconds")
print(function_3, ": OPERATION: (%)               " f"executed in {end_3 - start_3} seconds")
print(function_4, ": OPERATION: (str.format)      " f"executed in {end_4 - start_4} seconds")
print(function_5, ": OPERATION: (f-string format) " f"executed in {end_5 - start_5} seconds")
