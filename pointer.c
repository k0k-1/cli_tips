#include <stdio.h>

int main()
{
    char *x;
    int i;
    x = "fuck";
    for(i=0;i<5;i++){
        printf("%c",*x);
        x++;
    }
}
