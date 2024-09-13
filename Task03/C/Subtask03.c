#include <stdio.h>
int main()
{
    int n, i, k;
    printf("Enter a number: ");
    scanf("%d", &n);
    if (n % 2 == 0)
    {
        n = n + 1;
        printf("This is an even number but here's the pattern for the next number:\n");
    }
    k = n / 2;
    for (i = 0; i <= k; i++)
    {
        for (int j = 0; j < (k - i); j++)
        {
            printf(" ");
        }
        for (int j = 0; j < (2 * i + 1); j++)
        {
            printf("*");
        }
        printf("\n");
    }
    for (i = 0; i < k; i++)
    {
        for (int j = 0; j < (i + 1); j++)
        {
            printf(" ");
        }
        for (int j = 0; j < (n - 2 * (i + 1)); j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}