
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[]){

    int rank, size, i, provided;
    
    int nxc = 128; 
    double L = 2*3.1415; 
    

    MPI_Init_thread(&argc, &argv, MPI_THREAD_SINGLE, &provided);

    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    int nxn_loc = nxc/size + 3; 
    double L_loc = L/((double) size);
    double dx = L / ((double) nxc);
    
    double *f = calloc(nxn_loc, sizeof(double)); 
    double *dfdx = calloc(nxn_loc, sizeof(double)); 

    for (i=1; i<(nxn_loc-1); i++)
      f[i] = sin(L_loc*rank + (i-1) * dx);
    
    // need to communicate and fill ghost cells f[0] and f[nxn_loc-1]
    if (rank % 2 == 0) {
      int left = rank - 1;
      int right = (rank + 1) % size;
      MPI_Send(&f[1], 1, MPI_DOUBLE, left, 0, MPI_COMM_WORLD);
      MPI_Recv(&f[0], 1, MPI_DOUBLE, left, 0, MPI_COMM_WORLD);
      MPI_Send(&f[nxn_loc - 2], 1, MPI_DOUBLE, right, MPI_ANY_TAG, MPI_COMM_WORLD);
      MPI_Recv(&f[nxn_loc - 1], 1, MPI_DOUBLE, right, MPI_ANY_TAG, MPI_COMM_WORLD);
    }
    else {
      int left = (rank - 1 + size) % size;
      int right = (rank + 1) % size;
      MPI_Recv(&f[nxn_loc - 1], 1, MPI_DOUBLE, right, MPI_ANY_TAG, MPI_COMM_WORLD);
      MPI_Send(&f[nxn_loc - 2], 1, MPI_DOUBLE, right_node, MPI_ANY_TAG, MPI_COMM_WORLD);
      MPI_Send(&f[1], 1, MPI_DOUBLE, left_node, MPI_ANY_TAG, MPI_COMM_WORLD);
      MPI_Recv(&f[0], 1, MPI_DOUBLE, left_node, MPI_ANY_TAG, MPI_COMM_WORLD);
    }


    for (i=1; i<(nxn_loc-1); i++)
      dfdx[i] = (f[i+1] - f[i-1])/(2*dx);


    if (rank==0){ 
      printf("My rank %d of %d\n", rank, size );
      printf("Here are my values for f including ghost cells\n");
      for (i=0; i<nxn_loc; i++)
        printf("%f\n", f[i]);
      printf("\n");
    }   

    MPI_Finalize();
}






