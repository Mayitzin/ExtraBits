/* ===============
 * Build HTML File
 * ===============
 *
 * History:
 *     21.07.2015. First implementation.
 *
 * @author: Mario Garcia
 * www.mayitzin.com
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]){
	FILE *file;
	const char *fileName = "Output.html";

	printf("Hi!\n");

	file = fopen(fileName, "w");
	if(file == NULL){
		perror("Error opening file");
		exit(1);
	}

	fprintf(file, "<html><body>Hi!</body></html>");

	fclose(file);

	printf("End parsing\n");

	return 0;
}