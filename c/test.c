#include <stdio.h>
#include <stdint.h>
#include "recast.h"

int main() {
    printf("%f\n", int2float(0xdeadbeef));
    printf("%f\n", int2float(0xcafebabe));
    return 0;
}

