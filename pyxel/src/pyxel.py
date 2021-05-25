import numpy as np
from primeFunctionalities import *
import matplotlib.pyplot as plt

'''
check = np.zeros((512, 512))
check[::2, 1::2] = 1
check[1::2, ::2] = 1

# We plot the image
plt.axis('off')
plt.imshow(check, cmap='gray', interpolation='nearest')
plt.savefig('../images/books_read.png', transparent=True)
'''
pf = PrimeFunctionalities()

print(pf.MCD([20, 5]))