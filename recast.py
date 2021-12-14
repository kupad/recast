import ctypes

# Load the shared library
recast = ctypes.CDLL("./librecast.so")
recast.int2float.restype = ctypes.c_float
recast.bytes2float.restype = ctypes.c_float

f = recast.int2float(0xdeadbeef)
print(f)

f = recast.bytes2float(b'aaaa')
print(f)


