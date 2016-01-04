/*
 * Computer of Total Resistance
 */

#include <stdio.h>
#include <stdlib.h>

float r1, r2, rt;

float totalR(float r1, float r2);

int main(int argc, char *argv[]){
    int numElems = argc-1;
    printf("You gave %d resistor values:\n", numElems);
    if(argc>1){
        r2 = atoi(argv[1]);
        r1 = atoi(argv[2]);
    } else {
        r2 = 400.0;
        r1 = 200.0;
    }

    // Print all elements
    int i;
    float * vals = malloc(numElems * sizeof(float));
    for (i=0; i<numElems; ++i){
        // printf("%s\n", argv[i+1]);
        vals[i] = atof(argv[i+1]);
        printf("R%d :\t%2.3f\n", i, vals[i]);
    }

    // Compute total Resistance
    rt = totalR(r1, r2);

    // Print result
    printf("Resistencia Total: %f\n", rt);

    // Free memory
    free(vals);

    return (0);
}


float totalR(float r1, float r2){
    float rt;
    rt = 1.0f / ((1.0f/r1) + (1.0f/r2));
    return rt;
}