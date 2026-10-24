#include <stdio.h>

// Declare the function signatures of assembly functions
// Imported from the assembly file
extern int add(int a, int b);
extern int subtract(int a, int b);
extern int multiply(int a, int b);
extern float divide(int a, int b);
extern int modulo(int a, int b);

int main(int argc, char *argv[]) {
  int num1, num2;

  printf("Enter the first number: ");
  if (scanf("%d", &num1) != 1) {
    printf("Invalid input.\n");
    return 1;
  }

  printf("Enter the second number: ");
  if (scanf("%d", &num2) != 1) {
    printf("Invalid input.\n");
    return 1;
  }

  printf("\nResults:\n");
  printf("Sum:        %d\n", add(num1, num2));
  printf("Difference: %d\n", subtract(num1, num2));
  printf("Product:    %d\n", multiply(num1, num2));

  if (num2 != 0) {
    printf("Division:   %.2f\n", divide(num1, num2));
    printf("Modulo:     %d\n", modulo(num1, num2));
  } else {
    printf("Division:   Undefined (division by zero)\n");
    printf("Modulo:     Undefined (modulo by zero)\n");
  }

  return 0;
}
