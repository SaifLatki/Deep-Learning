import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))
dy_dx = y * (1 - y)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(x, y, label='Sigmoid')
axs[0].set_title('Sigmoid Activation Function')
axs[0].legend()
axs[1].plot(x, dy_dx, label='Derivative')
axs[1].set_title('Derivative of Sigmoid Activation Function')
axs[1].legend()