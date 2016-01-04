/*
 * Computer of Total Resistance
 */

#include <stdio.h>
#include <stdlib.h>

float r1, r2, rt;

float totalR(float array[]);

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
    float vals[numElems];
    int n = sizeof(vals) / sizeof(vals[0]);
    printf("Size of array: %d\n", n);
    for (i=0; i<numElems; ++i){
        vals[i] = atof(argv[i+1]);
        printf("R_%d = %2.3f\n", i, vals[i]);
    }

    // Compute total Resistance
    printf("Number of elements: %d\n", sizeof(vals)/sizeof(vals[0]));
    // float * v = &vals[0];
    rt = totalR(vals);

    // Print result
    printf("Resistencia Total: %f\n", rt);

    return (0);
}


// float totalR(float r1, float r2){
//     float rt;
//     rt = 1.0f / ((1.0f/r1) + (1.0f/r2));
//     return rt;
// }


float totalR(float array[]){
    int i;
    int len = sizeof(array);
    // int len = sizeof(array) / sizeof(array[0]);
    printf("Number of elements: %d\n", len);
    // for (i=0; i<len; ++i){
    //     printf("R_%d = %2.3f\n", i, array[i]);
    // }
    return len;
}