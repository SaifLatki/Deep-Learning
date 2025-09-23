import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
alpha = 1.0
y = np.where(x > 0, x, alpha * (np.exp(x) - 1))
dy_dx = np.where(x > 0, 1, y + alpha)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(x, y, label='ELU')
axs[0].set_title('ELU Activation Function')
axs[0].legend()
axs[1].plot(x, dy_dx, label='Derivative')
axs[1].set_title('Derivative of ELU Activation Function')
axs[1].legend()
plt.show()