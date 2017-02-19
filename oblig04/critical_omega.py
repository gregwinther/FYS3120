import numpy as np
from matplotlib import pyplot as plt

m = 1
R = 1
g = 9.81

def W(theta, omega):
    return -(1.0/2)*R*R*omega*omega*np.sin(theta)*np.sin(theta) \
            - m*g*R*np.cos(theta)

critical_omega = np.sqrt(g/R)
omega_small = 0.5*critical_omega
omega_large = 1.5*critical_omega

theta = np.linspace(-2*np.pi, 2*np.pi, 1000)

W_small = W(theta, omega_small)
W_large = W(theta, omega_large)

plt.plot(theta, W_small, label=r'$\omega=0.5\omega_{cr}$')
plt.plot(theta, W_large, label=r'$\omega=1.5\omega_{cr}$')

plt.title(r'$W(\theta)$')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$W(\theta)$')
plt.legend()

plt.show()