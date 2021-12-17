import ctypes
import sys
import struct
from functools import partial


# Load the shared library
_recast = ctypes.CDLL("./librecast.so")
_recast.int2float.restype = ctypes.c_float
_recast.bytes2float.restype = ctypes.c_float
_recast.strtod_wrap.restype = ctypes.c_double
_recast.float2bytes.restype = ctypes.c_char_p


def unpack(fmt, b):
    return struct.unpack(fmt, b)[0]


bytes2short = partial(unpack, 'h')
bytes2ushort = partial(unpack, 'H')
bytes2int = partial(unpack, 'i')
bytes2uint = partial(unpack, 'I')
bytes2long = partial(unpack, 'l')
bytes2ulong = partial(unpack, 'L')
bytes2longlong = partial(unpack, 'q')
bytes2ulonglong = partial(unpack, 'Q')
bytes2ssize_t = partial(unpack, 'n')
bytes2size_t = partial(unpack, 'N')
bytes2half = partial(unpack, 'e')  # half float
bytes2float = partial(unpack, 'f')
bytes2double = partial(unpack, 'd')
bytes2voidptr = partial(unpack, 'P')  # ???


def endian(order):
    return '<' if order == 'little' else '>'


def int2uint(i, byteorder=sys.byteorder):
    return bytes2uint(i.to_bytes(4, byteorder, signed=True))


def int2float(i, byteorder=sys.byteorder):
    return bytes2float(i.to_bytes(4, byteorder, signed=True))


def uint2int(ui, byteorder=sys.byteorder):
    return bytes2int(ui.to_bytes(4, byteorder))


def uint2float(ui, byteorder=sys.byteorder):
    return bytes2float(ui.to_bytes(4, byteorder))


def float2bytes(x, byteorder=sys.byteorder):
    return struct.pack(endian(byteorder) + 'f', f)


def float2int(f, byteorder=sys.byteorder):
    return bytes2int(float2bytes(f, byteorder))


def float2uint(f, byteorder=sys.byteorder):
    return bytes2uint(float2bytes(f, byteorder))


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

    print('b3', uint2int(0xdeadbeef))
    print('b4', hex(int2uint(-559038737)))
