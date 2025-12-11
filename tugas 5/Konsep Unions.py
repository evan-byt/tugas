#4.konsep union
from ctypes import Union, c_int, c_float, c_char

class DataUnion(Union):
    _fields_ = [("i", c_int), ("f", c_float), ("c", c_char)]

data = DataUnion()
data.i = 10
print("Union Integer:", data.i)

data.f = 3.14
print("Union Float:", data.f)