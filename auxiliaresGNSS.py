import numpy as np
from numpy import pi, sqrt, sin, cos, exp, log10, array, real, conj
from cuentitas import a0VV, a1VVF1, a1VVF2

def generadorS0(thi,ep1,ep2,d,s1,s2,ZA):
    
    landa = 0.19
    k0 = 2*np.pi/landa
    phi = 0
    ph = phi
    th = thi
    
    s0s = 1 + 2*np.real(a0VV(k0,thi,ep1,ep2,d)*exp(1j*2*k0*cos(th)*ZA))+abs(a0VV(k0,thi,ep1,ep2,d))**2\
        + abs(a1VVF1(k0,thi,phi,th,ph,ep1,ep2,d))**2*s1**2 + abs(a1VVF2(k0,thi,phi,th,ph,ep1,ep2,d))**2*s2**2
    
    s0s = 10*np.log10(s0s) #paso a db
    
    
    sM = np.mean(s0s) #normalizo
    s0 = (s0s-sM)/np.max(np.abs(s0s-sM))
    return s0

def generadorS0ruido(thi,ep1,ep2,d,s1,s2,ZA,noise):
    
    landa = 0.19
    k0 = 2*np.pi/landa
    phi = 0
    ph = phi
    th = thi
    
    s0s = 1 + 2*np.real(a0VV(k0,thi,ep1,ep2,d)*exp(1j*2*k0*cos(th)*ZA))+abs(a0VV(k0,thi,ep1,ep2,d))**2\
        + abs(a1VVF1(k0,thi,phi,th,ph,ep1,ep2,d))**2*s1**2 + abs(a1VVF2(k0,thi,phi,th,ph,ep1,ep2,d))**2*s2**2
    
    s0s = 10*np.log10(s0s) #paso a db
    
    maximo = np.max(np.abs(s0s))
    
    Noise = noise*maximo/100
    ruido = s0s + Noise*np.random.randn(len(s0s))
    
    sM = np.mean(ruido) #normalizo
    s0 = (ruido-sM)/np.max(np.abs(ruido-sM))
    return s0