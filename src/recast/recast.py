# recast - python bit recaster
# Copyright (C) 2021 Phil Dreizen and Miccah Castorina
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
# USA

import sys as _sys
import struct as _struct
from functools import partial as _partial


def _unpack(fmt, b, byteorder=_sys.byteorder):
    endian = _endian(byteorder)
    return _struct.unpack(f'{endian}{fmt}', b)[0]


bytes2short = _partial(_unpack, 'h')
bytes2ushort = _partial(_unpack, 'H')
bytes2int = _partial(_unpack, 'i')
bytes2uint = _partial(_unpack, 'I')
bytes2long = _partial(_unpack, 'l')
bytes2ulong = _partial(_unpack, 'L')
bytes2longlong = _partial(_unpack, 'q')
bytes2ulonglong = _partial(_unpack, 'Q')
bytes2ssize_t = _partial(_unpack, 'n')
bytes2size_t = _partial(_unpack, 'N')
bytes2half = _partial(_unpack, 'e')  # half float
bytes2float = _partial(_unpack, 'f')
bytes2double = _partial(_unpack, 'd')
bytes2voidptr = _partial(_unpack, 'P')  # ???


def _endian(order):
    return '<' if order == 'little' else '>'


def int2bytes(i, byteorder=_sys.byteorder):
    return i.to_bytes(4, byteorder, signed=True)


def int2uint(i, byteorder=_sys.byteorder):
    return bytes2uint(int2bytes(i, byteorder))


def int2float(i, byteorder=_sys.byteorder):
    return bytes2float(int2bytes(i, byteorder))


def uint2bytes(ui, byteorder=_sys.byteorder):
    return ui.to_bytes(4, byteorder, signed=False)


def uint2int(ui, byteorder=_sys.byteorder):
    return bytes2int(uint2bytes(ui, byteorder))


def uint2float(ui, byteorder=_sys.byteorder):
    return bytes2float(uint2bytes(ui, byteorder))


def float2bytes(f, byteorder=_sys.byteorder):
    return _struct.pack(_endian(byteorder) + 'f', f)


def float2int(f, byteorder=_sys.byteorder):
    return bytes2int(float2bytes(f, byteorder))


def float2uint(f, byteorder=_sys.byteorder):
    return bytes2uint(float2bytes(f, byteorder))


def double2bytes(d, byteorder=_sys.byteorder):
    return _struct.pack(_endian(byteorder) + 'd', d)


def double2long(d, byteorder=_sys.byteorder):
    return bytes2longlong(double2bytes(d, byteorder))


def double2ulong(d, byteorder=_sys.byteorder):
    return bytes2ulonglong(double2bytes(d, byteorder))


def ulong2bytes(u, byteorder=_sys.byteorder):
    return u.to_bytes(8, byteorder)


def ulong2double(u, byteorder=_sys.byteorder):
    return bytes2double(ulong2bytes(u, byteorder))
