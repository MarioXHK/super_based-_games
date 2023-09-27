#include <stdio.h>

int main(){
    int myNum;
    printf("GIMME NUMBERS please :)\n");
    scanf("%d", &myNum);
    printf("I looked up how to do this, wish you were here rn <3\nThis cool number you have is %d", myNum);
    printf("\nThis is a very cool thing, but it's making me dizzy.\nIt's a good thing declan gave me better glasses on this kind of thing.\nNow then, onto what we've been waiting for...");
    float ayy = 50.1f;
    float bee = 0.000001f;
    float sea;
    while (bee != 0){
        printf("GIMME A NUMBER pretty please :>)\n");
        scanf("%f", &ayy);
        printf("GIMME A NUMBER TO DIVIDE THAT NUMBER BY PLS :)\n");
        scanf("%f", &bee);
        printf("Tanks, gonna calcaclete!\n");
        if (bee != 0){
            sea = ayy/bee;
            printf("Doo bee do..... Ah! Got it!\n%f", ayy);
            printf(" divided by %f", bee);
            printf(" equals %f", sea);
            printf("!!!\nIn Order:");
            if (ayy < bee){
                printf(" %f", ayy);
                printf(" ");
                printf("%f", bee);
                printf("\n");
            }else{
                printf(" %f", bee);
                printf(" ");
                printf("%f", ayy);
                printf("\n");
            }
            if (ayy == 13 || bee == 13)
                printf("BAD LUCK!!!\n");
            printf("Odd Numbers:");
            if ((int)ayy % 2 == 1)
                printf(" %d",ayy);
            printf(" ");
            if ((int)bee % 2 == 1)
                printf(" %d",bee);
            printf("\nAlright, let's do this again!\n");
        }else{
            printf("Doo bee do..... hmm... ok...?\nIt seems that %d", ayy);
            printf("... divided by... 0..... is.....\n\n\nOH FFIUJHEDTGUIDFGBOUGISUERAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!\nWHATHAVE3OYUDOGODNEIKFDNGKLDVSHGNFDHDLFSGFD");
        }
    }
}