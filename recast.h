#ifndef recast_h__
#define recast_h__

#include <stdint.h>

float int2float(const uint32_t);
float float2int(const float);
float bytes2float(const unsigned char*);
unsigned char* float2bytes(const float);

#endif

