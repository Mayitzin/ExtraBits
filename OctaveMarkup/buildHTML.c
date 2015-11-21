/*******************************************************************************
 * Copyright (c) 2015 Mario Garcia                                             *
 *                                                                             *
 * Permission is hereby granted, free of charge, to any person obtaining a     *
 * copy of this software and associated documentation files (the "Software"),  *
 * to deal in the Software without restriction, including without limitation   *
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,    *
 * and/or sell copies of the Software, and to permit persons to whom the       *
 * Software is furnished to do so, subject to the following conditions:        *
 *                                                                             *
 * The above copyright notice and this permission notice shall be included in  *
 * all copies or substantial portions of the Software.                         *
 *                                                                             *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  *
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    *
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE *
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      *
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     *
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         *
 * DEALINGS IN THE SOFTWARE.                                                   *
 ******************************************************************************/

/**
 * @file buildHTML.c
 * @brief This code builds a simple HTML file.
 * @author Mario Garcia
 * @date 21 Nov 2015
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * getBody(char *text);
void printText(char *text);

int main(int argc, char *argv[]){
    FILE *file;
    char *fileName = "Output.html";

    printf("Hi!\n");

    file = fopen(fileName, "w");
    if(file == NULL){
        perror("Error opening file");
        exit(1);
    }
    fprintf(file, "<html><body>Hi!</body></html>");
    fclose(file);
    printf("End parsing\n");

    char newbodyChar[50];
    char * bodyChar = "The Body";
    char * newbodyChar_ptr;
    newbodyChar_ptr = getBody(bodyChar);
    printf("0x%p : ", newbodyChar_ptr);
    printText(newbodyChar_ptr);
    // free(newbodyChar_ptr);

    return 0;
}

char * getBody(char *text){
    size_t len = strlen(text);
    char bodyBlock[len+13];
    char * bodyBlock_ptr;
    // char * bodyBlock_ptr = (char *) malloc(len+1);  /* +1 for the null */
    // if(bodyBlock_ptr == NULL) return NULL;
    strcpy(bodyBlock, "");
    strcat(bodyBlock, "<body>");
    strcat(bodyBlock, text);
    strcat(bodyBlock, "</body>");
    printf("%s\n", bodyBlock);
    bodyBlock_ptr = &bodyBlock[0];
    printf("0x%p : ", bodyBlock_ptr);
    printText(bodyBlock_ptr);
    printf("Finishing inner Block\n");
    newbodyChar = bodyBlock;
    return newbodyChar;
}

void printText(char *text){
    size_t len = strlen(text);
    printf("%s\n", text);
    int i;
    for(i=0; i<len; ++i){
        printf("%c", *text);
        ++text;
    }
    printf("\n");
}