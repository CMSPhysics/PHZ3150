import numpy as np

def circle(x,x0,y0,r):
    """Function that takes an array of x, the circles centre coordinates x0, y0, and radius r, and returns all y coordinates.
    Input: xarray[x], centre coordinates[ x0, y0], radius[r]
    Output: yarray[y]"""
    
    y1 = y0-np.sqrt((r**2)-(x-x0)**2)
    y2 = y0+np.sqrt((r**2)-(x-x0)**2)
  
    
    return [y1,y2]

def order_array(input_array):
    """Function takes an input array and orders them from small to large.
    Input: input_array,
    Output: Numbers from small to large."""
    
    n = len(input_array)
    
    for i in range(n):
        for j in range(1, n-i):
            if input_array[j-1] > input_array[j]:
                (input_array[j-1], input_array[j]) = (input_array[j], input_array[j-1])

    print(input_array)
            