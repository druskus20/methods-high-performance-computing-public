rm sum_2
rm sum_3
touch sum_2
touch sum_3
cc -g -fopenmp parallel_sum.c -o run_2 -lm
cc -g -fopenmp parallel_critical_sum.c -o run_3 -lm

for t in 1 2 4 8 16 20 24 28 32; do
  export OMP_NUM_THREADS=$t
  srun -n 1 ./run_2 >> sum_2
  srun -n 1 ./run_3 >> sum_3
done
