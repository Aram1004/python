#include <stdio.h>

unsigned int factorial(unsigned int n)
{
    if (n <= 1)
        return 1;
    else
        return n * factorial(n - 1);
}

int main(void)
{
    printf("Start\n");
    int r = factorial(5);
    printf("Result : %d\n", r);
}