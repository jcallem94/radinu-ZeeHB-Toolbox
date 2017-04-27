# ----------------------------------------------------------------------  
# This model file was automatically created by SARAH version4.9.1 
# SARAH References: arXiv:0806.0538, arXiv:0909.2863, arXiv:1002.0840    
# (c) Florian Staub, 2011  
# ----------------------------------------------------------------------  
# File created at 16:0 on 18.1.2017   
# ----------------------------------------------------------------------  
 
 
from object_library import all_parameters,Parameter 
 
from function_library import complexconjugate,re,im,csc,sec,acsc,asec 
 
ZERO=Parameter(name='ZERO', 
                      nature='internal', 
                      type='real', 
                      value='0.0', 
                      texname='0') 
 
Md1 = 	 Parameter(name = 'Md1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.0035, 
	 texname = '\\text{Md1}', 
	 lhablock = 'MASS', 
	 lhacode = [1]) 
 
Md2 = 	 Parameter(name = 'Md2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.104, 
	 texname = '\\text{Md2}', 
	 lhablock = 'MASS', 
	 lhacode = [3]) 
 
Md3 = 	 Parameter(name = 'Md3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 4.2, 
	 texname = '\\text{Md3}', 
	 lhablock = 'MASS', 
	 lhacode = [5]) 
 
Mu1 = 	 Parameter(name = 'Mu1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.0015, 
	 texname = '\\text{Mu1}', 
	 lhablock = 'MASS', 
	 lhacode = [2]) 
 
Mu2 = 	 Parameter(name = 'Mu2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1.27, 
	 texname = '\\text{Mu2}', 
	 lhablock = 'MASS', 
	 lhacode = [4]) 
 
Mu3 = 	 Parameter(name = 'Mu3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 171.2, 
	 texname = '\\text{Mu3}', 
	 lhablock = 'MASS', 
	 lhacode = [6]) 
 
Wu3 = 	 Parameter(name = 'Wu3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1.51, 
	 texname = '\\text{Wu3}', 
	 lhablock = 'DECAY', 
	 lhacode = [6]) 
 
Me1 = 	 Parameter(name = 'Me1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.000511, 
	 texname = '\\text{Me1}', 
	 lhablock = 'MASS', 
	 lhacode = [11]) 
 
Me2 = 	 Parameter(name = 'Me2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.105, 
	 texname = '\\text{Me2}', 
	 lhablock = 'MASS', 
	 lhacode = [13]) 
 
Me3 = 	 Parameter(name = 'Me3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1.776, 
	 texname = '\\text{Me3}', 
	 lhablock = 'MASS', 
	 lhacode = [15]) 
 
MetI = 	 Parameter(name = 'MetI', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MetI}', 
	 lhablock = 'MASS', 
	 lhacode = [36]) 
 
WetI = 	 Parameter(name = 'WetI', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WetI}', 
	 lhablock = 'DECAY', 
	 lhacode = [36]) 
 
Mh1 = 	 Parameter(name = 'Mh1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mh1}', 
	 lhablock = 'MASS', 
	 lhacode = [25]) 
 
Wh1 = 	 Parameter(name = 'Wh1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wh1}', 
	 lhablock = 'DECAY', 
	 lhacode = [25]) 
 
Mh2 = 	 Parameter(name = 'Mh2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mh2}', 
	 lhablock = 'MASS', 
	 lhacode = [35]) 
 
Wh2 = 	 Parameter(name = 'Wh2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wh2}', 
	 lhablock = 'DECAY', 
	 lhacode = [35]) 
 
MHp2 = 	 Parameter(name = 'MHp2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MHp2}', 
	 lhablock = 'MASS', 
	 lhacode = [37]) 
 
WHp2 = 	 Parameter(name = 'WHp2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WHp2}', 
	 lhablock = 'DECAY', 
	 lhacode = [37]) 
 
MHp3 = 	 Parameter(name = 'MHp3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MHp3}', 
	 lhablock = 'MASS', 
	 lhacode = [900037]) 
 
WHp3 = 	 Parameter(name = 'WHp3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WHp3}', 
	 lhablock = 'DECAY', 
	 lhacode = [900037]) 
 
MZ = 	 Parameter(name = 'MZ', 
	 nature = 'external', 
	 type = 'real', 
	 value = 91.1876, 
	 texname = '\\text{MZ}', 
	 lhablock = 'MASS', 
	 lhacode = [23]) 
 
WZ = 	 Parameter(name = 'WZ', 
	 nature = 'external', 
	 type = 'real', 
	 value = 2.4952, 
	 texname = '\\text{WZ}', 
	 lhablock = 'DECAY', 
	 lhacode = [23]) 
 
WWp = 	 Parameter(name = 'WWp', 
	 nature = 'external', 
	 type = 'real', 
	 value = 2.141, 
	 texname = '\\text{WWp}', 
	 lhablock = 'DECAY', 
	 lhacode = [24]) 
 
repsU11 = 	 Parameter(name='repsU11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU11}', 
	 lhablock = 'EPSU', 
	 lhacode = [1, 1] ) 
 
iepsU11 = 	 Parameter(name='iepsU11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU11}', 
	 lhablock = 'IMEPSU', 
	 lhacode = [1, 1] ) 
 
repsU12 = 	 Parameter(name='repsU12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU12}', 
	 lhablock = 'EPSU', 
	 lhacode = [1, 2] ) 
 
iepsU12 = 	 Parameter(name='iepsU12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU12}', 
	 lhablock = 'IMEPSU', 
	 lhacode = [1, 2] ) 
 
repsU13 = 	 Parameter(name='repsU13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU13}', 
	 lhablock = 'EPSU', 
	 lhacode = [1, 3] ) 
 
iepsU13 = 	 Parameter(name='iepsU13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU13}', 
	 lhablock = 'IMEPSU', 
	 lhacode = [1, 3] ) 
 
repsU21 = 	 Parameter(name='repsU21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU21}', 
	 lhablock = 'EPSU', 
	 lhacode = [2, 1] ) 
 
iepsU21 = 	 Parameter(name='iepsU21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU21}', 
	 lhablock = 'IMEPSU', 
	 lhacode = [2, 1] ) 
 
repsU22 = 	 Parameter(name='repsU22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU22}', 
	 lhablock = 'EPSU', 
	 lhacode = [2, 2] ) 
 
iepsU22 = 	 Parameter(name='iepsU22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU22}', 
	 lhablock = 'IMEPSU', 
	 lhacode = [2, 2] ) 
 
repsU23 = 	 Parameter(name='repsU23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU23}', 
	 lhablock = 'EPSU', 
	 lhacode = [2, 3] ) 
 
iepsU23 = 	 Parameter(name='iepsU23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU23}', 
	 lhablock = 'IMEPSU', 
	 lhacode = [2, 3] ) 
 
repsU31 = 	 Parameter(name='repsU31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU31}', 
	 lhablock = 'EPSU', 
	 lhacode = [3, 1] ) 
 
iepsU31 = 	 Parameter(name='iepsU31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU31}', 
	 lhablock = 'IMEPSU', 
	 lhacode = [3, 1] ) 
 
repsU32 = 	 Parameter(name='repsU32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU32}', 
	 lhablock = 'EPSU', 
	 lhacode = [3, 2] ) 
 
iepsU32 = 	 Parameter(name='iepsU32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU32}', 
	 lhablock = 'IMEPSU', 
	 lhacode = [3, 2] ) 
 
repsU33 = 	 Parameter(name='repsU33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU33}', 
	 lhablock = 'EPSU', 
	 lhacode = [3, 3] ) 
 
iepsU33 = 	 Parameter(name='iepsU33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsU33}', 
	 lhablock = 'IMEPSU', 
	 lhacode = [3, 3] ) 
 
repsD11 = 	 Parameter(name='repsD11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD11}', 
	 lhablock = 'EPSD', 
	 lhacode = [1, 1] ) 
 
iepsD11 = 	 Parameter(name='iepsD11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD11}', 
	 lhablock = 'IMEPSD', 
	 lhacode = [1, 1] ) 
 
repsD12 = 	 Parameter(name='repsD12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD12}', 
	 lhablock = 'EPSD', 
	 lhacode = [1, 2] ) 
 
iepsD12 = 	 Parameter(name='iepsD12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD12}', 
	 lhablock = 'IMEPSD', 
	 lhacode = [1, 2] ) 
 
repsD13 = 	 Parameter(name='repsD13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD13}', 
	 lhablock = 'EPSD', 
	 lhacode = [1, 3] ) 
 
iepsD13 = 	 Parameter(name='iepsD13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD13}', 
	 lhablock = 'IMEPSD', 
	 lhacode = [1, 3] ) 
 
repsD21 = 	 Parameter(name='repsD21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD21}', 
	 lhablock = 'EPSD', 
	 lhacode = [2, 1] ) 
 
iepsD21 = 	 Parameter(name='iepsD21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD21}', 
	 lhablock = 'IMEPSD', 
	 lhacode = [2, 1] ) 
 
repsD22 = 	 Parameter(name='repsD22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD22}', 
	 lhablock = 'EPSD', 
	 lhacode = [2, 2] ) 
 
iepsD22 = 	 Parameter(name='iepsD22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD22}', 
	 lhablock = 'IMEPSD', 
	 lhacode = [2, 2] ) 
 
repsD23 = 	 Parameter(name='repsD23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD23}', 
	 lhablock = 'EPSD', 
	 lhacode = [2, 3] ) 
 
iepsD23 = 	 Parameter(name='iepsD23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD23}', 
	 lhablock = 'IMEPSD', 
	 lhacode = [2, 3] ) 
 
repsD31 = 	 Parameter(name='repsD31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD31}', 
	 lhablock = 'EPSD', 
	 lhacode = [3, 1] ) 
 
iepsD31 = 	 Parameter(name='iepsD31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD31}', 
	 lhablock = 'IMEPSD', 
	 lhacode = [3, 1] ) 
 
repsD32 = 	 Parameter(name='repsD32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD32}', 
	 lhablock = 'EPSD', 
	 lhacode = [3, 2] ) 
 
iepsD32 = 	 Parameter(name='iepsD32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD32}', 
	 lhablock = 'IMEPSD', 
	 lhacode = [3, 2] ) 
 
repsD33 = 	 Parameter(name='repsD33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD33}', 
	 lhablock = 'EPSD', 
	 lhacode = [3, 3] ) 
 
iepsD33 = 	 Parameter(name='iepsD33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsD33}', 
	 lhablock = 'IMEPSD', 
	 lhacode = [3, 3] ) 
 
repsE11 = 	 Parameter(name='repsE11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE11}', 
	 lhablock = 'EPSE', 
	 lhacode = [1, 1] ) 
 
iepsE11 = 	 Parameter(name='iepsE11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE11}', 
	 lhablock = 'IMEPSE', 
	 lhacode = [1, 1] ) 
 
repsE12 = 	 Parameter(name='repsE12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE12}', 
	 lhablock = 'EPSE', 
	 lhacode = [1, 2] ) 
 
iepsE12 = 	 Parameter(name='iepsE12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE12}', 
	 lhablock = 'IMEPSE', 
	 lhacode = [1, 2] ) 
 
repsE13 = 	 Parameter(name='repsE13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE13}', 
	 lhablock = 'EPSE', 
	 lhacode = [1, 3] ) 
 
iepsE13 = 	 Parameter(name='iepsE13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE13}', 
	 lhablock = 'IMEPSE', 
	 lhacode = [1, 3] ) 
 
repsE21 = 	 Parameter(name='repsE21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE21}', 
	 lhablock = 'EPSE', 
	 lhacode = [2, 1] ) 
 
iepsE21 = 	 Parameter(name='iepsE21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE21}', 
	 lhablock = 'IMEPSE', 
	 lhacode = [2, 1] ) 
 
repsE22 = 	 Parameter(name='repsE22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE22}', 
	 lhablock = 'EPSE', 
	 lhacode = [2, 2] ) 
 
iepsE22 = 	 Parameter(name='iepsE22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE22}', 
	 lhablock = 'IMEPSE', 
	 lhacode = [2, 2] ) 
 
repsE23 = 	 Parameter(name='repsE23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE23}', 
	 lhablock = 'EPSE', 
	 lhacode = [2, 3] ) 
 
iepsE23 = 	 Parameter(name='iepsE23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE23}', 
	 lhablock = 'IMEPSE', 
	 lhacode = [2, 3] ) 
 
repsE31 = 	 Parameter(name='repsE31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE31}', 
	 lhablock = 'EPSE', 
	 lhacode = [3, 1] ) 
 
iepsE31 = 	 Parameter(name='iepsE31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE31}', 
	 lhablock = 'IMEPSE', 
	 lhacode = [3, 1] ) 
 
repsE32 = 	 Parameter(name='repsE32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE32}', 
	 lhablock = 'EPSE', 
	 lhacode = [3, 2] ) 
 
iepsE32 = 	 Parameter(name='iepsE32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE32}', 
	 lhablock = 'IMEPSE', 
	 lhacode = [3, 2] ) 
 
repsE33 = 	 Parameter(name='repsE33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE33}', 
	 lhablock = 'EPSE', 
	 lhacode = [3, 3] ) 
 
iepsE33 = 	 Parameter(name='iepsE33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{epsE33}', 
	 lhablock = 'IMEPSE', 
	 lhacode = [3, 3] ) 
 
rYh11 = 	 Parameter(name='rYh11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh11}', 
	 lhablock = 'YH', 
	 lhacode = [1, 1] ) 
 
iYh11 = 	 Parameter(name='iYh11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh11}', 
	 lhablock = 'IMYH', 
	 lhacode = [1, 1] ) 
 
rYh12 = 	 Parameter(name='rYh12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh12}', 
	 lhablock = 'YH', 
	 lhacode = [1, 2] ) 
 
iYh12 = 	 Parameter(name='iYh12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh12}', 
	 lhablock = 'IMYH', 
	 lhacode = [1, 2] ) 
 
rYh13 = 	 Parameter(name='rYh13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh13}', 
	 lhablock = 'YH', 
	 lhacode = [1, 3] ) 
 
iYh13 = 	 Parameter(name='iYh13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh13}', 
	 lhablock = 'IMYH', 
	 lhacode = [1, 3] ) 
 
rYh21 = 	 Parameter(name='rYh21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh21}', 
	 lhablock = 'YH', 
	 lhacode = [2, 1] ) 
 
iYh21 = 	 Parameter(name='iYh21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh21}', 
	 lhablock = 'IMYH', 
	 lhacode = [2, 1] ) 
 
rYh22 = 	 Parameter(name='rYh22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh22}', 
	 lhablock = 'YH', 
	 lhacode = [2, 2] ) 
 
iYh22 = 	 Parameter(name='iYh22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh22}', 
	 lhablock = 'IMYH', 
	 lhacode = [2, 2] ) 
 
rYh23 = 	 Parameter(name='rYh23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh23}', 
	 lhablock = 'YH', 
	 lhacode = [2, 3] ) 
 
iYh23 = 	 Parameter(name='iYh23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh23}', 
	 lhablock = 'IMYH', 
	 lhacode = [2, 3] ) 
 
rYh31 = 	 Parameter(name='rYh31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh31}', 
	 lhablock = 'YH', 
	 lhacode = [3, 1] ) 
 
iYh31 = 	 Parameter(name='iYh31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh31}', 
	 lhablock = 'IMYH', 
	 lhacode = [3, 1] ) 
 
rYh32 = 	 Parameter(name='rYh32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh32}', 
	 lhablock = 'YH', 
	 lhacode = [3, 2] ) 
 
iYh32 = 	 Parameter(name='iYh32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh32}', 
	 lhablock = 'IMYH', 
	 lhacode = [3, 2] ) 
 
rYh33 = 	 Parameter(name='rYh33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh33}', 
	 lhablock = 'YH', 
	 lhacode = [3, 3] ) 
 
iYh33 = 	 Parameter(name='iYh33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Yh33}', 
	 lhablock = 'IMYH', 
	 lhacode = [3, 3] ) 
 
rlam1 = 	 Parameter(name='rlam1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam1}', 
	 lhablock = 'HDM', 
	 lhacode = [2] ) 
 
ilam1 = 	 Parameter(name='ilam1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam1}', 
	 lhablock = 'IMHDM', 
	 lhacode = [2] ) 
 
rlam2 = 	 Parameter(name='rlam2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam2}', 
	 lhablock = 'HDM', 
	 lhacode = [3] ) 
 
ilam2 = 	 Parameter(name='ilam2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam2}', 
	 lhablock = 'IMHDM', 
	 lhacode = [3] ) 
 
rlam4 = 	 Parameter(name='rlam4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam4}', 
	 lhablock = 'HDM', 
	 lhacode = [5] ) 
 
ilam4 = 	 Parameter(name='ilam4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam4}', 
	 lhablock = 'IMHDM', 
	 lhacode = [5] ) 
 
rlam3 = 	 Parameter(name='rlam3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam3}', 
	 lhablock = 'HDM', 
	 lhacode = [4] ) 
 
ilam3 = 	 Parameter(name='ilam3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam3}', 
	 lhablock = 'IMHDM', 
	 lhacode = [4] ) 
 
rlam7 = 	 Parameter(name='rlam7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam7}', 
	 lhablock = 'HDM', 
	 lhacode = [8] ) 
 
ilam7 = 	 Parameter(name='ilam7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam7}', 
	 lhablock = 'IMHDM', 
	 lhacode = [8] ) 
 
lam5 = 	 Parameter(name='lam5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam5}', 
	 lhablock = 'HDM', 
	 lhacode = [6] ) 
 
rlam6 = 	 Parameter(name='rlam6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam6}', 
	 lhablock = 'HDM', 
	 lhacode = [7] ) 
 
ilam6 = 	 Parameter(name='ilam6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam6}', 
	 lhablock = 'IMHDM', 
	 lhacode = [7] ) 
 
rlam9 = 	 Parameter(name='rlam9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam9}', 
	 lhablock = 'HDM', 
	 lhacode = [10] ) 
 
ilam9 = 	 Parameter(name='ilam9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam9}', 
	 lhablock = 'IMHDM', 
	 lhacode = [10] ) 
 
rlam8 = 	 Parameter(name='rlam8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam8}', 
	 lhablock = 'HDM', 
	 lhacode = [9] ) 
 
ilam8 = 	 Parameter(name='ilam8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam8}', 
	 lhablock = 'IMHDM', 
	 lhacode = [9] ) 
 
rlamh = 	 Parameter(name='rlamh', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lamh}', 
	 lhablock = 'HDM', 
	 lhacode = [12] ) 
 
ilamh = 	 Parameter(name='ilamh', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lamh}', 
	 lhablock = 'IMHDM', 
	 lhacode = [12] ) 
 
rmu = 	 Parameter(name='rmu', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{mu}', 
	 lhablock = 'HDM', 
	 lhacode = [15] ) 
 
imu = 	 Parameter(name='imu', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{mu}', 
	 lhablock = 'IMHDM', 
	 lhacode = [15] ) 
 
rlam10 = 	 Parameter(name='rlam10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam10}', 
	 lhablock = 'HDM', 
	 lhacode = [11] ) 
 
ilam10 = 	 Parameter(name='ilam10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{lam10}', 
	 lhablock = 'IMHDM', 
	 lhacode = [11] ) 
 
ZP11 = 	 Parameter(name='ZP11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP11}', 
	 lhablock = 'CHARGEMIX', 
	 lhacode = [1, 1] ) 
 
ZP12 = 	 Parameter(name='ZP12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP12}', 
	 lhablock = 'CHARGEMIX', 
	 lhacode = [1, 2] ) 
 
ZP13 = 	 Parameter(name='ZP13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP13}', 
	 lhablock = 'CHARGEMIX', 
	 lhacode = [1, 3] ) 
 
ZP21 = 	 Parameter(name='ZP21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP21}', 
	 lhablock = 'CHARGEMIX', 
	 lhacode = [2, 1] ) 
 
ZP22 = 	 Parameter(name='ZP22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP22}', 
	 lhablock = 'CHARGEMIX', 
	 lhacode = [2, 2] ) 
 
ZP23 = 	 Parameter(name='ZP23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP23}', 
	 lhablock = 'CHARGEMIX', 
	 lhacode = [2, 3] ) 
 
ZP31 = 	 Parameter(name='ZP31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP31}', 
	 lhablock = 'CHARGEMIX', 
	 lhacode = [3, 1] ) 
 
ZP32 = 	 Parameter(name='ZP32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP32}', 
	 lhablock = 'CHARGEMIX', 
	 lhacode = [3, 2] ) 
 
ZP33 = 	 Parameter(name='ZP33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZP33}', 
	 lhablock = 'CHARGEMIX', 
	 lhacode = [3, 3] ) 
 
rUV11 = 	 Parameter(name='rUV11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1., 
	 texname = '\\text{UV11}', 
	 lhablock = 'UVMIX', 
	 lhacode = [1, 1] ) 
 
iUV11 = 	 Parameter(name='iUV11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1., 
	 texname = '\\text{UV11}', 
	 lhablock = 'IMUVMIX', 
	 lhacode = [1, 1] ) 
 
rUV12 = 	 Parameter(name='rUV12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0, 
	 texname = '\\text{UV12}', 
	 lhablock = 'UVMIX', 
	 lhacode = [1, 2] ) 
 
iUV12 = 	 Parameter(name='iUV12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0, 
	 texname = '\\text{UV12}', 
	 lhablock = 'IMUVMIX', 
	 lhacode = [1, 2] ) 
 
rUV13 = 	 Parameter(name='rUV13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0, 
	 texname = '\\text{UV13}', 
	 lhablock = 'UVMIX', 
	 lhacode = [1, 3] ) 
 
iUV13 = 	 Parameter(name='iUV13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0, 
	 texname = '\\text{UV13}', 
	 lhablock = 'IMUVMIX', 
	 lhacode = [1, 3] ) 
 
rUV21 = 	 Parameter(name='rUV21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0, 
	 texname = '\\text{UV21}', 
	 lhablock = 'UVMIX', 
	 lhacode = [2, 1] ) 
 
iUV21 = 	 Parameter(name='iUV21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0, 
	 texname = '\\text{UV21}', 
	 lhablock = 'IMUVMIX', 
	 lhacode = [2, 1] ) 
 
rUV22 = 	 Parameter(name='rUV22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1., 
	 texname = '\\text{UV22}', 
	 lhablock = 'UVMIX', 
	 lhacode = [2, 2] ) 
 
iUV22 = 	 Parameter(name='iUV22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1., 
	 texname = '\\text{UV22}', 
	 lhablock = 'IMUVMIX', 
	 lhacode = [2, 2] ) 
 
rUV23 = 	 Parameter(name='rUV23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0, 
	 texname = '\\text{UV23}', 
	 lhablock = 'UVMIX', 
	 lhacode = [2, 3] ) 
 
iUV23 = 	 Parameter(name='iUV23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0, 
	 texname = '\\text{UV23}', 
	 lhablock = 'IMUVMIX', 
	 lhacode = [2, 3] ) 
 
rUV31 = 	 Parameter(name='rUV31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0, 
	 texname = '\\text{UV31}', 
	 lhablock = 'UVMIX', 
	 lhacode = [3, 1] ) 
 
iUV31 = 	 Parameter(name='iUV31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0, 
	 texname = '\\text{UV31}', 
	 lhablock = 'IMUVMIX', 
	 lhacode = [3, 1] ) 
 
rUV32 = 	 Parameter(name='rUV32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0, 
	 texname = '\\text{UV32}', 
	 lhablock = 'UVMIX', 
	 lhacode = [3, 2] ) 
 
iUV32 = 	 Parameter(name='iUV32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0, 
	 texname = '\\text{UV32}', 
	 lhablock = 'IMUVMIX', 
	 lhacode = [3, 2] ) 
 
rUV33 = 	 Parameter(name='rUV33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1., 
	 texname = '\\text{UV33}', 
	 lhablock = 'UVMIX', 
	 lhacode = [3, 3] ) 
 
iUV33 = 	 Parameter(name='iUV33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1., 
	 texname = '\\text{UV33}', 
	 lhablock = 'IMUVMIX', 
	 lhacode = [3, 3] ) 
 
rZDL11 = 	 Parameter(name='rZDL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL11}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [1, 1] ) 
 
iZDL11 = 	 Parameter(name='iZDL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL11}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [1, 1] ) 
 
rZDL12 = 	 Parameter(name='rZDL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL12}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [1, 2] ) 
 
iZDL12 = 	 Parameter(name='iZDL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL12}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [1, 2] ) 
 
rZDL13 = 	 Parameter(name='rZDL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL13}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [1, 3] ) 
 
iZDL13 = 	 Parameter(name='iZDL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL13}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [1, 3] ) 
 
rZDL21 = 	 Parameter(name='rZDL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL21}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [2, 1] ) 
 
iZDL21 = 	 Parameter(name='iZDL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL21}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [2, 1] ) 
 
rZDL22 = 	 Parameter(name='rZDL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL22}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [2, 2] ) 
 
iZDL22 = 	 Parameter(name='iZDL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL22}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [2, 2] ) 
 
rZDL23 = 	 Parameter(name='rZDL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL23}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [2, 3] ) 
 
iZDL23 = 	 Parameter(name='iZDL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL23}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [2, 3] ) 
 
rZDL31 = 	 Parameter(name='rZDL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL31}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [3, 1] ) 
 
iZDL31 = 	 Parameter(name='iZDL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL31}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [3, 1] ) 
 
rZDL32 = 	 Parameter(name='rZDL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL32}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [3, 2] ) 
 
iZDL32 = 	 Parameter(name='iZDL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL32}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [3, 2] ) 
 
rZDL33 = 	 Parameter(name='rZDL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL33}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [3, 3] ) 
 
iZDL33 = 	 Parameter(name='iZDL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL33}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [3, 3] ) 
 
rZDR11 = 	 Parameter(name='rZDR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR11}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [1, 1] ) 
 
iZDR11 = 	 Parameter(name='iZDR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR11}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [1, 1] ) 
 
rZDR12 = 	 Parameter(name='rZDR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR12}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [1, 2] ) 
 
iZDR12 = 	 Parameter(name='iZDR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR12}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [1, 2] ) 
 
rZDR13 = 	 Parameter(name='rZDR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR13}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [1, 3] ) 
 
iZDR13 = 	 Parameter(name='iZDR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR13}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [1, 3] ) 
 
rZDR21 = 	 Parameter(name='rZDR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR21}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [2, 1] ) 
 
iZDR21 = 	 Parameter(name='iZDR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR21}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [2, 1] ) 
 
rZDR22 = 	 Parameter(name='rZDR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR22}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [2, 2] ) 
 
iZDR22 = 	 Parameter(name='iZDR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR22}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [2, 2] ) 
 
rZDR23 = 	 Parameter(name='rZDR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR23}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [2, 3] ) 
 
iZDR23 = 	 Parameter(name='iZDR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR23}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [2, 3] ) 
 
rZDR31 = 	 Parameter(name='rZDR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR31}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [3, 1] ) 
 
iZDR31 = 	 Parameter(name='iZDR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR31}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [3, 1] ) 
 
rZDR32 = 	 Parameter(name='rZDR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR32}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [3, 2] ) 
 
iZDR32 = 	 Parameter(name='iZDR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR32}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [3, 2] ) 
 
rZDR33 = 	 Parameter(name='rZDR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR33}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [3, 3] ) 
 
iZDR33 = 	 Parameter(name='iZDR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR33}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [3, 3] ) 
 
rZUL11 = 	 Parameter(name='rZUL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL11}', 
	 lhablock = 'UULMIX', 
	 lhacode = [1, 1] ) 
 
iZUL11 = 	 Parameter(name='iZUL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL11}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [1, 1] ) 
 
rZUL12 = 	 Parameter(name='rZUL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL12}', 
	 lhablock = 'UULMIX', 
	 lhacode = [1, 2] ) 
 
iZUL12 = 	 Parameter(name='iZUL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL12}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [1, 2] ) 
 
rZUL13 = 	 Parameter(name='rZUL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL13}', 
	 lhablock = 'UULMIX', 
	 lhacode = [1, 3] ) 
 
iZUL13 = 	 Parameter(name='iZUL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL13}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [1, 3] ) 
 
rZUL21 = 	 Parameter(name='rZUL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL21}', 
	 lhablock = 'UULMIX', 
	 lhacode = [2, 1] ) 
 
iZUL21 = 	 Parameter(name='iZUL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL21}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [2, 1] ) 
 
rZUL22 = 	 Parameter(name='rZUL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL22}', 
	 lhablock = 'UULMIX', 
	 lhacode = [2, 2] ) 
 
iZUL22 = 	 Parameter(name='iZUL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL22}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [2, 2] ) 
 
rZUL23 = 	 Parameter(name='rZUL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL23}', 
	 lhablock = 'UULMIX', 
	 lhacode = [2, 3] ) 
 
iZUL23 = 	 Parameter(name='iZUL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL23}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [2, 3] ) 
 
rZUL31 = 	 Parameter(name='rZUL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL31}', 
	 lhablock = 'UULMIX', 
	 lhacode = [3, 1] ) 
 
iZUL31 = 	 Parameter(name='iZUL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL31}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [3, 1] ) 
 
rZUL32 = 	 Parameter(name='rZUL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL32}', 
	 lhablock = 'UULMIX', 
	 lhacode = [3, 2] ) 
 
iZUL32 = 	 Parameter(name='iZUL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL32}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [3, 2] ) 
 
rZUL33 = 	 Parameter(name='rZUL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL33}', 
	 lhablock = 'UULMIX', 
	 lhacode = [3, 3] ) 
 
iZUL33 = 	 Parameter(name='iZUL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL33}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [3, 3] ) 
 
rZUR11 = 	 Parameter(name='rZUR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR11}', 
	 lhablock = 'UURMIX', 
	 lhacode = [1, 1] ) 
 
iZUR11 = 	 Parameter(name='iZUR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR11}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [1, 1] ) 
 
rZUR12 = 	 Parameter(name='rZUR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR12}', 
	 lhablock = 'UURMIX', 
	 lhacode = [1, 2] ) 
 
iZUR12 = 	 Parameter(name='iZUR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR12}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [1, 2] ) 
 
rZUR13 = 	 Parameter(name='rZUR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR13}', 
	 lhablock = 'UURMIX', 
	 lhacode = [1, 3] ) 
 
iZUR13 = 	 Parameter(name='iZUR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR13}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [1, 3] ) 
 
rZUR21 = 	 Parameter(name='rZUR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR21}', 
	 lhablock = 'UURMIX', 
	 lhacode = [2, 1] ) 
 
iZUR21 = 	 Parameter(name='iZUR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR21}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [2, 1] ) 
 
rZUR22 = 	 Parameter(name='rZUR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR22}', 
	 lhablock = 'UURMIX', 
	 lhacode = [2, 2] ) 
 
iZUR22 = 	 Parameter(name='iZUR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR22}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [2, 2] ) 
 
rZUR23 = 	 Parameter(name='rZUR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR23}', 
	 lhablock = 'UURMIX', 
	 lhacode = [2, 3] ) 
 
iZUR23 = 	 Parameter(name='iZUR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR23}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [2, 3] ) 
 
rZUR31 = 	 Parameter(name='rZUR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR31}', 
	 lhablock = 'UURMIX', 
	 lhacode = [3, 1] ) 
 
iZUR31 = 	 Parameter(name='iZUR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR31}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [3, 1] ) 
 
rZUR32 = 	 Parameter(name='rZUR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR32}', 
	 lhablock = 'UURMIX', 
	 lhacode = [3, 2] ) 
 
iZUR32 = 	 Parameter(name='iZUR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR32}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [3, 2] ) 
 
rZUR33 = 	 Parameter(name='rZUR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR33}', 
	 lhablock = 'UURMIX', 
	 lhacode = [3, 3] ) 
 
iZUR33 = 	 Parameter(name='iZUR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR33}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [3, 3] ) 
 
rZEL11 = 	 Parameter(name='rZEL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL11}', 
	 lhablock = 'UELMIX', 
	 lhacode = [1, 1] ) 
 
iZEL11 = 	 Parameter(name='iZEL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL11}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [1, 1] ) 
 
rZEL12 = 	 Parameter(name='rZEL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL12}', 
	 lhablock = 'UELMIX', 
	 lhacode = [1, 2] ) 
 
iZEL12 = 	 Parameter(name='iZEL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL12}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [1, 2] ) 
 
rZEL13 = 	 Parameter(name='rZEL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL13}', 
	 lhablock = 'UELMIX', 
	 lhacode = [1, 3] ) 
 
iZEL13 = 	 Parameter(name='iZEL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL13}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [1, 3] ) 
 
rZEL21 = 	 Parameter(name='rZEL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL21}', 
	 lhablock = 'UELMIX', 
	 lhacode = [2, 1] ) 
 
iZEL21 = 	 Parameter(name='iZEL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL21}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [2, 1] ) 
 
rZEL22 = 	 Parameter(name='rZEL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL22}', 
	 lhablock = 'UELMIX', 
	 lhacode = [2, 2] ) 
 
iZEL22 = 	 Parameter(name='iZEL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL22}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [2, 2] ) 
 
rZEL23 = 	 Parameter(name='rZEL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL23}', 
	 lhablock = 'UELMIX', 
	 lhacode = [2, 3] ) 
 
iZEL23 = 	 Parameter(name='iZEL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL23}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [2, 3] ) 
 
rZEL31 = 	 Parameter(name='rZEL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL31}', 
	 lhablock = 'UELMIX', 
	 lhacode = [3, 1] ) 
 
iZEL31 = 	 Parameter(name='iZEL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL31}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [3, 1] ) 
 
rZEL32 = 	 Parameter(name='rZEL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL32}', 
	 lhablock = 'UELMIX', 
	 lhacode = [3, 2] ) 
 
iZEL32 = 	 Parameter(name='iZEL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL32}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [3, 2] ) 
 
rZEL33 = 	 Parameter(name='rZEL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL33}', 
	 lhablock = 'UELMIX', 
	 lhacode = [3, 3] ) 
 
iZEL33 = 	 Parameter(name='iZEL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL33}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [3, 3] ) 
 
rZER11 = 	 Parameter(name='rZER11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER11}', 
	 lhablock = 'UERMIX', 
	 lhacode = [1, 1] ) 
 
iZER11 = 	 Parameter(name='iZER11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER11}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [1, 1] ) 
 
rZER12 = 	 Parameter(name='rZER12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER12}', 
	 lhablock = 'UERMIX', 
	 lhacode = [1, 2] ) 
 
iZER12 = 	 Parameter(name='iZER12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER12}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [1, 2] ) 
 
rZER13 = 	 Parameter(name='rZER13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER13}', 
	 lhablock = 'UERMIX', 
	 lhacode = [1, 3] ) 
 
iZER13 = 	 Parameter(name='iZER13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER13}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [1, 3] ) 
 
rZER21 = 	 Parameter(name='rZER21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER21}', 
	 lhablock = 'UERMIX', 
	 lhacode = [2, 1] ) 
 
iZER21 = 	 Parameter(name='iZER21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER21}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [2, 1] ) 
 
rZER22 = 	 Parameter(name='rZER22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER22}', 
	 lhablock = 'UERMIX', 
	 lhacode = [2, 2] ) 
 
iZER22 = 	 Parameter(name='iZER22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER22}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [2, 2] ) 
 
rZER23 = 	 Parameter(name='rZER23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER23}', 
	 lhablock = 'UERMIX', 
	 lhacode = [2, 3] ) 
 
iZER23 = 	 Parameter(name='iZER23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER23}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [2, 3] ) 
 
rZER31 = 	 Parameter(name='rZER31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER31}', 
	 lhablock = 'UERMIX', 
	 lhacode = [3, 1] ) 
 
iZER31 = 	 Parameter(name='iZER31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER31}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [3, 1] ) 
 
rZER32 = 	 Parameter(name='rZER32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER32}', 
	 lhablock = 'UERMIX', 
	 lhacode = [3, 2] ) 
 
iZER32 = 	 Parameter(name='iZER32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER32}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [3, 2] ) 
 
rZER33 = 	 Parameter(name='rZER33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER33}', 
	 lhablock = 'UERMIX', 
	 lhacode = [3, 3] ) 
 
iZER33 = 	 Parameter(name='iZER33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER33}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [3, 3] ) 
 
alphaH = 	 Parameter(name='alphaH', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{alphaH}', 
	 lhablock = 'HMIX', 
	 lhacode = [11] ) 
 
aS = 	 Parameter(name='aS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.119, 
	 texname = '\\text{aS}', 
	 lhablock = 'SMINPUTS', 
	 lhacode = [3] ) 
 
aEWM1 = 	 Parameter(name='aEWM1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 137.035999679, 
	 texname = '\\text{aEWM1}', 
	 lhablock = 'SMINPUTS', 
	 lhacode = [1] ) 
 
Gf = 	 Parameter(name='Gf', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.0000116639, 
	 texname = '\\text{Gf}', 
	 lhablock = 'SMINPUTS', 
	 lhacode = [2] ) 
 
epsU11 = 	 Parameter(name='epsU11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsU11 + complex(0,1)*iepsU11', 
	 texname = '\\text{epsU11}' ) 
 
epsU12 = 	 Parameter(name='epsU12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsU12 + complex(0,1)*iepsU12', 
	 texname = '\\text{epsU12}' ) 
 
epsU13 = 	 Parameter(name='epsU13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsU13 + complex(0,1)*iepsU13', 
	 texname = '\\text{epsU13}' ) 
 
epsU21 = 	 Parameter(name='epsU21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsU21 + complex(0,1)*iepsU21', 
	 texname = '\\text{epsU21}' ) 
 
epsU22 = 	 Parameter(name='epsU22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsU22 + complex(0,1)*iepsU22', 
	 texname = '\\text{epsU22}' ) 
 
epsU23 = 	 Parameter(name='epsU23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsU23 + complex(0,1)*iepsU23', 
	 texname = '\\text{epsU23}' ) 
 
epsU31 = 	 Parameter(name='epsU31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsU31 + complex(0,1)*iepsU31', 
	 texname = '\\text{epsU31}' ) 
 
epsU32 = 	 Parameter(name='epsU32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsU32 + complex(0,1)*iepsU32', 
	 texname = '\\text{epsU32}' ) 
 
epsU33 = 	 Parameter(name='epsU33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsU33 + complex(0,1)*iepsU33', 
	 texname = '\\text{epsU33}' ) 
 
epsD11 = 	 Parameter(name='epsD11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsD11 + complex(0,1)*iepsD11', 
	 texname = '\\text{epsD11}' ) 
 
epsD12 = 	 Parameter(name='epsD12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsD12 + complex(0,1)*iepsD12', 
	 texname = '\\text{epsD12}' ) 
 
epsD13 = 	 Parameter(name='epsD13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsD13 + complex(0,1)*iepsD13', 
	 texname = '\\text{epsD13}' ) 
 
epsD21 = 	 Parameter(name='epsD21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsD21 + complex(0,1)*iepsD21', 
	 texname = '\\text{epsD21}' ) 
 
epsD22 = 	 Parameter(name='epsD22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsD22 + complex(0,1)*iepsD22', 
	 texname = '\\text{epsD22}' ) 
 
epsD23 = 	 Parameter(name='epsD23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsD23 + complex(0,1)*iepsD23', 
	 texname = '\\text{epsD23}' ) 
 
epsD31 = 	 Parameter(name='epsD31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsD31 + complex(0,1)*iepsD31', 
	 texname = '\\text{epsD31}' ) 
 
epsD32 = 	 Parameter(name='epsD32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsD32 + complex(0,1)*iepsD32', 
	 texname = '\\text{epsD32}' ) 
 
epsD33 = 	 Parameter(name='epsD33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsD33 + complex(0,1)*iepsD33', 
	 texname = '\\text{epsD33}' ) 
 
epsE11 = 	 Parameter(name='epsE11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsE11 + complex(0,1)*iepsE11', 
	 texname = '\\text{epsE11}' ) 
 
epsE12 = 	 Parameter(name='epsE12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsE12 + complex(0,1)*iepsE12', 
	 texname = '\\text{epsE12}' ) 
 
epsE13 = 	 Parameter(name='epsE13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsE13 + complex(0,1)*iepsE13', 
	 texname = '\\text{epsE13}' ) 
 
epsE21 = 	 Parameter(name='epsE21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsE21 + complex(0,1)*iepsE21', 
	 texname = '\\text{epsE21}' ) 
 
epsE22 = 	 Parameter(name='epsE22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsE22 + complex(0,1)*iepsE22', 
	 texname = '\\text{epsE22}' ) 
 
epsE23 = 	 Parameter(name='epsE23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsE23 + complex(0,1)*iepsE23', 
	 texname = '\\text{epsE23}' ) 
 
epsE31 = 	 Parameter(name='epsE31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsE31 + complex(0,1)*iepsE31', 
	 texname = '\\text{epsE31}' ) 
 
epsE32 = 	 Parameter(name='epsE32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsE32 + complex(0,1)*iepsE32', 
	 texname = '\\text{epsE32}' ) 
 
epsE33 = 	 Parameter(name='epsE33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'repsE33 + complex(0,1)*iepsE33', 
	 texname = '\\text{epsE33}' ) 
 
Yh11 = 	 Parameter(name='Yh11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYh11 + complex(0,1)*iYh11', 
	 texname = '\\text{Yh11}' ) 
 
Yh12 = 	 Parameter(name='Yh12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYh12 + complex(0,1)*iYh12', 
	 texname = '\\text{Yh12}' ) 
 
Yh13 = 	 Parameter(name='Yh13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYh13 + complex(0,1)*iYh13', 
	 texname = '\\text{Yh13}' ) 
 
Yh21 = 	 Parameter(name='Yh21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYh21 + complex(0,1)*iYh21', 
	 texname = '\\text{Yh21}' ) 
 
Yh22 = 	 Parameter(name='Yh22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYh22 + complex(0,1)*iYh22', 
	 texname = '\\text{Yh22}' ) 
 
Yh23 = 	 Parameter(name='Yh23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYh23 + complex(0,1)*iYh23', 
	 texname = '\\text{Yh23}' ) 
 
Yh31 = 	 Parameter(name='Yh31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYh31 + complex(0,1)*iYh31', 
	 texname = '\\text{Yh31}' ) 
 
Yh32 = 	 Parameter(name='Yh32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYh32 + complex(0,1)*iYh32', 
	 texname = '\\text{Yh32}' ) 
 
Yh33 = 	 Parameter(name='Yh33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYh33 + complex(0,1)*iYh33', 
	 texname = '\\text{Yh33}' ) 
 
lam1 = 	 Parameter(name='lam1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rlam1 + complex(0,1)*ilam1', 
	 texname = '\\text{lam1}' ) 
 
lam2 = 	 Parameter(name='lam2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rlam2 + complex(0,1)*ilam2', 
	 texname = '\\text{lam2}' ) 
 
lam4 = 	 Parameter(name='lam4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rlam4 + complex(0,1)*ilam4', 
	 texname = '\\text{lam4}' ) 
 
lam3 = 	 Parameter(name='lam3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rlam3 + complex(0,1)*ilam3', 
	 texname = '\\text{lam3}' ) 
 
lam7 = 	 Parameter(name='lam7', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rlam7 + complex(0,1)*ilam7', 
	 texname = '\\text{lam7}' ) 
 
lam6 = 	 Parameter(name='lam6', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rlam6 + complex(0,1)*ilam6', 
	 texname = '\\text{lam6}' ) 
 
lam9 = 	 Parameter(name='lam9', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rlam9 + complex(0,1)*ilam9', 
	 texname = '\\text{lam9}' ) 
 
lam8 = 	 Parameter(name='lam8', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rlam8 + complex(0,1)*ilam8', 
	 texname = '\\text{lam8}' ) 
 
lamh = 	 Parameter(name='lamh', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rlamh + complex(0,1)*ilamh', 
	 texname = '\\text{lamh}' ) 
 
mu = 	 Parameter(name='mu', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rmu + complex(0,1)*imu', 
	 texname = '\\text{mu}' ) 
 
lam10 = 	 Parameter(name='lam10', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rlam10 + complex(0,1)*ilam10', 
	 texname = '\\text{lam10}' ) 
 
UV11 = 	 Parameter(name='UV11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV11 + complex(0,1)*iUV11', 
	 texname = '\\text{UV11}' ) 
 
UV12 = 	 Parameter(name='UV12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV12 + complex(0,1)*iUV12', 
	 texname = '\\text{UV12}' ) 
 
UV13 = 	 Parameter(name='UV13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV13 + complex(0,1)*iUV13', 
	 texname = '\\text{UV13}' ) 
 
UV21 = 	 Parameter(name='UV21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV21 + complex(0,1)*iUV21', 
	 texname = '\\text{UV21}' ) 
 
UV22 = 	 Parameter(name='UV22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV22 + complex(0,1)*iUV22', 
	 texname = '\\text{UV22}' ) 
 
UV23 = 	 Parameter(name='UV23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV23 + complex(0,1)*iUV23', 
	 texname = '\\text{UV23}' ) 
 
UV31 = 	 Parameter(name='UV31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV31 + complex(0,1)*iUV31', 
	 texname = '\\text{UV31}' ) 
 
UV32 = 	 Parameter(name='UV32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV32 + complex(0,1)*iUV32', 
	 texname = '\\text{UV32}' ) 
 
UV33 = 	 Parameter(name='UV33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV33 + complex(0,1)*iUV33', 
	 texname = '\\text{UV33}' ) 
 
ZDL11 = 	 Parameter(name='ZDL11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL11 + complex(0,1)*iZDL11', 
	 texname = '\\text{ZDL11}' ) 
 
ZDL12 = 	 Parameter(name='ZDL12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL12 + complex(0,1)*iZDL12', 
	 texname = '\\text{ZDL12}' ) 
 
ZDL13 = 	 Parameter(name='ZDL13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL13 + complex(0,1)*iZDL13', 
	 texname = '\\text{ZDL13}' ) 
 
ZDL21 = 	 Parameter(name='ZDL21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL21 + complex(0,1)*iZDL21', 
	 texname = '\\text{ZDL21}' ) 
 
ZDL22 = 	 Parameter(name='ZDL22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL22 + complex(0,1)*iZDL22', 
	 texname = '\\text{ZDL22}' ) 
 
ZDL23 = 	 Parameter(name='ZDL23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL23 + complex(0,1)*iZDL23', 
	 texname = '\\text{ZDL23}' ) 
 
ZDL31 = 	 Parameter(name='ZDL31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL31 + complex(0,1)*iZDL31', 
	 texname = '\\text{ZDL31}' ) 
 
ZDL32 = 	 Parameter(name='ZDL32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL32 + complex(0,1)*iZDL32', 
	 texname = '\\text{ZDL32}' ) 
 
ZDL33 = 	 Parameter(name='ZDL33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL33 + complex(0,1)*iZDL33', 
	 texname = '\\text{ZDL33}' ) 
 
ZDR11 = 	 Parameter(name='ZDR11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR11 + complex(0,1)*iZDR11', 
	 texname = '\\text{ZDR11}' ) 
 
ZDR12 = 	 Parameter(name='ZDR12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR12 + complex(0,1)*iZDR12', 
	 texname = '\\text{ZDR12}' ) 
 
ZDR13 = 	 Parameter(name='ZDR13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR13 + complex(0,1)*iZDR13', 
	 texname = '\\text{ZDR13}' ) 
 
ZDR21 = 	 Parameter(name='ZDR21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR21 + complex(0,1)*iZDR21', 
	 texname = '\\text{ZDR21}' ) 
 
ZDR22 = 	 Parameter(name='ZDR22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR22 + complex(0,1)*iZDR22', 
	 texname = '\\text{ZDR22}' ) 
 
ZDR23 = 	 Parameter(name='ZDR23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR23 + complex(0,1)*iZDR23', 
	 texname = '\\text{ZDR23}' ) 
 
ZDR31 = 	 Parameter(name='ZDR31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR31 + complex(0,1)*iZDR31', 
	 texname = '\\text{ZDR31}' ) 
 
ZDR32 = 	 Parameter(name='ZDR32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR32 + complex(0,1)*iZDR32', 
	 texname = '\\text{ZDR32}' ) 
 
ZDR33 = 	 Parameter(name='ZDR33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR33 + complex(0,1)*iZDR33', 
	 texname = '\\text{ZDR33}' ) 
 
ZUL11 = 	 Parameter(name='ZUL11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL11 + complex(0,1)*iZUL11', 
	 texname = '\\text{ZUL11}' ) 
 
ZUL12 = 	 Parameter(name='ZUL12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL12 + complex(0,1)*iZUL12', 
	 texname = '\\text{ZUL12}' ) 
 
ZUL13 = 	 Parameter(name='ZUL13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL13 + complex(0,1)*iZUL13', 
	 texname = '\\text{ZUL13}' ) 
 
ZUL21 = 	 Parameter(name='ZUL21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL21 + complex(0,1)*iZUL21', 
	 texname = '\\text{ZUL21}' ) 
 
ZUL22 = 	 Parameter(name='ZUL22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL22 + complex(0,1)*iZUL22', 
	 texname = '\\text{ZUL22}' ) 
 
ZUL23 = 	 Parameter(name='ZUL23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL23 + complex(0,1)*iZUL23', 
	 texname = '\\text{ZUL23}' ) 
 
ZUL31 = 	 Parameter(name='ZUL31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL31 + complex(0,1)*iZUL31', 
	 texname = '\\text{ZUL31}' ) 
 
ZUL32 = 	 Parameter(name='ZUL32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL32 + complex(0,1)*iZUL32', 
	 texname = '\\text{ZUL32}' ) 
 
ZUL33 = 	 Parameter(name='ZUL33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL33 + complex(0,1)*iZUL33', 
	 texname = '\\text{ZUL33}' ) 
 
ZUR11 = 	 Parameter(name='ZUR11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR11 + complex(0,1)*iZUR11', 
	 texname = '\\text{ZUR11}' ) 
 
ZUR12 = 	 Parameter(name='ZUR12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR12 + complex(0,1)*iZUR12', 
	 texname = '\\text{ZUR12}' ) 
 
ZUR13 = 	 Parameter(name='ZUR13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR13 + complex(0,1)*iZUR13', 
	 texname = '\\text{ZUR13}' ) 
 
ZUR21 = 	 Parameter(name='ZUR21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR21 + complex(0,1)*iZUR21', 
	 texname = '\\text{ZUR21}' ) 
 
ZUR22 = 	 Parameter(name='ZUR22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR22 + complex(0,1)*iZUR22', 
	 texname = '\\text{ZUR22}' ) 
 
ZUR23 = 	 Parameter(name='ZUR23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR23 + complex(0,1)*iZUR23', 
	 texname = '\\text{ZUR23}' ) 
 
ZUR31 = 	 Parameter(name='ZUR31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR31 + complex(0,1)*iZUR31', 
	 texname = '\\text{ZUR31}' ) 
 
ZUR32 = 	 Parameter(name='ZUR32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR32 + complex(0,1)*iZUR32', 
	 texname = '\\text{ZUR32}' ) 
 
ZUR33 = 	 Parameter(name='ZUR33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR33 + complex(0,1)*iZUR33', 
	 texname = '\\text{ZUR33}' ) 
 
ZEL11 = 	 Parameter(name='ZEL11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL11 + complex(0,1)*iZEL11', 
	 texname = '\\text{ZEL11}' ) 
 
ZEL12 = 	 Parameter(name='ZEL12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL12 + complex(0,1)*iZEL12', 
	 texname = '\\text{ZEL12}' ) 
 
ZEL13 = 	 Parameter(name='ZEL13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL13 + complex(0,1)*iZEL13', 
	 texname = '\\text{ZEL13}' ) 
 
ZEL21 = 	 Parameter(name='ZEL21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL21 + complex(0,1)*iZEL21', 
	 texname = '\\text{ZEL21}' ) 
 
ZEL22 = 	 Parameter(name='ZEL22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL22 + complex(0,1)*iZEL22', 
	 texname = '\\text{ZEL22}' ) 
 
ZEL23 = 	 Parameter(name='ZEL23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL23 + complex(0,1)*iZEL23', 
	 texname = '\\text{ZEL23}' ) 
 
ZEL31 = 	 Parameter(name='ZEL31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL31 + complex(0,1)*iZEL31', 
	 texname = '\\text{ZEL31}' ) 
 
ZEL32 = 	 Parameter(name='ZEL32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL32 + complex(0,1)*iZEL32', 
	 texname = '\\text{ZEL32}' ) 
 
ZEL33 = 	 Parameter(name='ZEL33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL33 + complex(0,1)*iZEL33', 
	 texname = '\\text{ZEL33}' ) 
 
ZER11 = 	 Parameter(name='ZER11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER11 + complex(0,1)*iZER11', 
	 texname = '\\text{ZER11}' ) 
 
ZER12 = 	 Parameter(name='ZER12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER12 + complex(0,1)*iZER12', 
	 texname = '\\text{ZER12}' ) 
 
ZER13 = 	 Parameter(name='ZER13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER13 + complex(0,1)*iZER13', 
	 texname = '\\text{ZER13}' ) 
 
ZER21 = 	 Parameter(name='ZER21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER21 + complex(0,1)*iZER21', 
	 texname = '\\text{ZER21}' ) 
 
ZER22 = 	 Parameter(name='ZER22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER22 + complex(0,1)*iZER22', 
	 texname = '\\text{ZER22}' ) 
 
ZER23 = 	 Parameter(name='ZER23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER23 + complex(0,1)*iZER23', 
	 texname = '\\text{ZER23}' ) 
 
ZER31 = 	 Parameter(name='ZER31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER31 + complex(0,1)*iZER31', 
	 texname = '\\text{ZER31}' ) 
 
ZER32 = 	 Parameter(name='ZER32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER32 + complex(0,1)*iZER32', 
	 texname = '\\text{ZER32}' ) 
 
ZER33 = 	 Parameter(name='ZER33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER33 + complex(0,1)*iZER33', 
	 texname = '\\text{ZER33}' ) 
 
G = 	 Parameter(name='G', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)', 
	 texname = 'G') 
 
vv = 	 Parameter(name='vv', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '1.*(0)', 
	 texname = 'vv') 
 
ZH11 = 	 Parameter(name='ZH11', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '-cmath.sin(alphaH)', 
	 texname = 'ZH11') 
 
ZH12 = 	 Parameter(name='ZH12', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'cmath.cos(alphaH)', 
	 texname = 'ZH12') 
 
ZH21 = 	 Parameter(name='ZH21', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'cmath.cos(alphaH)', 
	 texname = 'ZH21') 
 
ZH22 = 	 Parameter(name='ZH22', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'cmath.sin(alphaH)', 
	 texname = 'ZH22') 
 
el = 	 Parameter(name='el', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)', 
	 texname = 'el') 
 
MWp = 	 Parameter(name='MWp', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (MZ**2*cmath.pi)/(cmath.sqrt(2)*aEWM1*Gf)))', 
	 texname = 'MWp') 
 
TW = 	 Parameter(name='TW', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'cmath.asin(cmath.sqrt(1 - MWp**2/MZ**2))', 
	 texname = 'TW') 
 
g1 = 	 Parameter(name='g1', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'el*1./cmath.cos(TW)', 
	 texname = 'g1') 
 
g2 = 	 Parameter(name='g2', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'el*1./cmath.sin(TW)', 
	 texname = 'g2') 
 
v = 	 Parameter(name='v', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '2*cmath.sqrt(MWp**2/g2**2)', 
	 texname = 'v') 
 
Yu11 = 	 Parameter(name='Yu11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '(cmath.sqrt(2)*Mu1)/v', 
	 texname = 'Yu11') 
 
Yu12 = 	 Parameter(name='Yu12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Yu12') 
 
Yu13 = 	 Parameter(name='Yu13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Yu13') 
 
Yu21 = 	 Parameter(name='Yu21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Yu21') 
 
Yu22 = 	 Parameter(name='Yu22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '(cmath.sqrt(2)*Mu2)/v', 
	 texname = 'Yu22') 
 
Yu23 = 	 Parameter(name='Yu23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Yu23') 
 
Yu31 = 	 Parameter(name='Yu31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Yu31') 
 
Yu32 = 	 Parameter(name='Yu32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Yu32') 
 
Yu33 = 	 Parameter(name='Yu33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '(cmath.sqrt(2)*Mu3)/v', 
	 texname = 'Yu33') 
 
Yd11 = 	 Parameter(name='Yd11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '(cmath.sqrt(2)*Md1)/v', 
	 texname = 'Yd11') 
 
Yd12 = 	 Parameter(name='Yd12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Yd12') 
 
Yd13 = 	 Parameter(name='Yd13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Yd13') 
 
Yd21 = 	 Parameter(name='Yd21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Yd21') 
 
Yd22 = 	 Parameter(name='Yd22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '(cmath.sqrt(2)*Md2)/v', 
	 texname = 'Yd22') 
 
Yd23 = 	 Parameter(name='Yd23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Yd23') 
 
Yd31 = 	 Parameter(name='Yd31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Yd31') 
 
Yd32 = 	 Parameter(name='Yd32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Yd32') 
 
Yd33 = 	 Parameter(name='Yd33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '(cmath.sqrt(2)*Md3)/v', 
	 texname = 'Yd33') 
 
Ye11 = 	 Parameter(name='Ye11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '(cmath.sqrt(2)*Me1)/v', 
	 texname = 'Ye11') 
 
Ye12 = 	 Parameter(name='Ye12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Ye12') 
 
Ye13 = 	 Parameter(name='Ye13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Ye13') 
 
Ye21 = 	 Parameter(name='Ye21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Ye21') 
 
Ye22 = 	 Parameter(name='Ye22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '(cmath.sqrt(2)*Me2)/v', 
	 texname = 'Ye22') 
 
Ye23 = 	 Parameter(name='Ye23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Ye23') 
 
Ye31 = 	 Parameter(name='Ye31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Ye31') 
 
Ye32 = 	 Parameter(name='Ye32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '1.*(0)', 
	 texname = 'Ye32') 
 
Ye33 = 	 Parameter(name='Ye33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = '(cmath.sqrt(2)*Me3)/v', 
	 texname = 'Ye33') 
 
RXiWp = 	 Parameter(name='RXiWp', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '1.', 
	 texname = 'RXiWp') 
 
RXiZ = 	 Parameter(name='RXiZ', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '1.', 
	 texname = 'RXiZ') 
 
HPP1 = 	 Parameter(name='HPP1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HPP1}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [25,22,22] ) 
 
HGG1 = 	 Parameter(name='HGG1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HGG1}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [25,21,21] ) 
 
HPP2 = 	 Parameter(name='HPP2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HPP2}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [35,22,22] ) 
 
HGG2 = 	 Parameter(name='HGG2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HGG2}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [35,21,21] ) 
 
