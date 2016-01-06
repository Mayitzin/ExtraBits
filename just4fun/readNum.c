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

int main(int argc, char *argv[]){
    // NOTE: The following lines count the digits of an integer (needs math.h)
    // int nDigits, num = atoi(argv[1]);
    // if (num==0){ nDigits = 1; }
    // else { nDigits = floor(log10(abs(num))) + 1; }

    int len = strlen(argv[1]);
    char root[len];
    strcpy(root, argv[1]);

    int i, digits[len];
    for (i=0; i<len; ++i) {
        digits[i] = root[i]-'0';
        printf("%d : ", digits[i]);
        switch(root[i]) {
            case '0':
                printf("zero\n");
                break;
            case '1':
                printf("one\n");
                break;
            case '2':
                printf("two\n");
                break;
            case '3':
                printf("three\n");
                break;
            case '4':
                printf("four\n");
                break;
            case '5':
                printf("five\n");
                break;
            case '6':
                printf("six\n");
                break;
            case '7':
                printf("seven\n");
                break;
            case '8':
                printf("eight\n");
                break;
            case '9':
                printf("nine\n");
                break;
            default:
                printf("None\n");
                break;
        }
    }

    return (0);
}