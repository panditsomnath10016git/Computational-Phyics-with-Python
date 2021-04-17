import numpy as np
import matplotlib.pyplot as plt

# import data from file
data = np.loadtxt("red.txt")
v_data = data[:,0]
i_data = data[:,1]

plt.plot(v_data, i_data, ".-g")
plt.title("V - I characteristics of red LED")
plt.xlabel("Bias voltage (V) $\longrightarrow$")
plt.ylabel("Photocurrent (I)$(\mu A)\longrightarrow$")
plt.grid()
plt.savefig("red.pdf")
plt.show()
