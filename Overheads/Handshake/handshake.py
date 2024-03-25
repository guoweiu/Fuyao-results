import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager
matplotlib.rcParams["font.family"] = 'Helvetica'
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

import numpy as np

# fig = plt.subplots(figsize=(4.65, 1.8), dpi=300)
fig = plt.subplots(figsize=(2.325, 1.8), dpi=300)

plt.subplots_adjust(hspace=None, wspace=None, top=0.99, bottom=0.26, left=0.18, right=0.99)


width = 0.35
gap = 0.08

workflows = ["Media", "Chain-2", "Chain-16", "Chain-32", "Chain-64", "Chain-128", "FINRA-10", "FINRA-20", "FINRA-40", "FINRA-60", "FINRA-80"]

intra_cold_lats = [57690, 16798, 102385, 201648, 394285, 793784, 53522, 121238, 185900, 310070, 514653]
intra_warm_lats = [4930, 319, 2211, 3892, 7471, 16030, 1652, 2986, 3996, 10515, 11916]

inter_cold_lats = [67968, 18585, 122202, 221648, 487725, 976156, 60224, 141238, 195900, 393010, 522971]
inter_warm_lats = [5720, 329, 2983, 4557, 9889, 16096, 1702, 2986, 4506, 10978, 12529]

indexs = []

DRC_lats = []
overheads = []

for i in range(len(workflows)):
    indexs.append(i - width/2 - gap/2)
    indexs.append(i + width/2 + gap/2)

    DRC_lats.append(intra_warm_lats[i]/1000.0)
    DRC_lats.append(inter_warm_lats[i]/1000.0)

    overheads.append((intra_cold_lats[i] - intra_warm_lats[i])/1000.0)
    overheads.append((inter_cold_lats[i] - inter_warm_lats[i])/1000.0)

# back_colors = ["#3182BD", "#c6dbef"]
# back_colors = ["#3182BD", "#08519C"]
back_colors = ["#00ADB5", "#F9BB31"]
back_colors = ["#00ADB5", "#F8A400"]

back_colors = ["#acc4ed", "#e3f0d8"]

linewidth = 0.5

mpl.rcParams['hatch.linewidth'] = 0.5

ylim = 300

bar1 = plt.bar(indexs, DRC_lats, width=width, color=back_colors[1], edgecolor="#000000", linewidth=linewidth, zorder=2)
bar2 = plt.bar(indexs, overheads, width=width, color=back_colors[0], edgecolor="#000000", linewidth=linewidth, zorder=2, bottom=DRC_lats)
# bar2 = plt.bar(indexs, overheads, bottom=DRC_lats, width=width, color="white", edgecolor=back_colors[1], hatch="xxxx" ,
#     linewidth=linewidth, zorder=2, label="Handshake overhead")
# bar3 = plt.bar(indexs, overheads, bottom=DRC_lats, width=width, color='none', edgecolor="k", 
#     linewidth=linewidth, zorder=2)

for i in range(len(indexs)):
    if DRC_lats[i] + overheads[i] > ylim:
        xs = np.linspace(indexs[i] - width/2 - 0.01, indexs[i] + width/2 + 0.01, 100)
        # print(xs)
        ys1 = []
        ys2 = []
        for xx in xs:
            ys1.append(285 + 5 * ((xx - (indexs[i] - width/2 - 0.01))/(width + 0.02)))
            ys2.append(290 + 5 * ((xx - (indexs[i] - width/2 - 0.01))/(width + 0.02)))

        plt.fill_between(xs, ys1, ys2, color="white", zorder=3)

        plt.plot([indexs[i] - width/2 - 0.01, indexs[i] + width/2 + 0.01], [285, 290], color="k", lw=0.5, zorder=4)
        plt.plot([indexs[i] - width/2 - 0.01, indexs[i] + width/2 + 0.01], [290, 295], color="k", lw=0.5, zorder=4)

        # plt.text(indexs[i] + 0.02, 285, str(round(overheads[i], 1)), ha="right", va="top", rotation=40, fontsize=7)

        if i == 8 or i == 18:
            plt.text(indexs[i] - width/2, 295, str(int(overheads[i])), ha="right", va="top", fontsize=9)
        elif i == 11:
            plt.text(indexs[i] + width/2, 295, str(int(overheads[i])), ha="left", va="top", fontsize=9)
        elif i == 21:
            plt.annotate("", xy=(indexs[i] + width/2, 205), 
            xytext=(-31, 0), textcoords="offset points", arrowprops=dict(arrowstyle="<-", connectionstyle="arc", color="black", lw=0.8),
            fontsize=9, color="black")
            plt.text(indexs[i] - width/2 - 2.1, 205, str(int(overheads[i])), ha="right", va="center", fontsize=9)
        elif i % 2 == 1:
            plt.annotate("", xy=(indexs[i] + width/2, 255), 
            xytext=(-20, 0), textcoords="offset points", arrowprops=dict(arrowstyle="<-", connectionstyle="arc", color="black", lw=0.8),
            fontsize=9, color="black")
            plt.text(indexs[i] - width/2 - 1.1, 255, str(int(overheads[i])), ha="right", va="center", fontsize=9)
        elif i == 10:
            plt.annotate("", xy=(indexs[i] + width/2, 230), 
            xytext=(-27, 0), textcoords="offset points", arrowprops=dict(arrowstyle="<-", connectionstyle="arc", color="black", lw=0.8),
            fontsize=9, color="black")
            plt.text(indexs[i] - width/2 - 1.7, 230, str(int(overheads[i])), ha="right", va="center", fontsize=9)
        elif i == 20:
            plt.annotate("", xy=(indexs[i] + width/2, 230), 
            xytext=(-27, 0), textcoords="offset points", arrowprops=dict(arrowstyle="<-", connectionstyle="arc", color="black", lw=0.8),
            fontsize=9, color="black")
            plt.text(indexs[i] - width/2 - 1.7, 230, str(int(overheads[i])), ha="right", va="center", fontsize=9)
        elif i % 2 == 0:
            plt.text(indexs[i] + width/2 + 0.03, 280, str(int(overheads[i])), ha="center", va="top", fontsize=7, rotation=20)
        else:
            plt.text(indexs[i] + 0.5, 285, str(int(overheads[i])), ha="right", va="top", rotation=60, fontsize=7)


plt.legend([bar1, bar2], ["Data Transfer", "Handshake"], framealpha=0.5, 
    loc=(0.28, 0.3)
    )


plt.text(indexs[0] + width/2, intra_cold_lats[0]/1000.0 + 5, "Intra", ha="right", va="bottom", rotation=90, fontsize=9)
plt.text(indexs[1] - width/2, inter_cold_lats[0]/1000.0 + 5, "Inter", ha="left", va="bottom", rotation=90, fontsize=9)

# plt.annotate("Intra", xy=(indexs[0], intra_cold_lats[0]/1000.0 - 10), xytext=(-0.6, intra_cold_lats[0]/1000.0 + 50), 
#     arrowprops=dict(arrowstyle="->"))

# plt.annotate("Inter", xy=(indexs[1] + 0.1, 50), xytext=(0.8, 50 - 8), 
#     arrowprops=dict(arrowstyle="->"))


plt.gca().set_xticks(range(len(workflows)))
# plt.gca().set_xticklabels(workflows, rotation=30)
plt.gca().set_xticklabels([i + "       " for i in workflows], rotation=40, fontsize=9)
plt.gca().tick_params(axis='x', which='major', pad=-12)

plt.yticks(rotation=60)
plt.gca().tick_params(axis='y', which='major', pad=0)

plt.ylim(0, ylim)

# plt.yscale("log")

plt.grid(ls="--", zorder=1, axis="y")

plt.ylabel("Time (ms)", labelpad=0)

plt.savefig('handshake.pdf')

plt.show()