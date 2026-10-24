#include <stdio.h>

int main() {
  //
#ifdef _WIN32
  // This macro is defined when compiling on both Windows 32 & 64 bit systems
  printf("Hello, from Windows!\n");

#elif __linux__
  // This macro is defined when compiling on most Linux distributions
  printf("Hello, from Linux!\n");

#elif __APPLE__
  // This macro is defined when compiling on both Apple systems(MacOS)
  printf("Hello, from MacOS!\n");

#else
  // Fallback if the OS is not recognized
  printf("Hello, from Unknown OS!\n");
#endif

  return 0;
}
