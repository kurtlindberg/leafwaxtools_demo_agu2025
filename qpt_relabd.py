'''
leafwaxtools.Chain.relative_abd()
'''

from leafwaxtools import Chain
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns


plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 16
plt.rcParams['font.family'] = "Liberation Sans"


qpt_df = pd.read_csv("gorbey2021qpt.csv")

qpt_chain_df = qpt_df[
    [
        # 'c20concentration',
        'c22concentration',
        'c24concentration',
        'c26concentration',
        'c28concentration',
        # 'c30concentration'
    ]
]
qpt_chain_arr = np.array(qpt_chain_df)

qpt_relabd = Chain(qpt_chain_arr).relative_abd(calculate_percent=True)

qpt_sum = np.zeros(shape=np.shape(qpt_relabd))
qpt_sum[:,0] = qpt_relabd[:,0]

for row in range(0, len(qpt_relabd[:,0])):
    for col in range(1, len(qpt_relabd[1,:])):
        qpt_sum[row,col] = np.sum(qpt_relabd[row,0:col+1])


# Figure script
fig, axs = plt.subplots(2,1,layout='constrained')

colors = [
    '#1b7837',          # C22
    '#7fbf7b',          # C24
    '#af8dc3',          # C26
    '#762a83'           # C28
    # '#d9f0d3',        # unused
    # '#e7d4e8',        # unused
]

ax = axs[0]
for c in range(0, len(colors)):
    sns.barplot(
        ax=ax, x=qpt_df.age, y=qpt_sum[:,c],
        color=colors[c], edgecolor='black', width=1,
        native_scale=True, zorder=(len(colors)-c)
    )
ax.set_xlim([6000,-100])
ax.set_xticks(
    ticks=[6000,5500,5000,4500,4000,3500,3000,2500,2000,1500,1000,500,0],
    labels=[6,"",5,"",4,"",3,"",2,"",1,"",0]
)
ax.set_xlabel("Age (cal kyr BP)")
ax.set_ylim([0,100])
ax.set_yticks(
    ticks=[0,25,50,75,100],
    labels=[0,25,50,75,100]
)
ax.set_ylabel("% Abundance")
ax.grid(visible=False)

# c30 = mpatches.Patch(color=colors[5], label='C30')
c28 = mpatches.Patch(color=colors[3], label='C28')
c26 = mpatches.Patch(color=colors[2], label='C26')
c24 = mpatches.Patch(color=colors[1], label='C24')
c22 = mpatches.Patch(color=colors[0], label='C22')
# c20 = mpatches.Patch(color=colors[0], label='C20')

ax.legend(
    handles=[c28,c26,c24,c22],
    loc='center left',
    bbox_to_anchor=(1,0.5)
)

fig.delaxes(axs[1])
    
    
figure_qpt_relabd = plt.gcf()
figure_qpt_relabd.savefig("figures/qpt_relabd.png", dpi=300)

