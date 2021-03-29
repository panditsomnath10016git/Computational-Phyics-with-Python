import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

# import data from file
mallus_data = np.loadtxt("malus_law.txt")
QWP_rot = np.loadtxt("QWP_angles.txt")
sq_cost = np.loadtxt("table2calc.txt")

analyzer_angle = np.arange(0, 360 + 1, 1)

m_a, m_i = mallus_data[:, 0], mallus_data[:, 1]
mallus_data_ext = m_i
mallus_fit = poly.polyval(analyzer_angle, poly.polyfit(m_a, m_i, 13))

plt.plot(m_a, mallus_data_ext, ".", label="expt. data")
plt.plot(analyzer_angle, mallus_fit, label="fitted curve")
plt.title("Plot of I vs. $\\theta$")
plt.xlabel("Analyzer angle $(\\theta^o) \longrightarrow$")
plt.ylabel("Photocurrent$(\mu A) \longrightarrow$")
plt.legend(loc="best")
plt.grid()
plt.xlim(0, 360)
plt.savefig("Mallus_law.pdf")
# plt.show()

##QWP calc
q_a = QWP_rot[:, 0]

q_rads = q_a * np.pi / 180
a_rads = analyzer_angle * np.pi / 180
QWP_fit=np.zeros((len(analyzer_angle),3))

plt.axes(projection="polar")

for i, angle in enumerate([100, 130, 160]):
    d=QWP_rot[:, i+1]
    d_fit = poly.polyval(analyzer_angle, poly.polyfit(q_a, d, 13))
    QWP_fit[:,i]=d_fit
    plt.polar(q_rads, d, ".")
    plt.polar(a_rads, d_fit, label="$%d^o$"%angle)

plt.title("Intensity at different analyzer angles")
plt.legend(title="QWP angles", loc="best")
plt.savefig("QWP_rot.pdf")
# plt.show()
plt.clf()

# a,b value calc

#sq_cost[:, 0]+

for i, angle in enumerate([100, 130, 160], 1):
    a_ofst=analyzer_angle[np.argmax(QWP_fit[:, i-1])]%180
    if a_ofst>90:
        a_ofst=a_ofst-180
    cos_sqr_a = np.cos(np.arange(-a_ofst,360-a_ofst+10,10)*np.pi/180)**2
    i_data = sq_cost[:, i]
    poly_coeff = poly.polyfit(cos_sqr_a, i_data, 1)
    i_fit = poly.polyval(cos_sqr_a, poly_coeff)
    slope = (i_fit[0] - i_fit[8]) / (cos_sqr_a[0] - cos_sqr_a[8])
    b2 = poly.polyval(0, poly_coeff)
    a_by_b = (1 + (slope / b2)) ** 0.5
    print(b2, slope, a_by_b)
    plt.plot(cos_sqr_a, i_data, ".")
    plt.plot(cos_sqr_a, i_fit)
    plt.title("Plot of I vs. $\cos^2\\theta$ for QWP angle %s$^o$" % angle)
    plt.text(
        0.7,
        min(i_fit),
        "$\\theta$ offset=%r$^o$\nslope($a^2-b^2$)=%.2f\ny-intercept($b^2$)=%.2f\na/b=%.2f"
        % (a_ofst,slope, b2, a_by_b),
    )
    plt.xlabel("$\cos^2\\theta\longrightarrow$")
    plt.ylabel("I $(\mu A) \longrightarrow$")
    plt.grid()
    plt.savefig("a_by_b%s.pdf"%angle)
    plt.show()
