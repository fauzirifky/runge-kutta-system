#kode hanya angin

import math as ma
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc


amax = init1;
def f(x, y, Us, mu, sig) : return [y,   ( 1/F - ((1 - Us)**2)/(x**3) )*y/mu - y**2/x - (x-1)*(x**2 + (1-Us**2)*x + (1-Us)**2)/(mu*sig*x**3)  ];


ls = [ '-', '--', '-.', ':', 'o', 'v', '^', '<', '>', '1', '2', '3', '4','s', 'p', '*', 'h', 'H','+','x','D','d','|', '_']; 


h = [[]]*len(mun);
w = [[]]*len(mun);
wmin = [];
hmin = [];
for j in range( len(mun)):
    mu = mun[j]
    for k in range(50):
        y1 = [amax]; #h
        y2 = [0]; #w
        for n in range(Nt):
                     k1          = f(y1[n]                    , y2[n]                   , c,  mu, sig );
                     k2          = f(y1[n] + 0.5 * dz * k1[0] , y2[n] + 0.5 * dz * k1[1] , c,  mu, sig );
                     k3          = f(y1[n] + 0.5 * dz * k2[0] , y2[n] + 0.5 * dz * k2[1] , c,  mu, sig );
                     k4          = f(y1[n] +       dz * k3[0] , y2[n] +       dz * k3[1] , c,  mu, sig );
                     y1.append(y1[n] + dz / 6 * ( k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0] ));
                     y2.append(y2[n] + dz / 6 * ( k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1] ));
                     n = n + 1;
        amax = max(y1);
        amin = min(y1);
    wmin.append(min(y2));
    hmin.append(min(y1));
    h[j] = y1;
    w[j] = y2;
    amax = init1;

