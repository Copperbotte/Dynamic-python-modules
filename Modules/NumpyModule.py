
import numpy as np
print("Numpy module loaded")

def Numpyfunc():
    print("Numpy sine:", np.sin(10.0))

def register():
    print("Numpy module registered") 
    return Numpyfunc.__name__, Numpyfunc
