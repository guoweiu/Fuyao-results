import os

abs_path = 'f20/fuyao'
# abs_path = 'f20/openfaas-new'

files = ['q100', 'q200', 'q300', 'q400', 'q500', 'q600']

for file_path in files:

    file_path_c = abs_path + '/' + file_path
    cpu_total = 0.0
    with open(file_path_c, 'r') as file:
        for line in file:
            if 'gateway' in line or 'engine' in line:
                parts = line.split()
                index_value = ''
                if 'S' in parts:
                    index_value = 'S'
                elif 'R' in parts:
                    index_value = 'R'
                elif 'Z' in parts:
                    index_value = 'Z'
                else:
                    index_value = 'D'
                cpu_percentage_index = parts.index(index_value) + 1  # 找到%CPU所在的位置
                cpu_percentage = float(parts[cpu_percentage_index])
                cpu_total += cpu_percentage

    avg_cpu_c = cpu_total / 10

    file_path_f = abs_path + '/' + file_path
    cpu_total = 0.0
    with open(file_path_f, 'r') as file:
        for line in file:
            if 'exp' in line:
                parts = line.split()
                index_value = ''
                if 'S' in parts:
                    index_value = 'S'
                elif 'R' in parts:
                    index_value = 'R'
                elif 'Z' in parts:
                    index_value = 'Z'
                else:
                    index_value = 'D'
                cpu_percentage_index = parts.index(index_value) + 1  # 找到%CPU所在的位置
                cpu_percentage = float(parts[cpu_percentage_index])
                cpu_total += cpu_percentage

    avg_cpu_f = cpu_total / 10

    print(file_path, "total_cpu: ", avg_cpu_f + avg_cpu_c, "avg_cpu_c: ", avg_cpu_c, "avg_cpu_f: ", avg_cpu_f)
