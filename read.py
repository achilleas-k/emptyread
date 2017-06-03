import h5py
import numpy as np


hfile = h5py.File("emptyread.h5", mode='w')
grp = hfile.create_group("grp")
ds = grp.create_dataset("data", data=np.random.random((3, 10, 5)))

for idx in range(200):
    print(idx)
    emptythingie = np.empty((1,))
    sl = (slice(1, 2, None), slice(1, 2, None), slice(0, 1, None))
    print(sl)
    print(ds.shape)
    print(emptythingie.shape)
    print(ds[:])
    ds.read_direct(emptythingie, sl)

hfile.close()
