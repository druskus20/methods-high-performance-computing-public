import matplotlib.pyplot as plt
import re
import numpy as np


# data looks like this
# DFTW calculation with N = 10000 
# DFTW computation in 19.115951 seconds
# Xre[0] = 10000.000000 
# DFTW calculation with N = 10000 
# DFTW computation in 0.687536 seconds
# Xre[0] = 10000.000000 
# DFTW calculation with N = 10000 
# DFTW computation in 0.360909 seconds
# Xre[0] = 10000.000000 
# DFTW calculation with N = 10000 
# DFTW computation in 0.267273 seconds
# Xre[0] = 10000.000000 

def parse_file(file): 
    pattern = r'DFTW computation in (\d+\.\d+) seconds'
    with open(file, 'r') as f:
        data = f.read()
    matches = re.findall(pattern, data)

    for i in range(len(matches)):
        matches[i] = float(matches[i])

    return matches


threads = [1, 32, 64, 128]

# plot

times = parse_file('./dftw_results')
times_opt = parse_file('./dftw_opt_results')

plt.figure(figsize=(10,5))
plt.xlabel('Threads')
plt.ylabel('Time')
plt.title('DFTW: time vs threads')
plt.xticks(threads)
plt.plot(threads, times_opt, label='Optimized', color='green')
plt.plot(threads, times, label='Regular', color='red')
plt.legend()
plt.savefig('dftw_results.png')

