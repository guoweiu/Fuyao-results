import os


current_directory = os.path.dirname(os.path.abspath(__file__))

dirs_path = [
    current_directory + '/inter/f10(600qps, 80ins, 10s)',
    current_directory + '/inter/f20(600qps, 80ins, 10s)',
    current_directory + '/inter/f40(100qps, 80ins, 60s)',
    current_directory + '/inter/f60(100qps, 80ins, 10s)',
    current_directory + '/inter/f80(100qps, 80ins, 10s)',
]

times = [10, 10, 60, 10, 10]

for dir_path in dirs_path:
    sum = 0
    i = 0
    for sub_dir in ['126', '129']:
        walk_path = os.path.join(dir_path, sub_dir)
        for root, dirs, files in os.walk(walk_path):
            files_path = [os.path.join(root, file) for file in files]
            for file_path in files_path:
                with open(file_path, 'r') as f:
                    for line in f:
                        if 'req_id' in line:
                            sum += 1
    print('qps:', sum/times[i])
    i = i + 1


