/*
 * Computer of Total Resistance
 */

#include <stdio.h>

float r1, r2, rt;

float totalR(float r1, float r2);

int main(int argc, char *argv[]){
    if(argc>1){
        r2 = atoi(argv[1]);
        r1 = atoi(argv[2]);
    } else {
        r2 = 1.0;
        r1 = 1.0;
    }
    // Compute total Resistance
    rt = totalR(r1, r2);

    // Print result
    printf("Resistencia Total: %f\n", rt);

    return (0);
}


float totalR(float r1, float r2){
    float rt;
    rt = (1.0f/r1) + (1.0f/r2);
    return rt;
}