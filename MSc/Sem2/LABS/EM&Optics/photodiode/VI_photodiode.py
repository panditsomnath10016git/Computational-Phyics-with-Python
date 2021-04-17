import numpy as np
import matplotlib.pyplot as plt

# import data from file
data = np.loadtxt("i2.txt")
v_data = data[:,0]
i_data = data[:,1]

plt.plot(v_data, i_data, ".-")
plt.title("V - I characteristics of photdiode with I2 intensity")
plt.xlabel("Bias voltage (V) $\longrightarrow$")
plt.ylabel("Photocurrent (I)$(\mu A)\longrightarrow$")
plt.grid()
plt.savefig("i2.pdf")
plt.show()
