#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <omp.h>

#define ARRAY_SIZE	10000000
#define N 5

typedef struct padded_double {
  double value;
  char padding[128-sizeof(double)];
} padded_double;

void generate_random(double *input, size_t size)
{
  for (size_t i = 0; i < size; i++) {
    input[i] = rand() / (double)(RAND_MAX);
  }
}

double opt_local_sum(double *x, size_t size)
{
  // This way we dont need to worry about changing MAX_THREADS 
  // when we run tests with different number of threads
  int nt = omp_get_max_threads();
  padded_double local_sum[nt];


  #pragma omp parallel shared(local_sum)
  {
    int id = omp_get_thread_num();
    #pragma omp for
    for (size_t i = 0; i < size; i++) {
      /* Print hello from thread */
      //  int id = omp_get_thread_num();
      //  printf("Hello World from Thread %d!\n", id);
      local_sum[id].value += x[i];
    }
  }

  double sum_val = 0.0;

  for (int i = 0; i < nt; i++) {
    sum_val += local_sum[i].value;
  } 

  return sum_val;
}

double ARRAY[ARRAY_SIZE];

int main() {
  // Init 
  double avg, std;
  generate_random(ARRAY, ARRAY_SIZE);
  
  // Run 
  double times[N];
  for (size_t i = 0; i < N; i++) {
    double start_time = omp_get_wtime();
    opt_local_sum(ARRAY, ARRAY_SIZE);
    double time = omp_get_wtime() - start_time;
    times[i] = time;
  }

  // Compute average and std 
  double sum = 0.0;
  for (size_t i = 0; i < N; i++) {
    sum += times[i];
  }
  avg = sum/N;

  sum = 0.0;
  for (size_t i = 0; i < N; i++) {
    sum += pow(times[i] - avg, 2);
  }
  std = sqrt(sum/(N-1));

  printf("Avg %f Std %f\n", avg, std);
  return 0;
}
