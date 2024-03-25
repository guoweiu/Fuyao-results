import numpy as np
import matplotlib.pyplot as plt

import matplotlib.font_manager
# matplotlib.rcParams["font.family"] = 'Helvetica'

# import matplotlib as mpl

# mpl.rcParams['text.usetex'] = True

# matplotlib.rcParams["font.family"] = 'Times New Roman'
# matplotlib.rcParams["font.weight"] = 'bold'

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

# mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

# plt.rc('text', usetex=True)

fig = plt.figure(dpi=300, figsize=(3, 2.2))

plt.subplots_adjust(hspace=0.0, wspace=None, top=0.95, bottom=0.10, left=0.18, right=0.99)

workload = []

for i in ["2", "3", "4"]:
    with open(i+"-smooth-10.txt", "r") as f:
        lines = f.readlines()
        lines = [float(l) for l in lines]
    workload.append(lines)

for i in range(len(workload)):
    window = 2
    smooth = []
    for j in range(0, len(workload[i]), window):
        temp = workload[i][j:min(j+window, len(workload[i]))]
        smooth.append(sum(temp)/len(temp))
    workload[i] = smooth


index = range(len(workload[0]))

print(workload[0])
print(workload[1])
print(workload[2])


# D62428 FF7F0E 1F77B4

linewidth = 1.8
# line1 = plt.plot(index, workload[0], color="#F40000", label="Sporadic", linewidth=linewidth)
# line1 = plt.plot(index, workload[0], color="#D62428", label="Sporadic", linewidth=linewidth, zorder=3)
# line1 = plt.plot(index, workload[0], color="red", label="Sporadic", linewidth=linewidth, zorder=3)

# line2 = plt.plot(index, workload[1], color="#51FF00", label="Periodic", linewidth=linewidth)
# line2 = plt.plot(index, workload[1], color="#FF7F0E", label="Periodic", linewidth=linewidth)
# line2 = plt.plot(index, workload[1], color="#B8B8B8", label="Periodic", linewidth=linewidth)

# line3 = plt.plot(index, workload[2], color="#1D0FFF", label="Bursty")
line3 = plt.plot(index, workload[2], color="#6096E6", label="Bursty", linewidth=linewidth)
# line3 = plt.plot(index, workload[2], color="#1F77B4", label="Bursty", linewidth=linewidth)

# print(dir(line3))
# line3.set_zorder(0)
# plt.rc('text', usetex=True)

plt.ylim((-8, 15))
# plt.yticks([0, 5, 10, 15], fontsize=15, color="#A0A0A0")
plt.yticks([0, 5, 10, 15], fontsize=15)

ticks = int(len(workload[0]) / 6)
xticks = [ticks, 3*ticks, 5*ticks]

# xt = plt.xticks(xticks, ["TUES", "WED", "THU"], fontsize=15, color="#A0A0A0")
xt = plt.xticks(xticks, ["TUES", "WED", "THU"], fontsize=15)
# print(dir(xt[0]))
plt.grid()

plt.gca().yaxis.set_tick_params(direction="in", which="major")
plt.gca().xaxis.set_tick_params(direction="in", which="major")

plt.legend(ncol=2,  loc=(0.01, 0.02), 
    # fontsize=15,
    borderpad=0.1, 
    labelspacing=0.25,
    columnspacing=0.2,
    handletextpad=0.15
    )

plt.gca().spines["bottom"].set_color("#A0A0A0")
# plt.gca().spines["bottom"].set_linewidth(1)
# ax.spines["top"].set_color("k")
plt.gca().spines["left"].set_color("#A0A0A0")
# plt.gca().spines["left"].set_linewidth(1)

plt.ylabel("Arrival Intensity [r/s]")

plt.show()

# fig.savefig("ArrivalIntensity.pdf")
