import os

files = ["pheromone/{}.txt".format(i) for i in range(1, 21)]

for file_path in files:
    cpu_total = 0.0
    with open(file_path, 'r') as file:
        for line in file:
            if 'executor' in line:
                parts = line.split()
                cpu_percentage_index = parts.index('R') + 1  # 找到%CPU所在的位置
                cpu_percentage = float(parts[cpu_percentage_index])
                cpu_total += cpu_percentage

    print(f'file_path: {file_path}. Total CPU percentage from lines containing "executor": {cpu_total}')

