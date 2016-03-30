/*
 * Matrix addressing
 *
 * History:
 *     04.11.2015. First implementation.
 *
 * @author: Mario Garcia.
 * www.mayitzin.com
 */

#include <stdio.h>
#include <stdlib.h>
#define size 3

int dim_x, dim_y;

int * transpose(int *matrix);
int * initMatrix(int *matrix, int y, int x);
int * copyMatrix(int *matrix_ptr, int *matrix2_ptr, int y, int x);
int * initZeros(int y, int x);
void printMatrix(int *matrix);
void printMatrixElems(int *matrix);

int main(int argc, char *argv[]){
    // Read default values
    if(argc>1){
        dim_y = atoi(argv[1]);
        dim_x = atoi(argv[2]);
    } else {
        dim_y = size;
        dim_x = size;
    }

    // Initialize Matrix
    int matrix[dim_y][dim_x];
    printf("The dimensions are %d by %d\n", dim_y, dim_x);
    // Set pointer of Matrix
    int *m_ptr;
    m_ptr = matrix[0];
    // Set values for each element
    m_ptr = initMatrix(m_ptr, dim_y, dim_x);
    // Print the elements
    printMatrixElems(m_ptr);
    printMatrix(m_ptr);
    m_ptr = matrix[0];
    // Copy the matrix and show it
    int matrix2[dim_y][dim_x];
    int *m2_ptr;
    m2_ptr = matrix2[0];
    m2_ptr = copyMatrix(m_ptr, m2_ptr, dim_y, dim_x);
    printMatrix(m2_ptr);

    // New matrix
    printf("Creating new matrix\n");
    int *tm;
    tm = transpose(m_ptr);
    printf("The new matrix is in 0x%p\n", tm);
    printMatrixElems(tm);
    printMatrix(tm);

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
* @param  [in] matrix_ptr is the pointer to the matrix to initialize.
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
int * transpose(int *matrix){
    int new_matrix[dim_x][dim_y];
    int *newm_ptr;
    // Set values for each element
    int i, j;
    for(i=0; i<dim_y; ++i){
        for(j=0; j<dim_x; ++j){
            new_matrix[j][i] = *(matrix+i+j);
            // ++matrix;
        }
    }
    newm_ptr = new_matrix[0];
    return (newm_ptr);
}


/**
* @brief Print matrix elements.
* 
* This function simply prints the elements of the matrix in an array-shaped
* output.
*
* @param  [in] matrix is the pointer to the matrix to show.
*/
void printMatrix(int *matrix){
    int i, j;
    for(i=0; i<dim_y; ++i){
        for(j=0; j<dim_x; ++j){
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
    for(i=0; i<dim_y; ++i){
        for(j=0; j<dim_x; ++j){
            printf("0x%p : M[%d][%d] = %d\n", matrix, i, j, *matrix);
            ++matrix;
        }
    }
}

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