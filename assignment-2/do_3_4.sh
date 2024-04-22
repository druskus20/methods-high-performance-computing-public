rm sum_4
touch sum_4
rm sum_5
touch sum_5
cc -g -fopenmp parallel_local_sum.c -o run_4 -lm
cc -g -fopenmp opt_parallel_local_sum.c -o run_5 -lm

for t in 1 32 64 128; do
  export OMP_NUM_THREADS=$t
  srun -n 1 ./run_4 >> sum_4
  srun -n 1 ./run_5 >> sum_5
done
