#indexing dataframe
#.loc() : locatoin based
# .iloc() : Interger based
# .ix() : Both integer and location based

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4, 3),
index = ['a', 'b', 'c', 'd'], columns = ['X', 'Y', 'Z'])

print (df.loc['c'] > 0)
