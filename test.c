#include <stdio.h>
#include <stdint.h>
#include "recast.h"

int main() {
    printf("%f\n", uint32_to_float(0xdeadbeef));
    printf("%f\n", uint32_to_float(0xcafebabe));
    return 0;
}

