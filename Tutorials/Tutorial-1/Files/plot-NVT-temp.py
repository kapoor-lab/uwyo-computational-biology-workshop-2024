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

nvt_temp = pd.read_csv('temperature.xvg', delim_whitespace=True, skiprows=24, header=None, names=['Time','Temp.'])

fig = plt.figure(figsize=(12,8))
plt.plot(nvt_temp['Time'], nvt_temp['Temp.'], linewidth=3, color='black')
plt.xlim(0,100)
plt.ylabel('Temperature (K)', labelpad=10)
plt.xlabel('Time (ps)', labelpad=10)
plt.title('NVT Equilibration', fontsize=26)
plt.savefig('NVT_Temp.png', dpi=400)
plt.show()
