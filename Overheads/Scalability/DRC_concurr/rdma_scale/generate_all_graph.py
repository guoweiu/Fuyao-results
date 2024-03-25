import matplotlib.pyplot as plt
import numpy as np
import sys
import random

import pandas as pd
import seaborn as sns

import matplotlib.font_manager
matplotlib.rcParams["font.family"] = 'Helvetica'
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

def filter_extreme_3sigma(data,n=3,times=3): 
    # times进行times次3sigma处理
    series = data.copy()
    for i in range(times):
        mean = series.mean()
        std = series.std()
        max_range = mean + n*std
        min_range = mean - n*std
        series = np.clip(series,min_range,max_range)
    return series

# data_size=sys.argv[1]
data_size="1"
#file_list=["1-1-","5-20-","10-20-","15-20-","20-20-","25-20-","30-20-","35-20-","40-20-"]
#file_list=["1-1-","5-20-","10-20-","15-20-","20-20-","25-20-","30-20-","40-20-"]
file_list=["1-1-","10-10-","20-20-","40-20-","40-30-","40-40-","50-40-"]
#two_list=["40-20-1"]

data_list=[]
labels=["1","100","400","800","1200","1600","2000"]

for i, file in enumerate(file_list):
    data = np.loadtxt("./"+file+str(data_size)+".log",dtype=np.int64)
    # if file in two_list:
    #         data=filter_extreme_3sigma(data,times=2)
    # else:
    
    for d in data:
        data_list.append([int(labels[i]), d/1000.0])
    
    # data=filter_extreme_3sigma(data)

    # data_list.append(data)
#data = [0.8685, 0.6671, 0.7971, 0.5774]

palette = {}
for label in labels:
    palette[label] = "#00ADB5"

# cols = ["QP Numbers", "Latencty (μs)"]
cols = ["DRC Numbers", r"Latencty (${\rm \mu}$s)"]

df = pd.DataFrame(data=data_list, columns=cols)

fig = plt.subplots(figsize=(2.325, 1.8), dpi=300)

plt.subplots_adjust(hspace=None, wspace=0.2, top=0.99, bottom=0.22, left=0.16, right=0.99)

plt.grid(zorder=1, linestyle=":")  # 显示网格

ax = sns.boxplot(x="DRC Numbers", y=r"Latencty (${\rm \mu}$s)", data=df, linewidth=0.8, showfliers=False, width=0.5)

for box in ax.artists:
    box.set_facecolor("#00ADB5")

plt.xticks(fontsize=8, rotation=30)
plt.gca().xaxis.set_tick_params(pad=0)

plt.xlabel("DRC Numbers", labelpad=0)

# plt.boxplot(data_list,
#             medianprops={'color': 'red', 'linewidth': '1.5'},
#             meanline=True,
#             showmeans=True,
#             showfliers=True,
#             meanprops={'color': 'blue', 'ls': '--', 'linewidth': '1.5'},
#             flierprops={"marker": ".", "markerfacecolor": "red", "markersize": 1}
#             ,labels=labels)
#plt.yticks(np.arange(0.4, 0.91, 0.1))
# plt.xlabel("QP Numbers")
# plt.ylabel("latencty(ns)")
#plt.title("Delay of rdma write "+str(data_size)+" byte operation with number of QPs")

plt.savefig("./rdma_scale.pdf") 

plt.show()
