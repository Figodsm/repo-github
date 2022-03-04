import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 30, 301)
k_1 = 1
k_2 = 1.1

y = plt.plot(x, np.cos(x * k_1)) 
y = plt.plot(x, np.cos(x * k_2))
plt.show