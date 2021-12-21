import sys
import struct
from functools import partial


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


def float2bytes(f, byteorder=sys.byteorder):
    return struct.pack(endian(byteorder) + 'f', f)


def float2int(f, byteorder=sys.byteorder):
    return bytes2int(float2bytes(f, byteorder))


def float2uint(f, byteorder=sys.byteorder):
    return bytes2uint(float2bytes(f, byteorder))
