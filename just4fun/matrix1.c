/*
 * Matrix addressing
 */

#include <stdio.h>
#define size 3

int dim_x, dim_y;

int * transpose(int *matrix);
int * initZeros(int y, int x);
void printMatrix(int *matrix);
void printMatrixElems(int *matrix);

int main(int argc, char *argv[]){
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
    // Get pointer of Matrix
    int *m_ptr;
    m_ptr = &matrix[0][0];

    int i, j;
    // Set values for each element
    for(i=0; i<(dim_x*dim_y); ++i){
        *(m_ptr+i) = i+1;
    }
    // // Print the elements
    printMatrixElems(m_ptr);
    printMatrix(m_ptr);
    m_ptr = &matrix[0][0];
    // New matrix
    printf("Creating new matrix\n");
    int *tm;
    tm = transpose(m_ptr);
    printf("The new matrix is in 0x%p\n", tm);
    printMatrixElems(tm);
    printMatrix(tm);

    return (0);
}

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
    newm_ptr = &new_matrix[0][0];
    return (newm_ptr);
}

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