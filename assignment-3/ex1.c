#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    int i, p, r, s;
    MPI_Init_thread(&argc, &argv, MPI_THREAD_SINGLE, &p);
    MPI_Comm_size(MPI_COMM_WORLD, &s);
    MPI_Comm_rank(MPI_COMM_WORLD, &r);
    printf("Hello World from rank %d from %d processes!\n", r, s);
}
