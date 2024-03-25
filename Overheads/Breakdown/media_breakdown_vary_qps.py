import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager
matplotlib.rcParams["font.family"] = 'Helvetica'
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

import numpy as np

# fig = plt.subplots(figsize=(4.65, 1.8), dpi=300)
fig = plt.subplots(figsize=(2.325, 1.8), dpi=300)
plt.subplots_adjust(hspace=None, wspace=None, top=0.99, bottom=0.26, left=0.19, right=0.99)


width = 0.35
gap = 0.08

requests_per_second = ["10", "50", "100", "200", "500", "800", "1000", "1200", "1400"]

intra_latency =  [6.955, 6.301, 6.598, 5.537, 5.819, 4.514, 8.620, 6.756, 8.465]
intra_execution_latency = [5.854, 4.707, 5.497, 4.664, 4.178, 3.695, 6.356, 5.748, 7.162]

inter_latency = [5.980, 5.792, 6.172, 5.914, 5.370,  7.053, 5.953, 5.549, 7.373]
inter_execution_latency = [4.865, 4.709, 5.166, 4.323, 3.856, 5.135, 5.027, 4.125, 6.016]

pers = []

comms = []

for i in range(len(intra_latency)):
    pers.append((intra_latency[i] - intra_execution_latency[i]) / intra_latency[i])
    pers.append((inter_latency[i] - inter_execution_latency[i]) / inter_latency[i])

    comms.append(intra_latency[i] - intra_execution_latency[i])
    comms.append(inter_latency[i] - inter_execution_latency[i])

# print(pers)
# print(sum(pers)/len(pers))

# print(comms)
# print(sum(comms)/len(comms))

# exit(0)

indexs = []

DRC_lats = []
overheads = []

for i in range(len(requests_per_second)):
    indexs.append(i - width/2 - gap/2)
    indexs.append(i + width/2 + gap/2)

    DRC_lats.append(intra_execution_latency[i])
    DRC_lats.append(inter_execution_latency[i])

    overheads.append((intra_latency[i] - intra_execution_latency[i]))
    overheads.append((inter_latency[i] - inter_execution_latency[i]))

# back_colors = ["#3182BD", "#c6dbef"]
# back_colors = ["#3182BD", "#08519C"]
back_colors = ["#00ADB5", "#60a865"]
back_colors = ["#00ADB5", "#F8A400"]

back_colors = ["#acc4ed", "#e3f0d8"]

linewidth = 0.5

mpl.rcParams['hatch.linewidth'] = 0.5

ylim = 10

bar1 = plt.bar(indexs, DRC_lats, width=width, color=back_colors[0], edgecolor="#000000", linewidth=linewidth, zorder=2)
bar2 = plt.bar(indexs, overheads, width=width, color=back_colors[1], edgecolor="#000000", linewidth=linewidth, zorder=2, bottom=DRC_lats)

# bar2 = plt.bar(indexs, overheads, bottom=DRC_lats, width=width, color="white", edgecolor=back_colors[1], hatch="xxxx" ,
    # linewidth=linewidth, zorder=2, label="Handshake overhead")
# bar3 = plt.bar(indexs, overheads, bottom=DRC_lats, width=width, color='none', edgecolor="k",
#     linewidth=linewidth, zorder=2)

# for i in range(len(indexs)):
#     if DRC_lats[i] + overheads[i] > ylim:
#         xs = np.linspace(indexs[i] - width/2 - 0.01, indexs[i] + width/2 + 0.01, 100)
#         # print(xs)
#         ys1 = []
#         ys2 = []
#         for xx in xs:
#             # ys1.append(250000 + 0.2 * ((xx - (indexs[i] - width/2 - 0.01))/(width + 0.02)))
#             # ys2.append(270000 + 0.2 * ((xx - (indexs[i] - width/2 - 0.01))/(width + 0.02)))
#
#             ys1.append(290)
#             ys2.append(293)
#
#         plt.fill_between(xs, ys1, ys2, color="white", zorder=3)
#
#         # plt.plot([indexs[i] - width/2 - 0.01, indexs[i] + width/2 + 0.01], [250000, 270000], color="k", lw=0.5, zorder=4)
#         # plt.plot([indexs[i] - width/2 - 0.01, indexs[i] + width/2 + 0.01], [270000, 290000], color="k", lw=0.5, zorder=4)
#
#         # plt.plot([indexs[i] - width/2 - 0.01, indexs[i] + width/2 + 0.01], [290, 290], color="k", lw=0.5, zorder=4)
#         # plt.plot([indexs[i] - width/2 - 0.01, indexs[i] + width/2 + 0.01], [293, 293], color="k", lw=0.5, zorder=4)
#
#         plt.text(indexs[i] + 0.02, 290, str(DRC_lats[i] + overheads[i]), ha="center", va="top", rotation=90)


# plt.legend([bar1, (bar2, bar3)], ["Execution", "Communication"], framealpha=0.5, loc=(0, 0.6))
plt.legend([bar1, bar2], ["Exec", "Comm"], framealpha=0.5, loc=(0, 0.63))

# plt.text(indexs[8] + width/2, intra_latency[4], "Intra", ha="right", va="bottom")

# plt.text(indexs[9] - width/2, inter_latency[4], "Inter", ha="left", va="bottom")

plt.text(indexs[10], intra_latency[5] + 0.1, "Intra", ha="center", va="bottom", rotation=90, fontsize=9)

plt.text(indexs[11], inter_latency[5] + 0.1, "Inter", ha="center", va="bottom", rotation=90, fontsize=9)

plt.gca().set_xticks(range(len(requests_per_second)))
plt.gca().set_xticklabels(requests_per_second, rotation=40)
plt.gca().tick_params(axis='x', which='major', pad=-2)

plt.yticks(rotation=60)
plt.gca().tick_params(axis='y', which='major', pad=0)

plt.xlabel("Throughput (queries per second)", labelpad=1, loc="right")

plt.ylim(0, ylim)

plt.grid(ls="--", zorder=1, axis="y")

plt.ylabel("Time (ms)", labelpad=0)

plt.savefig('media_breakdown_vary_qps.pdf')

plt.show()