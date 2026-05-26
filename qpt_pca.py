'''
leafwaxtools.Chain().pca()
'''

from leafwaxtools import Chain
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 16
plt.rcParams['font.family'] = "Liberation Sans"


qpt_df = pd.read_csv("gorbey2022qpt.csv")

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

qpt_pca = Chain(qpt_chain_arr).pca(
    chain_lengths=[22,24,26,28],
    use_clr=True
)


# Figure script
fig, axs = plt.subplots(1,1,layout='constrained')

ax = axs
for i, feature in enumerate(qpt_pca["features"]):
    ax.arrow(
        0, 0, qpt_pca["loadings"][0,i], qpt_pca["loadings"][1,i],
        head_width=0.05, head_length=0.05, color='black'
    )
    ax.text(
        qpt_pca["loadings"][0,i] * 1.15, qpt_pca["loadings"][1,i] * 1.15,
        "C" + str(feature), fontsize=16
    )
sns.scatterplot(
    ax=ax, x=qpt_pca["wax_pc1_score"], y=qpt_pca["wax_pc2_score"],
    s=125, hue=qpt_df.age, palette='Blues_r', edgecolors='black', zorder=10
)
ax.axhline(y=0, color='black', linestyle='--', linewidth=0.75, zorder=5)
ax.axvline(x=0, color='black', linestyle='--', linewidth=0.75, zorder=5)
ax.set_xlabel("PC1 (" + str(np.round(qpt_pca["pca"].explained_variance_ratio_[0]*100, decimals=0)) + "%)")
ax.set_ylabel("PC2 (" + str(np.round(qpt_pca["pca"].explained_variance_ratio_[1]*100, decimals=0)) + "%)")
ax.set_xlim([-0.9,0.9])
ax.set_xticks(
    ticks=[-0.9,-0.6,-0.3,0,0.3,0.6,0.9],
    labels=[-0.9,-0.6,-0.3,0,0.3,0.6,0.9]
)
ax.set_ylim([-0.9,0.9])
ax.set_yticks(
    ticks=[-0.9,-0.6,-0.3,0,0.3,0.6,0.9],
    labels=[-0.9,-0.6,-0.3,0,0.3,0.6,0.9]
)
ax.legend('', frameon=False)

norm = plt.Normalize(qpt_df['age'].min(), qpt_df['age'].max())
sm = plt.cm.ScalarMappable(cmap='Blues_r', norm=norm)
sm.set_array([])
ax.figure.colorbar(sm, ax=ax,
    location='right', shrink=0.8, label="Age (cal kyr BP)",
)

    
figure_qpt_pca = plt.gcf()
# figure_qpt_pca.savefig("figures/qpt_pca.png", dpi=300)
