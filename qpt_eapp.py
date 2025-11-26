'''
leafwaxtools.Isotope.epsilon()
'''

from leafwaxtools import Isotope
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 16
plt.rcParams['font.family'] = "Liberation Sans"


qpt_df = pd.read_csv("gorbey2021qpt.csv")

qpt_d2h_df = qpt_df[
    [
        'c22d2h',
        'c24d2h',
        'c26d2h',
        'c28d2h'
    ]
]
qpt_d2h_arr = np.array(qpt_d2h_df)

qpt_eapp_c22_jja = Isotope(qpt_d2h_arr).epsilon(
    epsilon_numerator=np.array(qpt_d2h_df.c22d2h),
    epsilon_denominator=-97
)
qpt_eapp_c28_jja = Isotope(qpt_d2h_arr).epsilon(
    epsilon_numerator=np.array(qpt_d2h_df.c28d2h),
    epsilon_denominator=-97
)


# Figure script
fig, axs = plt.subplots(2,1,layout='constrained')

colors = [
    '#1b7837',          # C20
    '#7fbf7b',          # C22
    # '#d9f0d3',          # C24
    # '#e7d4e8',          # C26
    '#af8dc3',          # C28
    '#762a83'           # C30
]

ax = axs[0]
ax.plot(
    qpt_df.age, qpt_eapp_c28_jja,
    color=colors[3], marker='o', markersize=5, label="C28"
)
ax.plot(
    qpt_df.age, qpt_eapp_c22_jja,
    color=colors[0], marker='o', markersize=5, label="C22"
)
ax.set_xlim([6000,-100])
ax.set_xticks(
    ticks=[6000,5500,5000,4500,4000,3500,3000,2500,2000,1500,1000,500,0],
    labels=[6,"",5,"",4,"",3,"",2,"",1,"",0]
)
ax.set_xlabel("Age (cal kyr BP)")
ax.set_ylim([-180,-100])
# ax.set_yticks(
#     ticks=[],
#     labels=[]
# )
ax.set_ylabel("Eapp (VSMOW)")
ax.grid(visible=False)
ax.legend(
    loc='center left',
    bbox_to_anchor=(1,0.5)
)

fig.delaxes(axs[1])


figure_qpt_eapp = plt.gcf()
# figure_qpt_eapp.savefig("figures/qpt_eapp.svg", dpi=300)
