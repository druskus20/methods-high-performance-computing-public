#!/bin/env python

import numpy as np

# Intra-node
time = np.array([
    0.000000776,
    0.000000295,
    0.000000256,
    0.000000258,
    0.000000276,
    0.000000324,
    0.000000418,
    0.000000608,
    0.000000975,
    0.000001445,
    0.000000706,
    0.000001136,
    0.000001841,
    0.000003401,
    0.000006065,
    0.000011678,
    0.000019350,
    0.000033195,
    0.000059439,
    0.000099789,
    0.000384907,
    0.001755560,
    0.002773836,
    0.004558827,
    0.008521297,
    0.016182613,
    0.031819208,
    0.062039224
    ])

# Inter-node
time2 = [
        0.000001956,
        0.000001904,
        0.000001953,
        0.000002039,
        0.000002575,
        0.000002582,
        0.000002860,
        0.000002631,
        0.000002961,
        0.000003339,
        0.000003354,
        0.000003710,
        0.000016730,
        0.000011509,
        0.000010254,
        0.000015877,
        0.000029752,
        0.000048578,
        0.000093843,
        0.000179558,
        0.000354083,
        0.000704135,
        0.001424981,
        0.002908634,
        0.005771466,
        0.012504362,
        0.026736009,
        0.054596928
        ]

size = np.array([
    8,        
    16,        
    32,        
    64,        
    128,        
    256,        
    512,        
    1024,        
    2048,        
    4096,        
    8192,        
    16384,        
    32768,        
    65536,        
    131072,        
    262144,        
    524288,        
    1048576,        
    2097152,        
    4194304,        
    8388608,        
    16777216,        
    33554432,        
    67108864,        
    134217728,        
    268435456,        
    536870912,        
    1073741824        
    ])

import matplotlib.pyplot as plt
import numpy as np


plt.figure(figsize=(5,5))
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Time vs Size - 2 processes intra node')

# logarithmic scale
plt.xscale('log')

plt.plot(size, time2, label='Times', color='lightcoral')
plt.savefig('ex2_intra.png')

plt.clf()

plt.figure(figsize=(5,5))
plt.xlabel('Input Size')
plt.ylabel('Time')
plt.title('Time vs Size - 2 processes inter node')

# logarithmic scale
plt.xscale('log')


plt.plot(size, time, label='Times', color='lightcoral')
plt.savefig('ex2_inter.png')
