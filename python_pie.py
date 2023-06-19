import matplotlib.pyplot as plt
import numpy as np
x = np.array([ 50,60,90,80 ])
subs = ["English","Biology","Maths","Chemistry"]
xplode = [0,0.1,0,0]
plt.title("Pie chart")
plt.pie(x,labels=subs, startangle=90,explode=xplode, shadow=True)
plt.legend()
plt.show()