import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
with open("data.txt", "r") as dataa:
    data = [float(i) for i in dataa.readlines()]
fig, ax = plt.subplots()
ax.minorticks_on()

time_all = 32.3655
time = np.linspace(0, time_all, num = 260)
ax.plot(time, data, color = 'blue', linestyle = '-', marker = '.', markersize = 5, markerfacecolor = 'green')
plt.xlabel('Время, с')
plt.ylabel('Напряжение, В')
ax.set_title('График лабораторная работа: Процесс заряда и разряда конденсатора в RC цепи', wrap = True)
blue_line = mlines.Line2D([], [], color = "blue", marker = ".", markersize = 10, label = "V(t)")
ax.legend(handles = [blue_line])
ax.legend()
ax.set_xlim(np.min(time), np.max(time) + 2)
ax.set_ylim(np.min(data), np.max(data) + 0.1)
plt.text(21, 1.25, 'Время разряда : 18с')
plt.text(21, 1.1, 'Время заряда : 14с')
ax.grid(which = 'major', linewidth = 1)
ax.grid(which = 'minor', linewidth = 0.5, linestyle = '--')
plt.savefig('graf.png')
plt.show()
