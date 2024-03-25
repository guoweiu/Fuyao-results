import re
import os

base_dir = "new_logs/"

list_files = os.listdir(base_dir)

# list_files = ['logs/exp02UploadRating3_worker_5.stdout']

reqs = {}

# regular expression
reg_exp = r'^(?P<severity>[IWEF])(?P<date>[^ ]*) (?P<timestamp>[^ ]*) (?P<info>[^]]*)] req_id = (?P<req_id>[^,]*), (?P<time_flag>[^ ]*) (?P<time_stamp>[^\n]*)'
for file in list_files:
    file = base_dir + os.sep + file
    with open(file, 'r') as f:
        for line in f:
            reg_match = re.match(reg_exp, line)
            if reg_match:
                line_dict = reg_match.groupdict()
                req_id = line_dict['req_id']
                time_flag = line_dict['time_flag']
                time_stamp = line_dict['time_stamp']

                if req_id not in reqs:
                    reqs[req_id] = {}

                if time_flag not in reqs[req_id]:
                    reqs[req_id][time_flag] = []

                reqs[req_id][time_flag].append(time_stamp)

ratios = []

for req in reqs.values():
    t0 = int(req['t0'][0])
    t1 = int(min(req['t1']))
    t2 = int(req['t2'][0])
    t3 = int(req['t3'][0])
    t4 = int(req['t4'][0])
    t5 = int(req['t5'][0])

    total_time = t5 - t0
    execution_time = (t4 - t3) + (t2 - t1)

    print("total_time: ", t5 - t0, ", execution_time: ", (t4 - t3) + (t2 - t1))
    ratios.append(execution_time * 1.0 / total_time)

# 10

intra_node = [6.955, 6.301, 6.598, 5.537, 5.819, 4.514, 8.620, 6.756, 8.465]
inter_node = [5.980, 5.792, 6.172, 5.914, 5.370,  7.053, 5.953, 5.549, 7.373]