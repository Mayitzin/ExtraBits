/*
 * Read Numbers
 *
 * @brief A program that writes down the pronuntiation of each number
 *
 * @author Mario Garcia
 * www.mayitzin.com
 */

#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc, char *argv[]){
    int len = strlen(argv[1]);
    char root[len];

    strcpy(root, argv[1]);

    // NOTE: The following lines count the digits of an integer
    // int nDigits, num = atoi(argv[1]);
    // if (num==0){ nDigits = 1; }
    // else { nDigits = floor(log10(abs(num))) + 1; }

    int i, digits[len];
    for (i=0; i<len; ++i) {
        digits[i] = root[i]-'0';
        printf("%d\n", digits[i]);
    }

    return (0);
}