#include <stdint.h>

float int2float(const uint32_t in) {
    float mem; 
    uint32_t* p = (uint32_t*)&mem;
    *p = in;
    return mem;
}

uint32_t float2int(const float in) {
    uint32_t mem; 
    float* p = (float*)&mem;
    *p = in;
    return mem;
}


float bytes2float(const unsigned char* in) {
    float mem; 
    unsigned char* p = (unsigned char*)&mem;
    for(int i=0; i < sizeof(float); i++) {
        *(p+i) = in[i];
    }

    return mem;
}

