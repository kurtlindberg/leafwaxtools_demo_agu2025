'''
leafwaxtools.Chain().acl()
'''

from leafwaxtools import Chain
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

qpt_acl = Chain(qpt_chain_arr).acl(
    chain_lengths=[22,24,26,28]
)


fig, axs = plt.subplots(2,1,layout='constrained')

ax = axs[0]
ax.plot(
    qpt_df.age, qpt_acl,
    color='black', marker='o', markersize=5, label="ACL"
)
ax.set_xlim([6000,-100])
ax.set_xticks(
    ticks=[6000,5500,5000,4500,4000,3500,3000,2500,2000,1500,1000,500,0],
    labels=[6,"",5,"",4,"",3,"",2,"",1,"",0]
)
ax.set_xlabel("Age (cal kyr BP)")
ax.set_ylim([24.5,26.5])
ax.set_yticks(
    ticks=[24.5,25,25.5,26,26.5],
    # labels=[24,"",25,"",26,"",27]
)
ax.set_ylabel("ACL (C22-C28)")
ax.grid(visible=False)
ax.legend(
    loc='center left',
    bbox_to_anchor=(1,0.5)
)

fig.delaxes(axs[1])


figure_qpt_acl = plt.gcf()
# figure_qpt_acl.savefig("figures/qpt_acl.svg", dpi=300)
