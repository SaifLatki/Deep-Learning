import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.maximum(0, x)
dy_dx = np.where(x > 0, 1, 0)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(x, y, label='ReLU')
axs[0].set_title('ReLU Activation Function')
axs[0].legend()
axs[1].plot(x, dy_dx, label='Derivative')
axs[1].set_title('Derivative of ReLU Activation Function')
axs[1].legend()
plt.show()