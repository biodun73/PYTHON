import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([5,10,15,20,25])
x_axis = plt.xlabel("X axis")
y_axis = plt.ylabel("Y axis")

plt.plot(x,y,
         color="red",
         linewidth="5",
         marker="o",
         markersize=20, 
         markeredgecolor="green")
plt.title("plot grapy")
plt.show()