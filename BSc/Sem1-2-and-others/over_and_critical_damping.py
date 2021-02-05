import math as m
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

np = 3200
xmax = 5.0
x0 = 0.0
y0 = 1.0
h = (xmax - x0) / (np - 1)
w = 4
b = b_critical = 4
b_over = 10
xp = [0.0] * np
yp = [0.0] * np
yo = [0.0] * np
yc = [0.0] * np

for j in range(2):
    x = x0
    y = y0
    y1 = 0.5
    y2 = 0.0
    for i in range(np):
        y2 = -(2 * b * y1 + w ** 2 * y)
        y = yp[i] = y + h * y1 + (h ** 2 / 2) * y2
        y1 = y1 + h * y2
        xp[i] = x + i * h
    b = b_over
    if j == 0:
        yc = yp
        yp = [0.0] * np
    else:
        yo = yp


plt.plot(
    xp,
    yc,
    "-r",
    xp,
    yo,
    "-b",
)
plt.title(" over and critical damping")
cp = mpatches.Patch(
    color="red",
    label="critical damping",
)
op = mpatches.Patch(
    color="blue",
    label="over damping",
)
plt.legend(handles=[cp] + [op])
plt.savefig(" over and critical damp.png")
# plt.show()
