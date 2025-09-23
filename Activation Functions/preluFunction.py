import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
alpha = 0.25
y = np.where(x > 0, x, alpha * x)
dy_dx = np.where(x > 0, 1, alpha)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(x, y, label='PReLU')
axs[0].set_title('PReLU Activation Function')
axs[0].legend()
axs[1].plot(x, dy_dx, label='Derivative')
axs[1].set_title('Derivative of PReLU Activation Function')
axs[1].legend()
plt.show()
