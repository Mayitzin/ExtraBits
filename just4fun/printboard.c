/* Checker Board Printer
 *
 * Usage:
 * >> printboard [width] [height]
 * 
 * History:
 *     17.10.2015. First implementation.
 *
 * @author: Mario Garcia
 * www.mayitzin.com
**/

#include <stdio.h>
// #include <string.h>

// Default Dimensions of each Cell
#define cellWidth  5
#define cellHeight 2

void printEdge(int cellw, int width);
void printClear(int cellw, int width);

int main(int argc, char *argv[]) {
	int height = 3, width = 4;		// Default Dimensions of Board
	int cellw  = cellWidth;
	if (argc>1){
		height = atoi(argv[1]);
		width  = atoi(argv[2]);
	}
	int i, ir;

	printf("%d by %d:\n", height, width);

	// Print the Board row by row
	printEdge(cellw, width);
	for (ir=0; ir<height; ++ir) {
		for (i=0; i<cellHeight; ++i) {
			printClear(cellw, width);
		}
		printEdge(cellw, width);
	}

	return (0);
}


void printEdge(int cellw, int width) {
	int i, ic=0;
	// Print Horizontal Edge
	printf("+");
	for(ic=0; ic<width; ++ic) {
		for(i=0; i<cellWidth; ++i) {
			printf("-");
		}
		printf("+");
	}
	printf("\n");
}


void printClear(int cellw, int width) {
	int i, ic=0;
	// Print Horizontal Area
	printf("|");
	for(ic=0; ic<width; ++ic) {
		for(i=0; i<cellWidth; ++i) {
			printf(" ");
		}
		printf("|");
	}
	printf("\n");
}