import re

hosts = ["intra", "inter"]
qpses = [["r1", "r10", "r50", "r100", "r200", "r500(470)", "r800(470)"],
  ["r1", "r10", "r50", "r100", "r200", "r500(470)", "r800(470)"]]

workers = 8

def get_data(file_path, start=True):
    results = {}
    with open(file_path, "r") as f:
        lines = f.readlines()

        for line in lines:
            if "req_id" in line:
                reqs = re.findall("req_id = (.*?),", line)
                if start:
                    times = re.findall("start_time = (.*?)\n", line)
                else:
                    times = re.findall("end_time = (.*?)\n", line)

                results[reqs[0]] = int(times[0])

    return results

def check(result, d):
    flag = False
    for k in result:
        if k in d:
            flag = True
            print("already has %s" % k)

def get_per(values, pt):
    sort_values = sorted(values)
    # print(len(values), pt, int(pt /100.0 * len(values)) - 1)
    return sort_values[int(pt /100.0 * len(values)) - 1]

for host, qpss in zip(hosts, qpses):
    for qps in qpss:
        start_dict = {}
        end_dict = {}

        for worker_index in range(workers):
            start_file_path = "Pheromone-best/%s/%s/exp09Start_worker_%d.stdout" % (host, qps, worker_index)
            end_file_path = "Pheromone-best/%s/%s/exp09End_worker_%d.stdout" % (host, qps, worker_index)

            start_results = get_data(start_file_path)
            end_results = get_data(end_file_path, start=False)

            # check(start_results, start_dict)
            # check(end_results, end_dict)

            start_dict.update(start_results)
            end_dict.update(end_results)

        lats = []

        sort_start_times = sorted(list(start_dict.values()))
        start_timestamp = sort_start_times[0] + 30000000

        for k in start_dict.keys():
            # if (not start_dict[k] < start_timestamp) and k in end_dict:
            if k in end_dict:
                # print(k, end_dict[k] - start_dict[k])
                lats.append(end_dict[k] - start_dict[k])

                # if lats[-1] < 0:
                    # print(k, end_dict[k], start_dict[k])

        # print(lats)
        try:
            median_lat = get_per(lats, 50)
            tail_lat = get_per(lats, 99)
            min_lat = min(lats)
            # print("%s-%s: %d, %d" % (host, qps, median_lat, tail_lat))
            print("%s-%s: %d, %d, %d" % (host, qps, min_lat, median_lat, tail_lat))
            # print(sorted(lats))
        except Exception as e:
            print(e)
            print("%s-%s: wrong" % (host, qps))
        
        # exit(0)

