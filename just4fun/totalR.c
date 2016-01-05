/*
 * Computer of Total Resistance
 *
 * @author Mario Garcia
 * www.mayitzin.com
 */

#include <stdio.h>
#include <stdlib.h>

float totalR(float array[], int size);

int main(int argc, char *argv[]){
    int i, numElems = argc-1;
    float rt, vals[numElems];
    printf("You gave %d resistor values:\n", numElems);

    // Convert and store all elements in an array of floats
    for (i=0; i<numElems; ++i) {
        vals[i] = atof(argv[i+1]);
    }

    // Compute total Resistance
    rt = totalR(vals, numElems);

    // Print result
    printf("Resistencia Total: %3.4f\n", rt);

    return (0);
}


float totalR(float array[], int size){
    int i, len = size;
    float rt, total = 0.0;
    for (i=0; i<len; ++i) {
        total += 1.0f / array[i];
    }
    rt = 1.0f / total;
    return rt;
}