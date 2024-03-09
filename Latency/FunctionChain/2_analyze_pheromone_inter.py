import os
import re

platforms = ["Pheromone"]

# req_id = 60003, token = 1780 us

def get_per(values, pt):
    sort_values = sorted(values)
    # print(len(values), pt, int(pt /100.0 * len(values)) - 1)
    return sort_values[int(pt / 100.0 * len(values)) - 1]


filepath = 'Pheromone/inter'
executor_files = ['executor_{}.log'.format(i) for i in range(1)]

results = {}

for executor_file in executor_files:
    with open(os.path.join(filepath, executor_file), 'r') as f:
        lines = f.readlines()
        for line in lines:
            result = re.findall(r"chain_length = (\d+), payload_size = (\d+), token (\d+)", line)
            if result:
                for match in result:
                    chain_length, payload_size, token = match

                    if payload_size not in results.keys():
                        results[payload_size] = {}
                    if chain_length not in results[payload_size].keys():
                        results[payload_size][chain_length] = []

                    results[payload_size][chain_length].append(int(token))

try:
    for payload_size in results.keys():
        for chain_length in results[payload_size].keys():
            times = results[payload_size][chain_length]
            median_lat = get_per(times, 50)
            tail_lat = get_per(times, 99)
            min_lat = min(times)
            print("%s-%s-%s: %d, %d, %d" % ('Pheromone', payload_size, chain_length, min_lat, median_lat, tail_lat))

except Exception as e:
    print(e)




