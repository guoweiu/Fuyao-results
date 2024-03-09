import os
import re

platforms = ["Pheromone"]
classifies = ["intra"]
filenames = ["f10", "f20", "f40", "f60", "f80"]

# req_id = 60003, token = 1780 us

def get_per(values, pt):
    sort_values = sorted(values)
    # print(len(values), pt, int(pt /100.0 * len(values)) - 1)
    return sort_values[int(pt / 100.0 * len(values)) - 1]

for platform in platforms:
    for classify in classifies:
        for filename in filenames:
            filepath = platform + os.sep + classify + os.sep + filename

            executor_files = ['executor_{}.log'.format(i) for i in range(80)]

            times = []
            for executor_file in executor_files:
                with open(os.path.join(filepath, executor_file), 'r') as f:
                    lines = f.readlines()

                    for line in lines:
                        time = re.findall(r"token (\d+)", line)

                        if time:
                            times.append(int(time[0]))
            try:
                median_lat = get_per(times, 50)
                tail_lat = get_per(times, 99)
                min_lat = min(times)
                print("%s-%s-%s: %d, %d, %d" % (platform, classify, filename, min_lat, median_lat, tail_lat))
            except Exception as e:
                print(e)




