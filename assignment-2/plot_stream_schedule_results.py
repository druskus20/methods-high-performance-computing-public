import matplotlib.pyplot as plt
import json 
import numpy as np

data = {}
data['static'] = json.loads(open('results_stream_dynamic.json').read())
data['dynamic'] = json.loads(open('results_stream_static.json').read())
data['guided'] = json.loads(open('results_stream_guided.json').read())

bandwidths_avg = [
        data['static']['averages']['Copy']['Best Rate MB/s'],
        data['dynamic']['averages']['Copy']['Best Rate MB/s'],
        data['guided']['averages']['Copy']['Best Rate MB/s'],
]
bandwidths_std = [
        data['static']['std_devs']['Copy']['Best Rate MB/s'],
        data['dynamic']['std_devs']['Copy']['Best Rate MB/s'],
        data['guided']['std_devs']['Copy']['Best Rate MB/s'],
]

print(bandwidths_avg)
print(bandwidths_std)


labels = ['Static', 'Dynamic', 'Guided']

plt.figure(figsize=(2.5,2.5))
plt.bar(labels, bandwidths_std, color='skyblue', edgecolor='black')

plt.xlabel('Labels')
plt.ylabel('Bandwidth (MB/s)')
plt.title('Histogram of average bandwidths (std)')

plt.show()

labels = ['Static', 'Dynamic', 'Guided']

# different color 
plt.figure(figsize=(2.5,2.5))
plt.bar(labels, bandwidths_avg, color='lightcoral', edgecolor='black')

plt.xlabel('Labels')
plt.ylabel('Bandwidth (MB/s)')
plt.title('Histogram of average bandwidths (avg)')

plt.show()

