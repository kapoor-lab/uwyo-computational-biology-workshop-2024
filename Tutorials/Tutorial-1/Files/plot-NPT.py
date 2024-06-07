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

npt_press = pd.read_csv('pressure.xvg',  delim_whitespace=True, skiprows=24, header=None, names=['Time','Press.'])

average_npt_press = np.mean(npt_press['Press.'])
std_npt_press = np.std(npt_press['Press.'])

fig = plt.figure(figsize=(12,8))
plt.plot(npt_press['Time'], npt_press['Press.'], linewidth=3, color='black')
plt.hlines(average_npt_press, 0, 100, colors=colors[0], linewidth=5, linestyle='dashed')
plt.fill_between(npt_press['Time'], average_npt_press+std_npt_press, average_npt_press-std_npt_press, alpha=0.3)
plt.xlim(0,100)
plt.ylim(-500,500)
plt.text(10, -400, f'Average Pressure = {round(average_npt_press,2)} ± {round(std_npt_press, 2)} bar', fontsize=20)
plt.ylabel('Pressure (bar)', labelpad=10)
plt.xlabel('Time (ps)', labelpad=10)
plt.title('NPT Equilibration', fontsize=26)
plt.savefig('NPT-Press.png', dpi=400)
plt.show()

npt_density = pd.read_csv('density.xvg',  delim_whitespace=True, skiprows=24, header=None, names=['Time','Density'])

average_npt_density = np.mean(npt_density['Density'])
std_npt_density = np.std(npt_density['Density'])

fig = plt.figure(figsize=(12,8))
plt.plot(npt_density['Time'], npt_density['Density'], linewidth=3, color='black')
plt.hlines(average_npt_density, 0, 100, colors='tab:red', linewidth=5, linestyle='dashed')
plt.fill_between(npt_density['Time'], average_npt_density+std_npt_density, average_npt_density-std_npt_density, color='tab:red', alpha=0.2)
plt.xlim(0,100)
plt.ylim(990, 1030)
plt.text(10, 1010, f'Average Density = {round(average_npt_density,2)} ± {round(std_npt_density, 2)} kg m$^{{{-3}}}$', fontsize=20)
plt.ylabel('Density (kg m$^{-3}$)', labelpad=10)
plt.xlabel('Time (ps)', labelpad=10)
plt.title('NPT Equilibration', fontsize=26)
plt.savefig('NPT-Density.png', dpi=400)
plt.show()
