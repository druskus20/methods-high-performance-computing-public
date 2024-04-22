for t in 1 32 64 128; do
  rm stream_$t
  touch stream_$t
  srun -n 1 stream >> stream_$t
  srun -n 1 stream >> stream_$t
  srun -n 1 stream >> stream_$t
  srun -n 1 stream >> stream_$t
  srun -n 1 stream >> stream_$t
done

