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

r_gyr = pd.read_csv('gyrate.xvg',  delim_whitespace=True, skiprows=27, header=None, names=['Time','Rg', 'Rg,x', 'Rg,y', 'Rg,z'])

fig = plt.figure(figsize=(12,8))
plt.plot(r_gyr['Time']/1000, r_gyr['Rg'], linewidth=3, color='black')
plt.xlim(0,1)
plt.ylim(1.3,1.5)
plt.ylabel('R$_{g}$ (nm)', labelpad=10)
plt.xlabel('Time (ns)', labelpad=10)
plt.title('Radius of Gyration', fontsize=26)
plt.savefig('Protein_Rgyration.png', dpi=400)
plt.show()
