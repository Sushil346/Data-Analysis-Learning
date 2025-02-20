import numpy as np
import pandas as pd

#Create Empty Pandas Series  
empty=pd.Series()

### Given the X python list convert it to an Y pandas Series
X = ['A','B','C']
print(X, type(X))

Y = pd.Series(X)
print(Y, type(Y)) # different type

X = pd.Series(['A','B','C'])

X.name = 'My letters'
X