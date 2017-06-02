import h5py
import numpy as np


hfile = h5py.File("emptyread.h5", mode='w')
grp = hfile.create_group("grp")
ds = grp.create_dataset("data", data=np.random.random((10, 5, 10)))

for idx in range(200):
    print(idx)
    emptythingie = np.empty([])
    ds.read_direct(emptythingie,
                   (slice(1, 2, None), slice(1, 2, None), slice(0, 1, None)))

hfile.close()
