#include <stdint.h>
#include <stdlib.h>

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

/*
void chars2float(char c1, char c2, char c3, char c4) {
    uint32_t word = c1 << 24 | c2 << 16 | c3 << 8 | c4;
    printf("%a\n", *(float*)&word);
}
*/

unsigned char* float2bytes(const float in) {
    unsigned char* mem = malloc(4); //???
    float *p = (float*)mem;
    *p = in;
    return mem;
}


