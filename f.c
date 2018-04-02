#include <stdio.h>
int f(int x, int y)
{
	//printf("x:%d,y:%d\n",x,y);
	if (y == 0){
		return x;
	}else{
		return f(y, x % y);
	}
}

int main()
{
	printf("ans:%d\n",f(775,527));
	return 0;
}
