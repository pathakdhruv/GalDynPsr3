
import math
import numpy as np
from ReadGC import readGCfunc,gcinp,GCrepeat
from ExcessGal import ExcessGalfunc

a = input("Is the Pulsar in a Globular Cluster?(y/n)")
if a=='y' or a == 'Y':
   readGCfunc()
   gcinp()
   GCrepeat()
elif a == 'n' or a == 'N':
   ExcessGalfunc()
else:
   print ("Invalid Input. Try Again.")


