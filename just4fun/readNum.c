/*
 * Read Numbers
 *
 * @brief A program that writes down the pronuntiation of each number
 *
 * @author Mario Garcia
 * www.mayitzin.com
 */

#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]){
    int num = atoi(argv[1]);
    int nDigits;

    if (num==0){
        nDigits = 1;
    } else {
        nDigits = floor(log10(abs(num))) + 1;
    }

    printf("%d\n", num);
    printf("%d\n", nDigits);

    return (0);
}