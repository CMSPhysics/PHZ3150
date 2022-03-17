import numpy as np
import math

def kepler_3rd(planet_x, p1, p2, a1):
    """Function that gets as input the orbital period of a planet in years and returns the orbital distance of a planet to the Sun.
    Input: Planet of interest(planet_x), orbital period planet Earth(p1) days, orbital period planet x(p2) days, distane planet Earth(a1) AU
    Output: Orbital distance planet x(a2) AU"""
    
    a2 = np.round(np.cbrt(((p2**2)*(a1**3))/(p1**2)), 2)
    
    print('The distance from the planet', planet_x, 'is', a2, 'AU.')
    
    return a2 
    
def piston(V,P0,V0,T0,gamma):
    """Calculates the pressures for the piston volumes in V, using the adiabatic law, and calculates the temperatures using the ideal gas law.
    Input: Volume(L), inital pressure (ATM), inital temperature (K), gamma 
    Output: pressure(ATM), temperature(K)"""

    const = (P0*V0)/T0
    const1 = P0*(V0**gamma)
    
    P = const1/(V**gamma)
    T = P*V/ const
              
    Piston = np.array([P, V, T])
    
    return Piston