import matplotlib.pyplot as plt
import re
import numpy as np

def parse_file(file):
    pattern = r'Avg (\d+\.\d+) Std (\d+\.\d+)'
    with open(file, 'r') as f:
        data = f.read()
    matches = re.findall(pattern, data)

    averages = []
    std_devs = []
    for match in matches:
        avg, std = map(float, match)
        averages.append(avg)
        std_devs.append(std)
    return averages, std_devs


threads = [1, 2, 4, 8, 16, 20, 24, 28, 32]

# plot

averages, std_devs = parse_file('sum_2')

plt.figure(figsize=(5,5))
plt.xlabel('Threads')
plt.ylabel('Time')
plt.title('parallel_sum: Time vs Threads (avg)')
plt.xticks(threads)
plt.plot(threads, averages, label='Average', color='lightcoral')
plt.savefig('avg_sum_2.png')

plt.figure(figsize=(5,5))
plt.xlabel('Threads')
plt.ylabel('Time')
plt.title('parallel_sum: Time vs Threads (std)')
plt.xticks(threads)
plt.plot(threads, std_devs, label='Standard Deviation', color='skyblue')
plt.savefig('std_sum_2.png')


averages, std_devs = parse_file('sum_3')

plt.figure(figsize=(5,5))
plt.xlabel('Threads')
plt.ylabel('Time')
plt.title('parallel_critical_sum: Time vs Threads (avg)') 
plt.xticks(threads)
plt.plot(threads, averages, label='Average', color='lightcoral')
plt.savefig('avg_sum_3.png')

plt.figure(figsize=(5,5))
plt.xlabel('Threads')
plt.ylabel('Time')
plt.title('parallel_critical_sum: Time vs Threads (std)') 
plt.xticks(threads)
plt.plot(threads, std_devs, label='Standard Deviation', color='skyblue')
plt.savefig('std_sum_3.png') 

pattern = r'Avg (\d+\.\d+) Std (\d+\.\d+)'
threads = [1, 32, 64, 128]

averages, std_devs = parse_file('sum_4')

plt.figure(figsize=(5,5))
plt.xlabel('Threads')
plt.ylabel('Time')
plt.title('parallel_local_sum: Time vs Threads (avg)')
plt.xticks(threads)
plt.plot(threads, averages, label='Average', color='lightcoral')
plt.savefig('avg_sum_4.png')

plt.figure(figsize=(5,5))
plt.xlabel('Threads')
plt.ylabel('Time')
plt.title('parallel_local_sum: Time vs Threads (std)')
plt.xticks(threads)
plt.plot(threads, std_devs, label='Standard Deviation', color='skyblue')
plt.savefig('std_sum_4.png')


averages, std_devs = parse_file('sum_5')

plt.figure(figsize=(5,5))
plt.xlabel('Threads')
plt.ylabel('Time')
plt.title('opt_parallel_local_sum: Time vs Threads (avg)')
plt.xticks(threads)
plt.plot(threads, averages, label='Average', color='lightcoral')
plt.savefig('avg_sum_5.png')

plt.figure(figsize=(5,5))
plt.xlabel('Threads')
plt.ylabel('Time')
plt.title('opt_parallel_local_sum: Time vs Threads (std)')
plt.xticks(threads)
plt.plot(threads, std_devs, label='Standard Deviation', color='skyblue')
plt.savefig('std_sum_5.png')
