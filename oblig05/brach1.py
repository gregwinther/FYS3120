import numpy as np
from matplotlib import pyplot as plt

theta = np.linspace(0, 1.4*np.pi)

x = theta - np.sin(theta)
y = np.cos(theta) - 1

plt.plot(x,y)
plt.plot(x[0], y[0], 'ob')
plt.text(x[0]+0.2, y[0]-0.1, "A", fontsize=15)
plt.plot(x[-1], y[-1], 'ob')
plt.text(x[-1]-0.35, y[-1], "B", fontsize=15)
plt.plot(x[10], y[10], 'ob')
plt.text(x[10]+0.1, y[10], "P", fontsize=15)
plt.annotate('G', xy=(1, -0.75), xytext=(1, -0.5),
            arrowprops=dict(facecolor='black', shrink=0.01), fontsize=15)
plt.xticks([],[])
plt.yticks([],[])
plt.show()