import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pylab as plt
from matplotlib import rcParams
import matplotlib.colors as colors
import matplotlib.cbook as cbook
from matplotlib.lines import Line2D

rcParams.update({'figure.autolayout': True})
sns.set_style("whitegrid", rc={"axes.edgecolor": "k"})
sns.set_style("ticks", {"xtick.major.size":8,"ytick.major.size":8})

sns.set_context("notebook",rc={"grid.linewidth": 0, 
                            "font.family":"Helvetica", "axes.labelsize":24.,"xtick.labelsize":24., 
                            "ytick.labelsize":24., "legend.fontsize":20.})

colors = sns.color_palette("colorblind", 12)

pot_E = pd.read_csv('potential.xvg', delim_whitespace=True, skiprows=24, header=None, names=['Time','Energy'])

fig = plt.figure(figsize=(12,8))
plt.plot(pot_E['Time'], pot_E['Energy'], linewidth=3, color='black')
plt.xlim(0,800)
plt.ylabel('Potential Energy (kJ/mol)', labelpad=10)
plt.xlabel('Time (ps)', labelpad=10)
plt.title('Energy Minimization', fontsize=26)
plt.savefig('EM_PotE.png', dpi=400)
plt.show()
