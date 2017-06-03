import numpy as np


print("Using numpy version: {}".format(np.__version__))

for idx in range(200):
    print(idx)
    emptythingie = np.empty((1,))
    emptythingie.resize(())

print("DONE")
