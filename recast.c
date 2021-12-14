#include <stdint.h>

float uint32_to_float(uint32_t n) {
    float f; 
    uint32_t* fp = (uint32_t*)&f;
    *fp = n;
    return f;
}

float bytes_to_float(char* s) {
    float f; 
    char* fp = (char*)&f;
    int i;
    for(i=0; i < sizeof(float); i++) {
        *(fp+i) = s[i];
    }

    return f;
}

