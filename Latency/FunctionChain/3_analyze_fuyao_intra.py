import os
import re

platforms = ["Fuyao"]

# req_id = 60003, token = 1780 us

def get_per(values, pt):
    sort_values = sorted(values)
    # print(len(values), pt, int(pt /100.0 * len(values)) - 1)
    return sort_values[int(pt / 100.0 * len(values)) - 1]


filepath = 'Fuyao/intra'

results = {}


with open(filepath, 'r') as f:
    lines = f.readlines()
    for line in lines:
        titles = re.findall(r"chain_len: (\d+), payload: (\d+\w+)", line)
        if titles:
            for match in titles:
                chain_len, payload = match
            continue
        time = re.findall(r"takes (\d+)", line)
        if time:
            if payload not in results.keys():
                results[payload] = {}
            if chain_len not in results[payload].keys():
                results[payload][chain_len] = []
            results[payload][chain_len].append(int(time[0]))

try:
    for payload_size in results.keys():
        for chain_length in results[payload_size].keys():
            times = results[payload_size][chain_length]
            median_lat = get_per(times, 50)
            tail_lat = get_per(times, 99)
            min_lat = min(times)
            print("%s-%s-%s: %d, %d, %d" % ('Fuyao', payload_size, chain_length, min_lat, median_lat, tail_lat))

except Exception as e:
    print(e)




