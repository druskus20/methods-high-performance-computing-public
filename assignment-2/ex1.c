/** 

Exercise 1 - OpenMP Hello World, get familiar with OpenMP Environment
Here we’re going to implement the first OpenMP program. Expected knowledge includes a basic understanding of the OpenMP environment, how to compile an OpenMP program, how to set the number of OpenMP threads, and retrieve the thread ID number at runtime.

Instructions. Write a C code to make each OpenMP thread print Hello World from Thread X! with X = thread ID. Learn how to launch the OpenMP code on Dardel. Your code using four threads should behave similarly to:

Hello World from Thread 3!
Hello World from Thread 0!
Hello World from Thread 2!
Hello World from Thread 1!
Questions:

Write an OpenMP C code with each thread printing Hello World from Thread X! where X is the thread ID.
How do you compile the code in question 1? Which compiler and flags have you used?
How do you run the OpenMP code on Dardel? What flags did you set?
How many different ways can the number of threads in OpenMP be changed? Which are they?


*/


#include "stdio.h"  
#include "stdlib.h" 
#include "omp.h"    


int main (int argc, char *argv[]) {
    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        printf("Hello World from Thread %d!\n", id);
    }
    return 0;
}

// To compile: 
// gcc -fopenmp ex1.c -o ex1
