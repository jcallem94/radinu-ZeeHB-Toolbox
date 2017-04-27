# ----------------------------------------------------------------------  
# This model file was automatically created by SARAH version4.9.1 
# SARAH References: arXiv:0806.0538, arXiv:0909.2863, arXiv:1002.0840    
# (c) Florian Staub, 2011  
# ----------------------------------------------------------------------  
# File created at 15:37 on 18.1.2017   
# ----------------------------------------------------------------------  
 
 
from object_library import all_lorentz,Lorentz 
from function_library import complexconjugate,re,im,csc,sec,acsc,asec 
 
 
VVS99 = Lorentz(name='VVSpp', 
spins=[3,3,1], 
structure='P(1,2)*P(2,1)-P(-1,1)*P(-1,2)*Metric(1,2)')
