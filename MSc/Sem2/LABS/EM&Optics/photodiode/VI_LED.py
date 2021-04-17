import numpy as np
import matplotlib.pyplot as plt

# import data from file
data = np.loadtxt("green.txt")
v_data = data[:, 0]
i_data = data[:, 1]

plt.plot(v_data, i_data, ".-g")
plt.title("V - I characteristics of green LED")
plt.xlabel("Bias voltage (V) $\longrightarrow$")
plt.ylabel("Photocurrent (I)$(\mu A)\longrightarrow$")
plt.grid()
plt.tight_layout()
plt.savefig("green.pdf")
plt.show()
