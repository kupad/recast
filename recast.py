import ctypes

# Load the shared library
_recast = ctypes.CDLL("./librecast.so")
_recast.int2float.restype = ctypes.c_float
_recast.bytes2float.restype = ctypes.c_float
_recast.strtod_wrap.restype = ctypes.c_double
_recast.float2bytes.restype = ctypes.c_char_p


def int2float(x):
    return _recast.int2float(x)


def bytes2float(b):
    return _recast.bytes2float(b)


def float2bytes(x):
    return _recast.float2bytes(ctypes.c_float(x))


def strtod(s):
    s = s.encode('utf-8')
    return _recast.strtod_wrap(s)


if __name__ == '__main__':
    # f = _recast.int2float(0xdeadbeef)
    # print(f)
    # f = _recast.bytes2float(b'aaaa')
    # print(f)

    b1 = b'abcd'
    print('b1', b1)

    f = bytes2float(b1)
    print('f', f)

    b2 = float2bytes(f)
    print('b2', b2)

