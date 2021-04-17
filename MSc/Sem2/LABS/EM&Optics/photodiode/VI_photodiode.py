import numpy as np
import matplotlib.pyplot as plt

# import data from file
data1 = np.loadtxt("i1.txt") * -1
data2 = np.loadtxt("i2.txt") * -1
v_data1 = data1[:, 0]
i_data1 = data1[:, 1]
v_data2 = data2[:, 0]
i_data2 = data2[:, 1]


plt.plot(v_data1, i_data1, ".-", label="I1")
plt.plot(v_data2, i_data2, ".-", label="I2<I1")
plt.title("V - I characteristics of photdiode at I1 & I2<I1 intensity")
plt.xlabel("Reverse bias voltage (V) $\longrightarrow$")
plt.ylabel("Reverse photocurrent (I)$(\mu A)\longrightarrow$")
plt.grid()
plt.legend(loc="best")
plt.savefig("photodiode.pdf")
plt.show()
