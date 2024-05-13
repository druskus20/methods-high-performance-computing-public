#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <mpi.h>

#define SEED     921
#define NUM_ITER 1000000000


int calc_pi(int n_iter);

int main(int argc, char* argv[])
{
    int count = 0;
    double x, y, z, pi;

    int R = 0;
    int size = 1, rank = 0;
    int provided; // output argument
    
    /* MPI Stuff */
    MPI_Init_thread(&argc, &argv, MPI_THREAD_SINGLE, &provided);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);


    // TIME -------------------------------------
    double start_time = MPI_Wtime();

    srand(SEED * rank); 

    int n_iter = NUM_ITER / size;
    count = calc_pi(n_iter); // only n_iter
    MPI_Reduce(&count, &R, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
  
    if (rank == 0) {
      pi = ((double)R / (double)NUM_ITER) * 4.0;
    }

    double end_time = MPI_Wtime();
    double t = end_time - start_time;
    // TIME -------------------------------------

    if (rank == 0) {
      printf("The result is %f\n", pi);
      printf("The time is: %fs\n", t);
    }

    MPI_Finalize();
    return 0;
}

int calc_pi(int n_iter) 
{
    int count = 0;
    double x, y, z, pi;
    for (int iter = 0; iter < n_iter; iter++)
    {
        x = (double)random() / (double)RAND_MAX;
        y = (double)random() / (double)RAND_MAX;
        z = (x * x) + (y * y);

        if (z <= 1.0)
        {
            count++;
        }
    }
    return count;
}

