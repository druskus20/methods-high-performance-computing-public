#!/bin/env python

import matplotlib.pyplot as plt
import numpy as np

times = [2.365310, 1.214215, 0.925051, 0.349872, 0.273813]
cores = [8, 16, 32, 64, 128]

plt.figure(figsize=(5,5))
plt.xlabel('Cores')
plt.ylabel('Time')
plt.title('Aproximation of PI - MPI reduce')
plt.xticks(cores)
plt.plot(cores, times, label='Times', color='lightcoral')
plt.savefig('ex4.png')
