from .recast import (
    _endian,
    int2uint, int2float,
    uint2bytes, uint2int, uint2float,
    float2bytes, float2int, float2uint,
    double2bytes, double2long, double2ulong,
    ulong2bytes,
    bytes2short,
)


def test_endian():
    assert _endian('little') == '<'
    assert _endian('big') == '>'


def test_int2uint():
    assert int2uint(-1) == 0xffffffff


def test_int2float():
    assert int2float(0) == 0
    assert int2float(0x3f000000) == 0.5


def test_uint2int():
    assert uint2int(0xffffffff) == -1


def test_uint2float():
    assert uint2float(0x3f000000) == 0.5
    assert uint2float(0xbf000000) == -0.5


def test_float2bytes():
    assert float2bytes(7.7130332882300185e+31) == b'cast'


def test_float2int():
    assert float2int(7.7130332882300185e+31) == 1953718627
    assert float2int(.5) == 0x3f000000


def test_float2uint():
    assert float2uint(.5) == 0x3f000000
    assert float2uint(-.5) == 0xbf000000


def test_double2bytes():
    assert double2bytes(4.2658851707902345e-149) == b'recast!!'


def test_double2long():
    assert double2long(.5) == 0x3fe0000000000000


def test_double2ulong():
    assert double2ulong(-.5) == 0xbfe0000000000000


def test_uint2bytes():
    assert uint2bytes(0xdeadbeef, byteorder='big') == b'\xde\xad\xbe\xef'


def test_ulong2bytes():
    assert ulong2bytes(2387317316387038578) == b'recast!!'


def test_bytes2short():
    assert bytes2short(b'\x13\x37', byteorder='big') == 0x1337
