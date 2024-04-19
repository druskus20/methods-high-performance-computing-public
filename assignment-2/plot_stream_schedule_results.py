import matplotlib.pyplot as plt
import json
import numpy as np

data = {}
data['1'] = json.loads(open('results_stream_1.json').read())
data['32'] = json.loads(open('results_stream_32.json').read())
data['64'] = json.loads(open('results_stream_64.json').read())
data['128'] = json.loads(open('results_stream_128.json').read())

bandwidths_avg = [
        data['1']['averages']['Copy']['Best Rate MB/s'],
        data['32']['averages']['Copy']['Best Rate MB/s'],
        data['64']['averages']['Copy']['Best Rate MB/s'],
        data['128']['averages']['Copy']['Best Rate MB/s']
]
bandwidths_std = [
        data['1']['std_devs']['Copy']['Best Rate MB/s'],
        data['32']['std_devs']['Copy']['Best Rate MB/s'],
        data['64']['std_devs']['Copy']['Best Rate MB/s'],
        data['128']['std_devs']['Copy']['Best Rate MB/s']
]

print(bandwidths_avg)
print(bandwidths_std)

