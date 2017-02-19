import numpy as np
from matplotlib import pyplot as plt

m = 1
R = 1
g = 9.81
omega_cr = np.sqrt(g/R)
omega = 1.5*omega_cr

def conjugate_momentum(theta, H=1):
    P = R*np.sqrt(2*m*H + (m*R*omega*np.sin(theta))**2 \
            + 2*g*m*m*R*np.cos(theta))

    return P

theta = np.linspace(-1.3*np.pi, 1.3*np.pi, 2500)


for H in np.arange(-50,50,10):
    p = conjugate_momentum(theta, H)
    plt.plot(theta,  p, 'b')
    plt.plot(theta, -p, 'b')

plt.title('Hamiltonian phase space')
plt.xlabel(r'$\theta$', fontsize=14)
plt.ylabel(r'$p_{\theta}$', fontsize=14)

plt.show()