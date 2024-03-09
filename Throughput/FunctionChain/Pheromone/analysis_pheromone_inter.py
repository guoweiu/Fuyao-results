import os


current_directory = os.path.dirname(os.path.abspath(__file__))

dirs_path = [
    current_directory + '/inter/2(130ins, 3000qps, 10s)',
    current_directory + '/inter/16(130ins, 3000qps, 10s)',
    current_directory + '/inter/32(130ins, 3000qps, 10s)',
    current_directory + '/inter/64(130ins, 3000qps, 10s)',
    current_directory + '/inter/128(130ins, 3000qps, 10s)',
]


for dir_path in dirs_path:
    sum = 0
    for sub_dir in ['126', '129']:
        walk_path = os.path.join(dir_path, sub_dir)
        for root, dirs, files in os.walk(walk_path):
            files_path = [os.path.join(root, file) for file in files]
            for file_path in files_path:
                with open(file_path, 'r') as f:
                    for line in f:
                        if 'chain_length' in line:
                            sum += 1
    print('qps:', sum/10)


