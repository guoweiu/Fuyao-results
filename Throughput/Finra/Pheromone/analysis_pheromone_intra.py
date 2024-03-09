import os


current_directory = os.path.dirname(os.path.abspath(__file__))

dirs_path = [
    current_directory + '/intra/10(80ins, 100qps, 10s)',
    current_directory + '/intra/20(80ins, 100qps, 60s)',
    current_directory + '/intra/40(80ins, 100qps, 10s)',
    current_directory + '/intra/60(80ins, 100qps, 10s)',
    current_directory + '/intra/80(80ins, 100qps, 10s)',
]

# sums = []
for dir_path in dirs_path:
    for root, dirs, files in os.walk(dir_path):
        sum = 0
        files_path = [os.path.join(root, file) for file in files]
        for file_path in files_path:
            with open(file_path, 'r') as f:
                for line in f:
                    if 'req_id' in line:
                        sum += 1
        # sums.append(sum)
        # print('dir:', root, ' qps:', sum/10)

        print('dir:', root, ' sum:', sum)

