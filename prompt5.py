import numpy as np 
import matplotlib.pyplot as plt

import sys
import os

x= np.linspace(0,2*np.pi, num=1000)
y= np.sin(x)

array= np.array([[x],[y]])
print(np.array2string(array).replace('[[',' [').replace(']]',']'))