import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

p_data = np.loadtxt("plateau.txt")
h_data = np.loadtxt("Vheight.txt")

p_volt = p_data[:, 0]
p_count = p_data[:, 1]
h_volt = h_data[:, 0]
h_height = h_data[:, 1]

# get plateau region data
p_region_v = []
p_region_r = []
for v, r in zip(p_volt, p_count):
    if 250 < r < 350:
        p_region_v += [v]
        p_region_r += [r]

p_coeff = poly.polyfit(p_region_v, p_region_r, 1)
p_v_fit = np.linspace(p_region_v[0], p_region_v[-1], 10)
p_r_fit = poly.polyval(p_v_fit, p_coeff)
v_f, v_i = p_v_fit[-1], p_v_fit[0]
r_f, r_i = p_r_fit[-1], p_r_fit[0]
operating_v = (v_f + v_i) / 2
p_slope = 100 * 100 * (r_f - r_i) / (r_i * (v_f - v_i))
# print((r_f-r_i)/r_i,r_i,r_f,operating_v, p_slope)

plt.plot(p_volt, p_count, "o")
plt.plot(p_v_fit, p_r_fit)
plt.title("Plateau Characteristics of a G.M Counter")
plt.xlabel("Baseline Voltage(Volt)$\longrightarrow$")
plt.ylabel("Count /20s$\longrightarrow$")
plt.text(v_i - 50, r_i, "($V_1,R_1$)")
plt.annotate("($V_2,R_2$)", (v_f, r_f))
plt.text(
    550,
    30,
    "Operating voltage = %r V\nSlope(in %% per 100V) = %.3f%%" % (operating_v, p_slope),
)
plt.grid()
plt.savefig("plateau.svg")
plt.show()

plt.plot(h_volt, h_height, "o-")
plt.title("Variation of GM Pulse height with Baseline Voltage")
plt.xlabel("Baseline Voltage (Volt)$\longrightarrow$")
plt.ylabel("Pulse height (Volt)$\longrightarrow$")
plt.grid()
plt.savefig("Vheight.svg")
plt.show()
