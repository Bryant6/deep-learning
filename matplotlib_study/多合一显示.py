# -*-coding:utf-8-*-
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 4)
plt.plot([0, 2], [0, 1])

plt.subplot(2, 3, 5)
plt.plot([0, 3], [0, 1])

plt.subplot(2, 3, 6)
plt.plot([0, 4], [0, 1])


plt.show()