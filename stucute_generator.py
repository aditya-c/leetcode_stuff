import numpy as np

z = np.arange(1, ).reshape(11, 11)
z[z > 21] = 0
print(z.astype(bool).tolist())
