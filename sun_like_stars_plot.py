import numpy as np
import matplotlib.pyplot as plt

teff,logg = np.loadtxt('randomstarset.txt',skiprows=1,usecols=(0,1),unpack=True)
plt.figure(figsize=(8,5))

plt.gcf().subplots_adjust(bottom=0.17, wspace=0.0, top=0.86, right=0.94, left=0.16)
ax = plt.gca()


ax.set_xlim(12000, 2000)
ax.set_ylim(6,-1)
ax.set_ylabel('Surface Gravity (log g)', fontsize=18)
ax.set_xlabel('Temperature (K)', fontsize=18)
ax.set_title ('Kepler Stars',fontsize=22)

plt.rcParams['axes.linewidth']=3
plt.rcParams['xtick.major.width'] = 2
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['xtick.minor.width'] = 2
plt.rcParams['ytick.minor.width'] = 2
plt.rc('xtick.major', size=8, pad=8)
plt.rc('xtick.minor', size=6, pad=5)
plt.rc('ytick.major', size=8, pad=8)
plt.rc('ytick.minor', size=6, pad=5)

plt.plot(teff,logg,'o')
plt.semilogx()


ax.set_xticks([12000,11000,10000,9000,8000,7000,6000,5000,4000,3000,2000])
ax.set_xticklabels(['12000','','','9000','','','6000','','4000','3000','2000'], fontsize=14)
ax.set_yticks(np.arange(-1, 6+1, 1))
ax.set_yticklabels(np.arange(-1, 6+1, 1), fontsize=14)


plt.show()

