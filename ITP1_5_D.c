#include <stdio.h>

void
call(int n)
{
    for(int i = 1; i <= n; i++){
        int x = i;
        if(0 == x%3){
            printf(" %d", i);
            continue;
        }
        while(x){
            if(3 == x%10){
                printf(" %d", i);
                break;
            }
            x /= 10;
        }
    }
    puts("");
}

int
main(int argc, char *argv[])
{
    int n;
    scanf("%d\n", &n);

    call(n);
    return 0;
}
