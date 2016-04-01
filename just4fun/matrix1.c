/*
 * Matrix addressing
 *
 * History:
 *     04.11.2015. First implementation.
 *     30.03.2015. Added descriptions and functions.
 *
 * @author: Mario Garcia.
 * www.mayitzin.com
 */

#include <stdio.h>
#include <stdlib.h>
#define defSize 3

int columns = defSize, rows = defSize;

int * transpose(int *matrix_ptr, int *matrix2_ptr, int y, int x);
int * initMatrix(int *matrix, int y, int x);
int * copyMatrix(int *matrix_ptr, int *matrix2_ptr, int y, int x);
int * initZeros(int y, int x);
void printMatrix(int *matrix, int y, int x);
void printMatrixElems(int *matrix);

int main(int argc, char *argv[]){
    // Read default values
    if(argc>1){
        rows = atoi(argv[1]);
        columns = atoi(argv[2]);
    }

    // Initialize Matrix
    int matrix[rows][columns];
    printf("The dimensions are %d by %d\n", rows, columns);
    // Set pointer of Matrix
    int *m_ptr;
    m_ptr = matrix[0];
    // Set values for each element
    m_ptr = initMatrix(m_ptr, rows, columns);
    // Print the elements
    printMatrixElems(m_ptr);
    printMatrix(m_ptr, rows, columns);
    m_ptr = matrix[0];

    // Copy the matrix and show it
    int matrix2[rows][columns];
    int *m2_ptr;
    m2_ptr = matrix2[0];
    m2_ptr = copyMatrix(m_ptr, m2_ptr, rows, columns);
    printf("\nSecond matrix:\n");
    printMatrix(m2_ptr, rows, columns);

    // New matrix
    int matrix3[columns][rows];
    int *m3_ptr;
    m3_ptr = matrix3[0];
    m3_ptr = transpose(m_ptr, m3_ptr, columns, rows);
    printf("\nThird matrix:\n");
    printMatrixElems(m3_ptr);
    printMatrix(m3_ptr, columns, rows);

    return (0);
}


/**
* @brief Initialize a Matrix with a sequence of increasing integers.
* 
* This function builds a matrix with the given dimensions, whose elements are a
* set of integers increasing from the first upper-left element until reaching
* the last element of the matrix at the lower-right.
*
* @param  [in] matrix_ptr is the pointer to the matrix to initialize.
* @param  [in] y is the number of columns for the new matrix.
* @param  [in] x is the number of rows for the new matrix.
*/
int * initMatrix(int *matrix_ptr, int y, int x){
    int i;
    // Set values for each element
    for(i=0; i<(x*y); ++i){
        *(matrix_ptr+i) = i+1;
    }
    return (matrix_ptr);
}


/**
* @brief Copy a Matrix to a new one.
* 
* This function copies a matrix, whose elements are the same values as in the
* given input matrix.
*
* @param  [in] matrix_ptr is the pointer of the matrix copying from.
* @param  [in] matrix2_ptr is the pointer of the matrix copying to.
* @param  [in] y is the number of columns for the new matrix.
* @param  [in] x is the number of rows for the new matrix.
*/
int * copyMatrix(int *matrix_ptr, int *matrix2_ptr, int y, int x){
    int i;
    // Set values for each element
    for(i=0; i<(x*y); ++i){
        *(matrix2_ptr+i) = *(matrix_ptr+i);
    }
    return (matrix2_ptr);
}


/**
* @brief Transpose the matrix.
* 
* This function re-adresses the elements of the matrix to transpose a matrix.
*
* @param  [in] matrix is the pointer to the matrix to show.
*/
int * transpose(int *matrix_ptr, int *matrix2_ptr, int rows, int columns){
    int i, j;
    int *init_ptr;
    init_ptr = matrix2_ptr;
    // Set values for each element
    for(i=0; i<rows; ++i){
        for(j=0; j<columns; ++j){
            *(matrix2_ptr) = *(matrix_ptr);
            ++matrix_ptr;
            ++matrix2_ptr;
        }
    }
    return (init_ptr);
}


/**
* @brief Print matrix elements.
* 
* This function simply prints the elements of the matrix in an array-shaped
* output.
*
* @param  [in] matrix is the pointer to the matrix to show.
*/
void printMatrix(int *matrix, int rows, int columns){
    int i, j;
    for(i=0; i<rows; ++i){
        for(j=0; j<columns; ++j){
            printf("\t%d", *matrix);
            ++matrix;
        }
        printf("\n");
    }
}


/**
* @brief Print matrix elements with their memory addresses.
* 
* This function prints out the elements of the given matrix preceded by their
* address in the memory and their position in the matrix in a C/Python style.
*
* @param  [in] matrix is the pointer to the matrix to show.
*/
void printMatrixElems(int *matrix){
    int i, j;
    // Print the elements
    for(i=0; i<rows; ++i){
        for(j=0; j<columns; ++j){
            printf("0x%p : M[%d][%d] = %d\n", matrix, i, j, *matrix);
            ++matrix;
        }
    }
}


/**
* @brief Initialize a Matrix with zeros.
* 
* This function builds a matrix with the given dimensions, whose elements are a
* set of integers equal to zero.
*
* @param  [in] y is the number of columns for the new matrix.
* @param  [in] x is the number of rows for the new matrix.
* @param  [out] m_ptr is the pointer to the created matrix.
*/
int * initZeros(int y, int x){
    int matrix[x][y];
    int *m_ptr;
    m_ptr = &matrix[0][0];
    int i;
    // Set values for each element
    for(i=0; i<(x*y); ++i){
        *(m_ptr+i) = 0;
    }
    return (m_ptr);
}