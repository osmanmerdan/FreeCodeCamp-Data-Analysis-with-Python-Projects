import numpy as np

import numpy as np

def calculate(list):

    #If a list containing less than 9 elements is passed into the function,
    #it should raise a ValueError exception with the message: 
    #"List must contain nine numbers."  
    
    if len(list)!=9:
        raise ValueError('List must contain nine numbers.')
    
    #create an array from the given list and reshape it in 3x3 format
    a=np.array([list]).reshape(3,3)
    
    #create a calculations dictionary 
    #dictionary will store values as lists
    calculations={
  'mean': [],
  'variance': [],
  'standard deviation': [],
  'max': [],
  'min': [],
  'sum': []
    }
    
    #create a loop for each axis
    #columns,rows and flattened-->[0,1,None]
    #convert arrays to list with .tolist() method
    #append lists to corresponding keys in the dictionary
    for ax in [0,1,None]:
        calculations['sum'].append((a.sum(axis=ax)).tolist())
        calculations['min'].append((a.min(axis=ax)).tolist())
        calculations['max'].append((a.max(axis=ax)).tolist())
        calculations['standard deviation'].append((a.std(axis=ax)).tolist())
        calculations['variance'].append((a.var(axis=ax)).tolist())
        calculations['mean'].append((a.mean(axis=ax)).tolist())


    return calculations