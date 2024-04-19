import re
import sys
import json
import numpy as np

# first arg is the stream file
if len(sys.argv) < 2:
    print("Usage: python parse.py <stream_file>")
    sys.exit(1)

stream_file = sys.argv[1]


# Define a regular expression pattern to match the required data
pattern = r'(\w+):\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)'

# Open the file
with open(stream_file, 'r') as file:
    data = file.read()

# Find all matches of the pattern in the file
matches = re.findall(pattern, data)

# Store the values in a dictionary
function_data = {}
for match in matches:
    function_name = match[0]
    values = list(map(float, match[1:]))
    if function_name not in function_data:
        function_data[function_name] = []
    function_data[function_name].append(values)

# Calculate average and standard deviation for each function
averages = {}
std_devs = {}
for function_name, values_list in function_data.items():
    values_array = np.array(values_list)
    averages[function_name] = np.mean(values_array, axis=0)
    std_devs[function_name] = np.std(values_array, axis=0)


# Print the results
#for function_name, avg_values in averages.items():
#    print("Function:", function_name)
#    print("Average Best Rate MB/s:", avg_values[0])
#    print("Average Avg time:", avg_values[1])
#    print("Average Min time:", avg_values[2])
#    print("Average Max time:", avg_values[3])
#    print("Standard Deviation Best Rate MB/s:", std_devs[function_name][0])
#    print("Standard Deviation Avg time:", std_devs[function_name][1])
#    print("Standard Deviation Min time:", std_devs[function_name][2])
#    print("Standard Deviation Max time:", std_devs[function_name][3])
#    print("-" * 60)

# store results in a dictionary
results = {}
results['averages'] = {}
results['std_devs'] = {}
for function_name, avg_values in averages.items():
    results['averages'][function_name] = {}
    results['std_devs'][function_name] = {}
    results['averages'][function_name]['Best Rate MB/s'] = avg_values[0]
    results['averages'][function_name]['Avg time'] = avg_values[1]
    results['averages'][function_name]['Min time'] = avg_values[2]
    results['averages'][function_name]['Max time'] = avg_values[3]
    results['std_devs'][function_name]['Best Rate MB/s'] = std_devs[function_name][0]
    results['std_devs'][function_name]['Avg time'] = std_devs[function_name][1]
    results['std_devs'][function_name]['Min time'] = std_devs[function_name][2]
    results['std_devs'][function_name]['Max time'] = std_devs[function_name][3]

json.dump(results, open(f"results_{stream_file}.json", 'w'), indent=4)


