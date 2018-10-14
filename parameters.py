import math

global pi,degtorad,dtoyr,c,kpctom,yrts,Vs,Rskpc,conversion
pi = math.pi
degtorad= pi/180.0
dtoyr = 1.0/365.25
c = 299792458.0 #m/s
kpctom = 3.0856775814913675e+19
yrts = 365.25*24.0*3600.0
conversion = 1000.0/(c*yrts*pow(10.0,6.0))


inp = open('parameters.in','r')
x=[]
for line in inp:
   s=line.split() 
   x.append(s)

Vs = float(x[0][2])
sigVs = float(x[1][2])

Rskpc = float(x[2][2])
sigRs = float(x[3][2]) 


b0reid14 = float(x[4][2])
sigb0r = float(x[5][2])

b0dt91 = float(x[6][2])
sigb0dt = float(x[7][2])


# --- parameters and errors in those ----
'''
Vs = 220.0 #km/s
sigVs = 7.0

Rskpc = 8.0 #kpc
sigRs = 0.17 


b0reid14 = -0.2 # km s^-1 kpc^-1, (dV/dR)
sigb0r = 0.4

b0dt91 = 0.00 # [-(Rs/V)*(dV/dR)]at R = Rs
sigb0dt = 0.03
'''


