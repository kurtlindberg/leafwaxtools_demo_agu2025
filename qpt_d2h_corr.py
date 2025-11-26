'''
leafwaxtools.Isotope().corr_rvals()
'''

from leafwaxtools import Isotope
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 18
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

qpt_d2h_corr_rvals = Isotope(qpt_d2h_arr).corr_rvals()
qpt_d2h_corr_pvals = Isotope(qpt_d2h_arr).corr_pvals()


# Figure script
fig, axs = plt.subplots(1,1,layout='constrained')

corr_mask = np.triu(np.ones_like(qpt_d2h_corr_rvals, dtype=bool))

ax = axs
sns.heatmap(
    ax=ax, data=qpt_d2h_corr_rvals,
    cmap='Reds', mask=corr_mask, annot=True, fmt='.2f', vmin=0, vmax=1,
    linewidths=1, linecolor='black', clip_on=False,
    cbar=True, cbar_kws={'label': "Pearson r-value", 'shrink': 0.66},
    xticklabels=['C22','C24','C26','C28'],
    yticklabels=['C22','C24','C26','C28']
)


figure_qpt_d2h_corr = plt.gcf()
# figure_qpt_d2h_corr.savefig("figures/qpt_d2h_corr.svg", dpi=300)

