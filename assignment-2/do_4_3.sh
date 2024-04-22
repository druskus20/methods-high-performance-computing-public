rm dftw_results
touch dftw_results
rm dftw_opt_results
touch dftw_opt_results

cc -g -fopenmp DFTW_1.c  -o DFTW -lm
cc -g -fopenmp DFTW_OPT.c  -o DFTW_OPT -lm

for t in 1 32 64 128; do
  export OMP_NUM_THREADS=$t
	srun -n 1 ./DFTW >> dftw_results
	srun -n 1 ./DFTW_OPT >> dftw_opt_results
done
