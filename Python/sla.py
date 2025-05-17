#include <stdio.h>
int main(){
 int n;
 while(1){   
 printf("Entre com um valor maior que 8:");
 scanf("%d",&n);
 if(n<8) break;
 int i;
 int a[n+1]; //quantidade de 3's'
 int b[n+1]; //quantidade de 5's'
 a[8] = 1;
 b[8] = 1;
 a[9] = 3;
 b[9] = 0;
 a[10] = 0;
 b[10] = 2;
 for(i=11;i<=n;i++){
    a[i] = a[i-3]+1;
    b[i] = b[i-3];
 }
 printf("%d=3*%d + 5*%d\n",n,a[n],b[n]);
 }
 return 0;
}
