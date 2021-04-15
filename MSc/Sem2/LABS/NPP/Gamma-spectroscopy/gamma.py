import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
from interpolate import cubic_spline_interpolate

cs = np.loadtxt("Cs.txt")
co = np.loadtxt("Co.txt")
unknown = np.loadtxt("unknown.txt")


sources = [["Cs-137", "cs"], ["Co-60", "co"], ["Unknown-source", "unknown"]]
peak_pos = np.array([[2, 3], [5, 6, 6, 7], [2, 3]])
peak_v = []
peak_count = []
FWHM_V = []
photofrac = []

for k, source in enumerate(sources):
    v = eval(source[1])[:, 0]
    count = eval(source[1])[:, 2]
    V = np.arange(0, max(v), 0.01)
    Count_inp = cubic_spline_interpolate(v, count, V)
    # print( source, v)
    area_tot = np.trapz(Count_inp, V)
    # find peaks
    peaks = peak_pos[k]
    v_peak = []
    count_peak = []
    for peak_i in range(int(len(peaks) / 2)):
        i = 2 * peak_i
        temp_max = count[0]
        for v_ in v:
            if peaks[i] <= v_ <= peaks[i + 1]:
                n = count[np.where(v == v_)]
                if n > temp_max:
                    temp_max = n

        v_p = [v[np.where(count == temp_max)[0][0]]]
        v_peak += v_p
        count_peak += [temp_max]
        peak_v += v_p

        ##find FWHM
        half_count_minus = abs(Count_inp - (temp_max / 2))
        min_v_i = np.where(V == peaks[i])[0][0]
        max_v_i = np.where(V == peaks[i + 1])[0][0]
        max_c_i = np.where(Count_inp == temp_max)[0][0]
        i_1 = min_v_i + np.argmin(half_count_minus[min_v_i:max_c_i])
        i_2 = max_c_i + np.argmin(half_count_minus[max_c_i:max_v_i])
        fwhm_v = abs(V[i_1] - V[i_2])
        FWHM_V += [fwhm_v]

        ##PhotoFraction
        area_peak = np.trapz(Count_inp[i_1:i_2], V[i_1:i_2])
        area_frac = area_peak / area_tot
        photofrac += [area_frac]
        print(
            "area under peak =",
            area_peak,
            "\ntotal area =",
            area_tot,
            "\nPhotofraction =",
            area_frac,
        )

    plt.plot(v, count, ".")
    plt.plot(V, Count_inp)
    for xy in zip(v_peak, count_peak):
        plt.annotate("(%.1f, %d)" % xy, xy)
    plt.title("Energy spectrum of %s" % source[0])
    plt.xlabel("Baseline Voltage(V) -->")
    plt.ylabel("Counts -->")
    plt.grid()
    plt.savefig("%s.pdf" % (source[1]))
    plt.show()
    plt.clf()

gamma_E = [661.7, 1173.2, 1332.25]
p_coeff = poly.polyfit(peak_v[:-1], gamma_E, 1)
E_fit = poly.polyval(peak_v, p_coeff)
E_unkn = E_fit[-1]
gamma_E += [E_unkn]
slope = (E_fit[0] - E_fit[1]) / (peak_v[0] - peak_v[1])
ycut = poly.polyval(0, p_coeff)


plt.plot(peak_v, gamma_E, "o")
plt.plot(peak_v, E_fit, peak_v[-1], E_unkn, "o")
plt.title("Energy Calibration")
plt.xlabel("Baseline Voltage(V) -->")
plt.ylabel("Energy (KeV) -->")
xy = (peak_v[-1], E_unkn)
plt.annotate("(%.1f,%.1f)" % xy, xy)
plt.text(5, 700, "y=%.2f*x+%.2f" % (slope, ycut))
plt.grid()
plt.savefig("calibration.pdf")
plt.show()

# resolution
FWHM_V = np.array(FWHM_V)
peak_v = np.array(peak_v)
dE = slope * FWHM_V
E = slope * peak_v + ycut
R = dE / E
print("dE = ", dE)
print("E = ", E)
print("R = ", R)

lnE = np.log(E)
lnR = np.log(R)
plt.plot(lnE, lnR, "o")
coeff = poly.polyfit(lnE, lnR, 1)
lnE_fit = np.linspace(min(lnE), max(lnE), 500)
lnR_fit = poly.polyval(lnE_fit, coeff)
plt.plot(lnE_fit, lnR_fit)
slope = (lnR_fit[0] - lnR_fit[1]) / (lnE_fit[0] - lnE_fit[1])
plt.text(7, -2.4, "slope = %.2f" % slope)
plt.xlabel("ln(E) -->")
plt.ylabel("ln(R) -->")
plt.grid()
plt.savefig("lnR.pdf")
plt.show()

# photofraction
P = np.array(photofrac)
print("P = ", P)
lnP = np.log(P)
plt.plot(lnE, lnP, "o")
coeff = poly.polyfit(lnE, lnP, 1)
lnP_fit = poly.polyval(lnE_fit, coeff)
plt.plot(lnE_fit, lnP_fit)
slope = (lnP_fit[0] - lnP_fit[1]) / (lnE_fit[0] - lnE_fit[1])
plt.text(6.5, -1.8, "slope = %.2f" % slope)
plt.xlabel("ln(E) -->")
plt.ylabel("ln(P) -->")
plt.grid()
plt.savefig("lnP.pdf")
plt.show()
