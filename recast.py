import ctypes

# Load the shared library
_recast = ctypes.CDLL("./librecast.so")
_recast.int2float.restype = ctypes.c_float
_recast.bytes2float.restype = ctypes.c_float
_recast.float2bytes.restype = ctypes.c_char_p


def int2float(x):
    return _recast.int2float(x)


def bytes2float(x):
    return _recast.bytes2float(x)


def float2bytes(x):
    return _recast.float2bytes(ctypes.c_float(x))


if __name__ == '__main__':
    # f = _recast.int2float(0xdeadbeef)
    # print(f)
    # f = _recast.bytes2float(b'aaaa')
    # print(f)

    b1 = b'aaaa'
    print('b1', b1)

    f = bytes2float(b1)
    print('f', f)

    b2 = float2bytes(f)
    print('b2', b2)

