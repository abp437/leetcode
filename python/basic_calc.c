
#include <stdio.h>

int multiply(int a, int b) {
    printf("Multiplying %d * %d\n", a, b);
    return a * b;
}

int add(int a, int b) {
    printf("Adding %d + %d\n", a, b);
    return a + b;
}

int subtract(int a, int b) {
    printf("Subtracting %d - %d\n", a, b);
    return a - b;
}

float divide(int a, int b) {
    printf("Dividing %d / %d\n", a, b);
    return (float)a / b;
}

int modulo(int a, int b) {
    printf("Getting remainder %d %% %d\n", a, b);
    return a % b;
}
