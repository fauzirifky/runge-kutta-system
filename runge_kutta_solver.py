
import math as ma
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc



def SIR(x, param) : 
    S = x[0]
    I = x[1]
    R = x[2]
    beta = param[0]
    gamma = param[1]
    
    N = S + I + R

    dS = -beta*S*I/N
    dI = beta*S*I/N - gamma*I
    dR = gamma*I
    
    return np.array([dS, dI, dR])

def RK4solver(func, param, tspan, init):
    dim = len(init)
    ntime = len(tspan)
    dz = tspan[1] - tspan[0]
    y = np.zeros((ntime, dim))
    y[0,:] = init
    
    n = 0
    while (n < ntime - 1):
        k1             = func(y[n,:]                , param )
        k2             = func(y[n,:] + 0.5 * dz * k1, param )
        k3             = func(y[n,:] + 0.5 * dz * k2, param )
        k4             = func(y[n,:] +       dz * k3, param )
        y[n + 1,:]     = y[n,:] + dz / 6 * ( k1 + 2 * k2 + 2 * k3 + k4 )
        n = n + 1;
    return y

#simulation
R0 = 2.2
gamma = 1/10
beta = gamma*R0
param = [beta, gamma]
y0 = [N-1, 1, 0]
tspan = np.linspace(0,20,100)
y = RK4solver(SIR, param, tspan, y0)
