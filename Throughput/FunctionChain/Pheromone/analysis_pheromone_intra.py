import os


current_directory = os.path.dirname(os.path.abspath(__file__))

dirs_path = [
    current_directory + '/intra/2(130ins, 3000qps, 10s)',
    current_directory + '/intra/16(130ins, 3000qps, 10s)',
    current_directory + '/intra/32(130ins, 3000qps, 10s)',
    current_directory + '/intra/64(130ins, 3000qps, 10s)',
    current_directory + '/intra/128(130ins, 3000qps, 10s)',
]


for dir_path in dirs_path:
    for root, dirs, files in os.walk(dir_path):
        sum = 0
        files_path = [os.path.join(root, file) for file in files]
        for file_path in files_path:
            with open(file_path, 'r') as f:
                for line in f:
                    if 'chain_length' in line:
                        sum += 1

        print('qps:', sum/10)


