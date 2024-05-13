rm -rf ex4_results.txt
touch ex4_results.txt

for t in 8 16 32 64 128; do
  srun -n $t ./ex4 >> ex4_results.txt
done

