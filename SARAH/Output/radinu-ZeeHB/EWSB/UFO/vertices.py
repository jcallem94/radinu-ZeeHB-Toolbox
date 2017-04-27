# ------------------------------------------------------------------------------  
# This model file was automatically created by SARAH version4.9.1 
# SARAH References: arXiv:0806.0538, 0909.2863, 1002.0840, 1207.0906, 1309.7223   
# (c) Florian Staub, 2013  
# -------------------------------------------------------------------------------  
# File created at 16:00 on 18.1.2017   
# ----------------------------------------------------------------------  
 
 
from object_library import all_vertices,Vertex 
import particles as P 
import couplings as C 
import lorentz as L 
 
 
V_1 = Vertex(name = 'V_1', 
	 particles = [P.Ah, P.Ah, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_1}) 
 
 
V_2 = Vertex(name = 'V_2', 
	 particles = [P.Ah, P.Ah, P.etI], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_2}) 
 
 
V_3 = Vertex(name = 'V_3', 
	 particles = [P.Ah, P.Ah, P.h1], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_3}) 
 
 
V_4 = Vertex(name = 'V_4', 
	 particles = [P.Ah, P.Ah, P.h2], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_4}) 
 
 
V_5 = Vertex(name = 'V_5', 
	 particles = [P.Ah, P.etI, P.etI], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_5}) 
 
 
V_6 = Vertex(name = 'V_6', 
	 particles = [P.Ah, P.etI, P.h1], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_6}) 
 
 
V_7 = Vertex(name = 'V_7', 
	 particles = [P.Ah, P.etI, P.h2], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_7}) 
 
 
V_8 = Vertex(name = 'V_8', 
	 particles = [P.Ah, P.h1, P.h1], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_8}) 
 
 
V_9 = Vertex(name = 'V_9', 
	 particles = [P.Ah, P.h1, P.h2], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_9}) 
 
 
V_10 = Vertex(name = 'V_10', 
	 particles = [P.Ah, P.h2, P.h2], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_10}) 
 
 
V_11 = Vertex(name = 'V_11', 
	 particles = [P.Ah, P.Hp1, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_11}) 
 
 
V_12 = Vertex(name = 'V_12', 
	 particles = [P.Ah, P.Hp1, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_12}) 
 
 
V_13 = Vertex(name = 'V_13', 
	 particles = [P.Ah, P.Hp1, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_13}) 
 
 
V_14 = Vertex(name = 'V_14', 
	 particles = [P.Ah, P.Hp2, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_14}) 
 
 
V_15 = Vertex(name = 'V_15', 
	 particles = [P.Ah, P.Hp2, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_15}) 
 
 
V_16 = Vertex(name = 'V_16', 
	 particles = [P.Ah, P.Hp2, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_16}) 
 
 
V_17 = Vertex(name = 'V_17', 
	 particles = [P.Ah, P.Hp3, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_17}) 
 
 
V_18 = Vertex(name = 'V_18', 
	 particles = [P.Ah, P.Hp3, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_18}) 
 
 
V_19 = Vertex(name = 'V_19', 
	 particles = [P.Ah, P.Hp3, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_19}) 
 
 
V_20 = Vertex(name = 'V_20', 
	 particles = [P.etI, P.etI, P.etI], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_20}) 
 
 
V_21 = Vertex(name = 'V_21', 
	 particles = [P.etI, P.etI, P.h1], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_21}) 
 
 
V_22 = Vertex(name = 'V_22', 
	 particles = [P.etI, P.etI, P.h2], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_22}) 
 
 
V_23 = Vertex(name = 'V_23', 
	 particles = [P.etI, P.h1, P.h1], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_23}) 
 
 
V_24 = Vertex(name = 'V_24', 
	 particles = [P.etI, P.h1, P.h2], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_24}) 
 
 
V_25 = Vertex(name = 'V_25', 
	 particles = [P.etI, P.h2, P.h2], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_25}) 
 
 
V_26 = Vertex(name = 'V_26', 
	 particles = [P.etI, P.Hp1, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_26}) 
 
 
V_27 = Vertex(name = 'V_27', 
	 particles = [P.etI, P.Hp1, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_27}) 
 
 
V_28 = Vertex(name = 'V_28', 
	 particles = [P.etI, P.Hp1, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_28}) 
 
 
V_29 = Vertex(name = 'V_29', 
	 particles = [P.etI, P.Hp2, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_29}) 
 
 
V_30 = Vertex(name = 'V_30', 
	 particles = [P.etI, P.Hp2, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_30}) 
 
 
V_31 = Vertex(name = 'V_31', 
	 particles = [P.etI, P.Hp2, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_31}) 
 
 
V_32 = Vertex(name = 'V_32', 
	 particles = [P.etI, P.Hp3, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_32}) 
 
 
V_33 = Vertex(name = 'V_33', 
	 particles = [P.etI, P.Hp3, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_33}) 
 
 
V_34 = Vertex(name = 'V_34', 
	 particles = [P.etI, P.Hp3, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_34}) 
 
 
V_35 = Vertex(name = 'V_35', 
	 particles = [P.h1, P.h1, P.h1], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_35}) 
 
 
V_36 = Vertex(name = 'V_36', 
	 particles = [P.h1, P.h1, P.h2], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_36}) 
 
 
V_37 = Vertex(name = 'V_37', 
	 particles = [P.h1, P.h2, P.h2], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_37}) 
 
 
V_38 = Vertex(name = 'V_38', 
	 particles = [P.h2, P.h2, P.h2], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_38}) 
 
 
V_39 = Vertex(name = 'V_39', 
	 particles = [P.h1, P.Hp1, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_39}) 
 
 
V_40 = Vertex(name = 'V_40', 
	 particles = [P.h1, P.Hp1, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_40}) 
 
 
V_41 = Vertex(name = 'V_41', 
	 particles = [P.h1, P.Hp1, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_41}) 
 
 
V_42 = Vertex(name = 'V_42', 
	 particles = [P.h1, P.Hp2, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_42}) 
 
 
V_43 = Vertex(name = 'V_43', 
	 particles = [P.h1, P.Hp2, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_43}) 
 
 
V_44 = Vertex(name = 'V_44', 
	 particles = [P.h1, P.Hp2, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_44}) 
 
 
V_45 = Vertex(name = 'V_45', 
	 particles = [P.h1, P.Hp3, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_45}) 
 
 
V_46 = Vertex(name = 'V_46', 
	 particles = [P.h1, P.Hp3, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_46}) 
 
 
V_47 = Vertex(name = 'V_47', 
	 particles = [P.h1, P.Hp3, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_47}) 
 
 
V_48 = Vertex(name = 'V_48', 
	 particles = [P.h2, P.Hp1, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_48}) 
 
 
V_49 = Vertex(name = 'V_49', 
	 particles = [P.h2, P.Hp1, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_49}) 
 
 
V_50 = Vertex(name = 'V_50', 
	 particles = [P.h2, P.Hp1, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_50}) 
 
 
V_51 = Vertex(name = 'V_51', 
	 particles = [P.h2, P.Hp2, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_51}) 
 
 
V_52 = Vertex(name = 'V_52', 
	 particles = [P.h2, P.Hp2, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_52}) 
 
 
V_53 = Vertex(name = 'V_53', 
	 particles = [P.h2, P.Hp2, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_53}) 
 
 
V_54 = Vertex(name = 'V_54', 
	 particles = [P.h2, P.Hp3, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_54}) 
 
 
V_55 = Vertex(name = 'V_55', 
	 particles = [P.h2, P.Hp3, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_55}) 
 
 
V_56 = Vertex(name = 'V_56', 
	 particles = [P.h2, P.Hp3, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_56}) 
 
 
V_57 = Vertex(name = 'V_57', 
	 particles = [P.Ah, P.Ah, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_57}) 
 
 
V_58 = Vertex(name = 'V_58', 
	 particles = [P.Ah, P.Ah, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_58}) 
 
 
V_59 = Vertex(name = 'V_59', 
	 particles = [P.Ah, P.Hp1, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_59}) 
 
 
V_60 = Vertex(name = 'V_60', 
	 particles = [P.Ah, P.Hp2, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_60}) 
 
 
V_61 = Vertex(name = 'V_61', 
	 particles = [P.Ah, P.Hp3, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_61}) 
 
 
V_62 = Vertex(name = 'V_62', 
	 particles = [P.Ah, P.Hp1, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_62}) 
 
 
V_63 = Vertex(name = 'V_63', 
	 particles = [P.Ah, P.Hp2, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_63}) 
 
 
V_64 = Vertex(name = 'V_64', 
	 particles = [P.Ah, P.Hp3, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_64}) 
 
 
V_65 = Vertex(name = 'V_65', 
	 particles = [P.Ah, P.Hp1c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_65}) 
 
 
V_66 = Vertex(name = 'V_66', 
	 particles = [P.Ah, P.Hp2c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_66}) 
 
 
V_67 = Vertex(name = 'V_67', 
	 particles = [P.Ah, P.Hp3c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_67}) 
 
 
V_68 = Vertex(name = 'V_68', 
	 particles = [P.Ah, P.Hp1c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_68}) 
 
 
V_69 = Vertex(name = 'V_69', 
	 particles = [P.Ah, P.Hp2c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_69}) 
 
 
V_70 = Vertex(name = 'V_70', 
	 particles = [P.Ah, P.Hp3c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_70}) 
 
 
V_71 = Vertex(name = 'V_71', 
	 particles = [P.etI, P.etI, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_71}) 
 
 
V_72 = Vertex(name = 'V_72', 
	 particles = [P.etI, P.etI, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_72}) 
 
 
V_73 = Vertex(name = 'V_73', 
	 particles = [P.etI, P.Hp1, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_73}) 
 
 
V_74 = Vertex(name = 'V_74', 
	 particles = [P.etI, P.Hp2, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_74}) 
 
 
V_75 = Vertex(name = 'V_75', 
	 particles = [P.etI, P.Hp3, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_75}) 
 
 
V_76 = Vertex(name = 'V_76', 
	 particles = [P.etI, P.Hp1, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_76}) 
 
 
V_77 = Vertex(name = 'V_77', 
	 particles = [P.etI, P.Hp2, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_77}) 
 
 
V_78 = Vertex(name = 'V_78', 
	 particles = [P.etI, P.Hp3, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_78}) 
 
 
V_79 = Vertex(name = 'V_79', 
	 particles = [P.etI, P.Hp1c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_79}) 
 
 
V_80 = Vertex(name = 'V_80', 
	 particles = [P.etI, P.Hp2c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_80}) 
 
 
V_81 = Vertex(name = 'V_81', 
	 particles = [P.etI, P.Hp3c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_81}) 
 
 
V_82 = Vertex(name = 'V_82', 
	 particles = [P.etI, P.Hp1c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_82}) 
 
 
V_83 = Vertex(name = 'V_83', 
	 particles = [P.etI, P.Hp2c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_83}) 
 
 
V_84 = Vertex(name = 'V_84', 
	 particles = [P.etI, P.Hp3c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_84}) 
 
 
V_85 = Vertex(name = 'V_85', 
	 particles = [P.h1, P.h1, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_85}) 
 
 
V_86 = Vertex(name = 'V_86', 
	 particles = [P.h1, P.h2, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_86}) 
 
 
V_87 = Vertex(name = 'V_87', 
	 particles = [P.h2, P.h2, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_87}) 
 
 
V_88 = Vertex(name = 'V_88', 
	 particles = [P.h1, P.h1, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_88}) 
 
 
V_89 = Vertex(name = 'V_89', 
	 particles = [P.h1, P.h2, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_89}) 
 
 
V_90 = Vertex(name = 'V_90', 
	 particles = [P.h2, P.h2, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_90}) 
 
 
V_91 = Vertex(name = 'V_91', 
	 particles = [P.h1, P.Hp1, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_91}) 
 
 
V_92 = Vertex(name = 'V_92', 
	 particles = [P.h1, P.Hp2, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_92}) 
 
 
V_93 = Vertex(name = 'V_93', 
	 particles = [P.h1, P.Hp3, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_93}) 
 
 
V_94 = Vertex(name = 'V_94', 
	 particles = [P.h2, P.Hp1, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_94}) 
 
 
V_95 = Vertex(name = 'V_95', 
	 particles = [P.h2, P.Hp2, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_95}) 
 
 
V_96 = Vertex(name = 'V_96', 
	 particles = [P.h2, P.Hp3, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_96}) 
 
 
V_97 = Vertex(name = 'V_97', 
	 particles = [P.h1, P.Hp1, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_97}) 
 
 
V_98 = Vertex(name = 'V_98', 
	 particles = [P.h1, P.Hp2, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_98}) 
 
 
V_99 = Vertex(name = 'V_99', 
	 particles = [P.h1, P.Hp3, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_99}) 
 
 
V_100 = Vertex(name = 'V_100', 
	 particles = [P.h2, P.Hp1, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_100}) 
 
 
V_101 = Vertex(name = 'V_101', 
	 particles = [P.h2, P.Hp2, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_101}) 
 
 
V_102 = Vertex(name = 'V_102', 
	 particles = [P.h2, P.Hp3, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_102}) 
 
 
V_103 = Vertex(name = 'V_103', 
	 particles = [P.h1, P.Hp1c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_103}) 
 
 
V_104 = Vertex(name = 'V_104', 
	 particles = [P.h1, P.Hp2c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_104}) 
 
 
V_105 = Vertex(name = 'V_105', 
	 particles = [P.h1, P.Hp3c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_105}) 
 
 
V_106 = Vertex(name = 'V_106', 
	 particles = [P.h2, P.Hp1c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_106}) 
 
 
V_107 = Vertex(name = 'V_107', 
	 particles = [P.h2, P.Hp2c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_107}) 
 
 
V_108 = Vertex(name = 'V_108', 
	 particles = [P.h2, P.Hp3c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_108}) 
 
 
V_109 = Vertex(name = 'V_109', 
	 particles = [P.h1, P.Hp1c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_109}) 
 
 
V_110 = Vertex(name = 'V_110', 
	 particles = [P.h1, P.Hp2c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_110}) 
 
 
V_111 = Vertex(name = 'V_111', 
	 particles = [P.h1, P.Hp3c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_111}) 
 
 
V_112 = Vertex(name = 'V_112', 
	 particles = [P.h2, P.Hp1c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_112}) 
 
 
V_113 = Vertex(name = 'V_113', 
	 particles = [P.h2, P.Hp2c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_113}) 
 
 
V_114 = Vertex(name = 'V_114', 
	 particles = [P.h2, P.Hp3c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_114}) 
 
 
V_115 = Vertex(name = 'V_115', 
	 particles = [P.Hp1, P.Hp1c, P.A, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_115}) 
 
 
V_116 = Vertex(name = 'V_116', 
	 particles = [P.Hp1, P.Hp2c, P.A, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_116}) 
 
 
V_117 = Vertex(name = 'V_117', 
	 particles = [P.Hp1, P.Hp3c, P.A, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_117}) 
 
 
V_118 = Vertex(name = 'V_118', 
	 particles = [P.Hp2, P.Hp1c, P.A, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_118}) 
 
 
V_119 = Vertex(name = 'V_119', 
	 particles = [P.Hp2, P.Hp2c, P.A, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_119}) 
 
 
V_120 = Vertex(name = 'V_120', 
	 particles = [P.Hp2, P.Hp3c, P.A, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_120}) 
 
 
V_121 = Vertex(name = 'V_121', 
	 particles = [P.Hp3, P.Hp1c, P.A, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_121}) 
 
 
V_122 = Vertex(name = 'V_122', 
	 particles = [P.Hp3, P.Hp2c, P.A, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_122}) 
 
 
V_123 = Vertex(name = 'V_123', 
	 particles = [P.Hp3, P.Hp3c, P.A, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_123}) 
 
 
V_124 = Vertex(name = 'V_124', 
	 particles = [P.Hp1, P.Hp1c, P.A, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_124}) 
 
 
V_125 = Vertex(name = 'V_125', 
	 particles = [P.Hp1, P.Hp2c, P.A, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_125}) 
 
 
V_126 = Vertex(name = 'V_126', 
	 particles = [P.Hp1, P.Hp3c, P.A, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_126}) 
 
 
V_127 = Vertex(name = 'V_127', 
	 particles = [P.Hp2, P.Hp1c, P.A, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_127}) 
 
 
V_128 = Vertex(name = 'V_128', 
	 particles = [P.Hp2, P.Hp2c, P.A, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_128}) 
 
 
V_129 = Vertex(name = 'V_129', 
	 particles = [P.Hp2, P.Hp3c, P.A, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_129}) 
 
 
V_130 = Vertex(name = 'V_130', 
	 particles = [P.Hp3, P.Hp1c, P.A, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_130}) 
 
 
V_131 = Vertex(name = 'V_131', 
	 particles = [P.Hp3, P.Hp2c, P.A, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_131}) 
 
 
V_132 = Vertex(name = 'V_132', 
	 particles = [P.Hp3, P.Hp3c, P.A, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_132}) 
 
 
V_133 = Vertex(name = 'V_133', 
	 particles = [P.Hp1, P.Hp1c, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_133}) 
 
 
V_134 = Vertex(name = 'V_134', 
	 particles = [P.Hp1, P.Hp2c, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_134}) 
 
 
V_135 = Vertex(name = 'V_135', 
	 particles = [P.Hp1, P.Hp3c, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_135}) 
 
 
V_136 = Vertex(name = 'V_136', 
	 particles = [P.Hp2, P.Hp1c, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_136}) 
 
 
V_137 = Vertex(name = 'V_137', 
	 particles = [P.Hp2, P.Hp2c, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_137}) 
 
 
V_138 = Vertex(name = 'V_138', 
	 particles = [P.Hp2, P.Hp3c, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_138}) 
 
 
V_139 = Vertex(name = 'V_139', 
	 particles = [P.Hp3, P.Hp1c, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_139}) 
 
 
V_140 = Vertex(name = 'V_140', 
	 particles = [P.Hp3, P.Hp2c, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_140}) 
 
 
V_141 = Vertex(name = 'V_141', 
	 particles = [P.Hp3, P.Hp3c, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_141}) 
 
 
V_142 = Vertex(name = 'V_142', 
	 particles = [P.Hp1, P.Hp1c, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_142}) 
 
 
V_143 = Vertex(name = 'V_143', 
	 particles = [P.Hp1, P.Hp2c, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_143}) 
 
 
V_144 = Vertex(name = 'V_144', 
	 particles = [P.Hp1, P.Hp3c, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_144}) 
 
 
V_145 = Vertex(name = 'V_145', 
	 particles = [P.Hp2, P.Hp1c, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_145}) 
 
 
V_146 = Vertex(name = 'V_146', 
	 particles = [P.Hp2, P.Hp2c, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_146}) 
 
 
V_147 = Vertex(name = 'V_147', 
	 particles = [P.Hp2, P.Hp3c, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_147}) 
 
 
V_148 = Vertex(name = 'V_148', 
	 particles = [P.Hp3, P.Hp1c, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_148}) 
 
 
V_149 = Vertex(name = 'V_149', 
	 particles = [P.Hp3, P.Hp2c, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_149}) 
 
 
V_150 = Vertex(name = 'V_150', 
	 particles = [P.Hp3, P.Hp3c, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_150}) 
 
 
V_151 = Vertex(name = 'V_151', 
	 particles = [P.Ah, P.h1, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_151}) 
 
 
V_152 = Vertex(name = 'V_152', 
	 particles = [P.Ah, P.h2, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_152}) 
 
 
V_153 = Vertex(name = 'V_153', 
	 particles = [P.Ah, P.Hp1, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_153}) 
 
 
V_154 = Vertex(name = 'V_154', 
	 particles = [P.Ah, P.Hp2, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_154}) 
 
 
V_155 = Vertex(name = 'V_155', 
	 particles = [P.Ah, P.Hp3, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_155}) 
 
 
V_156 = Vertex(name = 'V_156', 
	 particles = [P.Ah, P.Hp1c, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_156}) 
 
 
V_157 = Vertex(name = 'V_157', 
	 particles = [P.Ah, P.Hp2c, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_157}) 
 
 
V_158 = Vertex(name = 'V_158', 
	 particles = [P.Ah, P.Hp3c, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_158}) 
 
 
V_159 = Vertex(name = 'V_159', 
	 particles = [P.etI, P.h1, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_159}) 
 
 
V_160 = Vertex(name = 'V_160', 
	 particles = [P.etI, P.h2, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_160}) 
 
 
V_161 = Vertex(name = 'V_161', 
	 particles = [P.etI, P.Hp1, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_161}) 
 
 
V_162 = Vertex(name = 'V_162', 
	 particles = [P.etI, P.Hp2, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_162}) 
 
 
V_163 = Vertex(name = 'V_163', 
	 particles = [P.etI, P.Hp3, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_163}) 
 
 
V_164 = Vertex(name = 'V_164', 
	 particles = [P.etI, P.Hp1c, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_164}) 
 
 
V_165 = Vertex(name = 'V_165', 
	 particles = [P.etI, P.Hp2c, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_165}) 
 
 
V_166 = Vertex(name = 'V_166', 
	 particles = [P.etI, P.Hp3c, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_166}) 
 
 
V_167 = Vertex(name = 'V_167', 
	 particles = [P.h1, P.Hp1, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_167}) 
 
 
V_168 = Vertex(name = 'V_168', 
	 particles = [P.h1, P.Hp2, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_168}) 
 
 
V_169 = Vertex(name = 'V_169', 
	 particles = [P.h1, P.Hp3, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_169}) 
 
 
V_170 = Vertex(name = 'V_170', 
	 particles = [P.h2, P.Hp1, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_170}) 
 
 
V_171 = Vertex(name = 'V_171', 
	 particles = [P.h2, P.Hp2, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_171}) 
 
 
V_172 = Vertex(name = 'V_172', 
	 particles = [P.h2, P.Hp3, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_172}) 
 
 
V_173 = Vertex(name = 'V_173', 
	 particles = [P.h1, P.Hp1c, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_173}) 
 
 
V_174 = Vertex(name = 'V_174', 
	 particles = [P.h1, P.Hp2c, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_174}) 
 
 
V_175 = Vertex(name = 'V_175', 
	 particles = [P.h1, P.Hp3c, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_175}) 
 
 
V_176 = Vertex(name = 'V_176', 
	 particles = [P.h2, P.Hp1c, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_176}) 
 
 
V_177 = Vertex(name = 'V_177', 
	 particles = [P.h2, P.Hp2c, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_177}) 
 
 
V_178 = Vertex(name = 'V_178', 
	 particles = [P.h2, P.Hp3c, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_178}) 
 
 
V_179 = Vertex(name = 'V_179', 
	 particles = [P.Hp1, P.Hp1c, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_179}) 
 
 
V_180 = Vertex(name = 'V_180', 
	 particles = [P.Hp1, P.Hp2c, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_180}) 
 
 
V_181 = Vertex(name = 'V_181', 
	 particles = [P.Hp1, P.Hp3c, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_181}) 
 
 
V_182 = Vertex(name = 'V_182', 
	 particles = [P.Hp2, P.Hp1c, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_182}) 
 
 
V_183 = Vertex(name = 'V_183', 
	 particles = [P.Hp2, P.Hp2c, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_183}) 
 
 
V_184 = Vertex(name = 'V_184', 
	 particles = [P.Hp2, P.Hp3c, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_184}) 
 
 
V_185 = Vertex(name = 'V_185', 
	 particles = [P.Hp3, P.Hp1c, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_185}) 
 
 
V_186 = Vertex(name = 'V_186', 
	 particles = [P.Hp3, P.Hp2c, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_186}) 
 
 
V_187 = Vertex(name = 'V_187', 
	 particles = [P.Hp3, P.Hp3c, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_187}) 
 
 
V_188 = Vertex(name = 'V_188', 
	 particles = [P.Hp1, P.Hp1c, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_188}) 
 
 
V_189 = Vertex(name = 'V_189', 
	 particles = [P.Hp1, P.Hp2c, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_189}) 
 
 
V_190 = Vertex(name = 'V_190', 
	 particles = [P.Hp1, P.Hp3c, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_190}) 
 
 
V_191 = Vertex(name = 'V_191', 
	 particles = [P.Hp2, P.Hp1c, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_191}) 
 
 
V_192 = Vertex(name = 'V_192', 
	 particles = [P.Hp2, P.Hp2c, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_192}) 
 
 
V_193 = Vertex(name = 'V_193', 
	 particles = [P.Hp2, P.Hp3c, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_193}) 
 
 
V_194 = Vertex(name = 'V_194', 
	 particles = [P.Hp3, P.Hp1c, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_194}) 
 
 
V_195 = Vertex(name = 'V_195', 
	 particles = [P.Hp3, P.Hp2c, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_195}) 
 
 
V_196 = Vertex(name = 'V_196', 
	 particles = [P.Hp3, P.Hp3c, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_196}) 
 
 
V_197 = Vertex(name = 'V_197', 
	 particles = [P.h1, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_197}) 
 
 
V_198 = Vertex(name = 'V_198', 
	 particles = [P.h2, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_198}) 
 
 
V_199 = Vertex(name = 'V_199', 
	 particles = [P.h1, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_199}) 
 
 
V_200 = Vertex(name = 'V_200', 
	 particles = [P.h2, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_200}) 
 
 
V_201 = Vertex(name = 'V_201', 
	 particles = [P.Hp1, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_201}) 
 
 
V_202 = Vertex(name = 'V_202', 
	 particles = [P.Hp2, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_202}) 
 
 
V_203 = Vertex(name = 'V_203', 
	 particles = [P.Hp3, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_203}) 
 
 
V_204 = Vertex(name = 'V_204', 
	 particles = [P.Hp1, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_204}) 
 
 
V_205 = Vertex(name = 'V_205', 
	 particles = [P.Hp2, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_205}) 
 
 
V_206 = Vertex(name = 'V_206', 
	 particles = [P.Hp3, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_206}) 
 
 
V_207 = Vertex(name = 'V_207', 
	 particles = [P.Hp1c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_207}) 
 
 
V_208 = Vertex(name = 'V_208', 
	 particles = [P.Hp2c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_208}) 
 
 
V_209 = Vertex(name = 'V_209', 
	 particles = [P.Hp3c, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_209}) 
 
 
V_210 = Vertex(name = 'V_210', 
	 particles = [P.Hp1c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_210}) 
 
 
V_211 = Vertex(name = 'V_211', 
	 particles = [P.Hp2c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_211}) 
 
 
V_212 = Vertex(name = 'V_212', 
	 particles = [P.Hp3c, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_212}) 
 
 
V_213 = Vertex(name = 'V_213', 
	 particles = [P.d1bar, P.d1, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_213,(0,1):C.GC_214}) 
 
 
V_214 = Vertex(name = 'V_214', 
	 particles = [P.d1bar, P.d2, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_215,(0,1):C.GC_216}) 
 
 
V_215 = Vertex(name = 'V_215', 
	 particles = [P.d1bar, P.d3, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_217,(0,1):C.GC_218}) 
 
 
V_216 = Vertex(name = 'V_216', 
	 particles = [P.d2bar, P.d1, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_219,(0,1):C.GC_220}) 
 
 
V_217 = Vertex(name = 'V_217', 
	 particles = [P.d2bar, P.d2, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_221,(0,1):C.GC_222}) 
 
 
V_218 = Vertex(name = 'V_218', 
	 particles = [P.d2bar, P.d3, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_223,(0,1):C.GC_224}) 
 
 
V_219 = Vertex(name = 'V_219', 
	 particles = [P.d3bar, P.d1, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_225,(0,1):C.GC_226}) 
 
 
V_220 = Vertex(name = 'V_220', 
	 particles = [P.d3bar, P.d2, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_227,(0,1):C.GC_228}) 
 
 
V_221 = Vertex(name = 'V_221', 
	 particles = [P.d3bar, P.d3, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_229,(0,1):C.GC_230}) 
 
 
V_222 = Vertex(name = 'V_222', 
	 particles = [P.e1bar, P.e1, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_231,(0,1):C.GC_232}) 
 
 
V_223 = Vertex(name = 'V_223', 
	 particles = [P.e1bar, P.e2, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_233,(0,1):C.GC_234}) 
 
 
V_224 = Vertex(name = 'V_224', 
	 particles = [P.e1bar, P.e3, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_235,(0,1):C.GC_236}) 
 
 
V_225 = Vertex(name = 'V_225', 
	 particles = [P.e2bar, P.e1, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_237,(0,1):C.GC_238}) 
 
 
V_226 = Vertex(name = 'V_226', 
	 particles = [P.e2bar, P.e2, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_239,(0,1):C.GC_240}) 
 
 
V_227 = Vertex(name = 'V_227', 
	 particles = [P.e2bar, P.e3, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_241,(0,1):C.GC_242}) 
 
 
V_228 = Vertex(name = 'V_228', 
	 particles = [P.e3bar, P.e1, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_243,(0,1):C.GC_244}) 
 
 
V_229 = Vertex(name = 'V_229', 
	 particles = [P.e3bar, P.e2, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_245,(0,1):C.GC_246}) 
 
 
V_230 = Vertex(name = 'V_230', 
	 particles = [P.e3bar, P.e3, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_247,(0,1):C.GC_248}) 
 
 
V_231 = Vertex(name = 'V_231', 
	 particles = [P.u1bar, P.u1, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_249,(0,1):C.GC_250}) 
 
 
V_232 = Vertex(name = 'V_232', 
	 particles = [P.u1bar, P.u2, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_251,(0,1):C.GC_252}) 
 
 
V_233 = Vertex(name = 'V_233', 
	 particles = [P.u1bar, P.u3, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_253,(0,1):C.GC_254}) 
 
 
V_234 = Vertex(name = 'V_234', 
	 particles = [P.u2bar, P.u1, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_255,(0,1):C.GC_256}) 
 
 
V_235 = Vertex(name = 'V_235', 
	 particles = [P.u2bar, P.u2, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_257,(0,1):C.GC_258}) 
 
 
V_236 = Vertex(name = 'V_236', 
	 particles = [P.u2bar, P.u3, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_259,(0,1):C.GC_260}) 
 
 
V_237 = Vertex(name = 'V_237', 
	 particles = [P.u3bar, P.u1, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_261,(0,1):C.GC_262}) 
 
 
V_238 = Vertex(name = 'V_238', 
	 particles = [P.u3bar, P.u2, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_263,(0,1):C.GC_264}) 
 
 
V_239 = Vertex(name = 'V_239', 
	 particles = [P.u3bar, P.u3, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_265,(0,1):C.GC_266}) 
 
 
V_240 = Vertex(name = 'V_240', 
	 particles = [P.d1bar, P.d1, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_267,(0,1):C.GC_268}) 
 
 
V_241 = Vertex(name = 'V_241', 
	 particles = [P.d1bar, P.d2, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_269,(0,1):C.GC_270}) 
 
 
V_242 = Vertex(name = 'V_242', 
	 particles = [P.d1bar, P.d3, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_271,(0,1):C.GC_272}) 
 
 
V_243 = Vertex(name = 'V_243', 
	 particles = [P.d2bar, P.d1, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_273,(0,1):C.GC_274}) 
 
 
V_244 = Vertex(name = 'V_244', 
	 particles = [P.d2bar, P.d2, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_275,(0,1):C.GC_276}) 
 
 
V_245 = Vertex(name = 'V_245', 
	 particles = [P.d2bar, P.d3, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_277,(0,1):C.GC_278}) 
 
 
V_246 = Vertex(name = 'V_246', 
	 particles = [P.d3bar, P.d1, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_279,(0,1):C.GC_280}) 
 
 
V_247 = Vertex(name = 'V_247', 
	 particles = [P.d3bar, P.d2, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_281,(0,1):C.GC_282}) 
 
 
V_248 = Vertex(name = 'V_248', 
	 particles = [P.d3bar, P.d3, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_283,(0,1):C.GC_284}) 
 
 
V_249 = Vertex(name = 'V_249', 
	 particles = [P.e1bar, P.e1, P.etI], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_285,(0,1):C.GC_286}) 
 
 
V_250 = Vertex(name = 'V_250', 
	 particles = [P.e1bar, P.e2, P.etI], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_287,(0,1):C.GC_288}) 
 
 
V_251 = Vertex(name = 'V_251', 
	 particles = [P.e1bar, P.e3, P.etI], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_289,(0,1):C.GC_290}) 
 
 
V_252 = Vertex(name = 'V_252', 
	 particles = [P.e2bar, P.e1, P.etI], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_291,(0,1):C.GC_292}) 
 
 
V_253 = Vertex(name = 'V_253', 
	 particles = [P.e2bar, P.e2, P.etI], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_293,(0,1):C.GC_294}) 
 
 
V_254 = Vertex(name = 'V_254', 
	 particles = [P.e2bar, P.e3, P.etI], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_295,(0,1):C.GC_296}) 
 
 
V_255 = Vertex(name = 'V_255', 
	 particles = [P.e3bar, P.e1, P.etI], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_297,(0,1):C.GC_298}) 
 
 
V_256 = Vertex(name = 'V_256', 
	 particles = [P.e3bar, P.e2, P.etI], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_299,(0,1):C.GC_300}) 
 
 
V_257 = Vertex(name = 'V_257', 
	 particles = [P.e3bar, P.e3, P.etI], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_301,(0,1):C.GC_302}) 
 
 
V_258 = Vertex(name = 'V_258', 
	 particles = [P.u1bar, P.u1, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_303,(0,1):C.GC_304}) 
 
 
V_259 = Vertex(name = 'V_259', 
	 particles = [P.u1bar, P.u2, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_305,(0,1):C.GC_306}) 
 
 
V_260 = Vertex(name = 'V_260', 
	 particles = [P.u1bar, P.u3, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_307,(0,1):C.GC_308}) 
 
 
V_261 = Vertex(name = 'V_261', 
	 particles = [P.u2bar, P.u1, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_309,(0,1):C.GC_310}) 
 
 
V_262 = Vertex(name = 'V_262', 
	 particles = [P.u2bar, P.u2, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_311,(0,1):C.GC_312}) 
 
 
V_263 = Vertex(name = 'V_263', 
	 particles = [P.u2bar, P.u3, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_313,(0,1):C.GC_314}) 
 
 
V_264 = Vertex(name = 'V_264', 
	 particles = [P.u3bar, P.u1, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_315,(0,1):C.GC_316}) 
 
 
V_265 = Vertex(name = 'V_265', 
	 particles = [P.u3bar, P.u2, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_317,(0,1):C.GC_318}) 
 
 
V_266 = Vertex(name = 'V_266', 
	 particles = [P.u3bar, P.u3, P.etI], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_319,(0,1):C.GC_320}) 
 
 
V_267 = Vertex(name = 'V_267', 
	 particles = [P.d1bar, P.d1, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_321,(0,1):C.GC_322}) 
 
 
V_268 = Vertex(name = 'V_268', 
	 particles = [P.d1bar, P.d1, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_323,(0,1):C.GC_324}) 
 
 
V_269 = Vertex(name = 'V_269', 
	 particles = [P.d1bar, P.d2, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_325,(0,1):C.GC_326}) 
 
 
V_270 = Vertex(name = 'V_270', 
	 particles = [P.d1bar, P.d2, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_327,(0,1):C.GC_328}) 
 
 
V_271 = Vertex(name = 'V_271', 
	 particles = [P.d1bar, P.d3, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_329,(0,1):C.GC_330}) 
 
 
V_272 = Vertex(name = 'V_272', 
	 particles = [P.d1bar, P.d3, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_331,(0,1):C.GC_332}) 
 
 
V_273 = Vertex(name = 'V_273', 
	 particles = [P.d2bar, P.d1, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_333,(0,1):C.GC_334}) 
 
 
V_274 = Vertex(name = 'V_274', 
	 particles = [P.d2bar, P.d1, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_335,(0,1):C.GC_336}) 
 
 
V_275 = Vertex(name = 'V_275', 
	 particles = [P.d2bar, P.d2, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_337,(0,1):C.GC_338}) 
 
 
V_276 = Vertex(name = 'V_276', 
	 particles = [P.d2bar, P.d2, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_339,(0,1):C.GC_340}) 
 
 
V_277 = Vertex(name = 'V_277', 
	 particles = [P.d2bar, P.d3, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_341,(0,1):C.GC_342}) 
 
 
V_278 = Vertex(name = 'V_278', 
	 particles = [P.d2bar, P.d3, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_343,(0,1):C.GC_344}) 
 
 
V_279 = Vertex(name = 'V_279', 
	 particles = [P.d3bar, P.d1, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_345,(0,1):C.GC_346}) 
 
 
V_280 = Vertex(name = 'V_280', 
	 particles = [P.d3bar, P.d1, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_347,(0,1):C.GC_348}) 
 
 
V_281 = Vertex(name = 'V_281', 
	 particles = [P.d3bar, P.d2, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_349,(0,1):C.GC_350}) 
 
 
V_282 = Vertex(name = 'V_282', 
	 particles = [P.d3bar, P.d2, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_351,(0,1):C.GC_352}) 
 
 
V_283 = Vertex(name = 'V_283', 
	 particles = [P.d3bar, P.d3, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_353,(0,1):C.GC_354}) 
 
 
V_284 = Vertex(name = 'V_284', 
	 particles = [P.d3bar, P.d3, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_355,(0,1):C.GC_356}) 
 
 
V_285 = Vertex(name = 'V_285', 
	 particles = [P.u1bar, P.d1, P.Hp1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_357,(0,1):C.GC_358}) 
 
 
V_286 = Vertex(name = 'V_286', 
	 particles = [P.u1bar, P.d1, P.Hp2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_359,(0,1):C.GC_360}) 
 
 
V_287 = Vertex(name = 'V_287', 
	 particles = [P.u1bar, P.d1, P.Hp3], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_361,(0,1):C.GC_362}) 
 
 
V_288 = Vertex(name = 'V_288', 
	 particles = [P.u1bar, P.d2, P.Hp1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_363,(0,1):C.GC_364}) 
 
 
V_289 = Vertex(name = 'V_289', 
	 particles = [P.u1bar, P.d2, P.Hp2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_365,(0,1):C.GC_366}) 
 
 
V_290 = Vertex(name = 'V_290', 
	 particles = [P.u1bar, P.d2, P.Hp3], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_367,(0,1):C.GC_368}) 
 
 
V_291 = Vertex(name = 'V_291', 
	 particles = [P.u1bar, P.d3, P.Hp1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_369,(0,1):C.GC_370}) 
 
 
V_292 = Vertex(name = 'V_292', 
	 particles = [P.u1bar, P.d3, P.Hp2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_371,(0,1):C.GC_372}) 
 
 
V_293 = Vertex(name = 'V_293', 
	 particles = [P.u1bar, P.d3, P.Hp3], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_373,(0,1):C.GC_374}) 
 
 
V_294 = Vertex(name = 'V_294', 
	 particles = [P.u2bar, P.d1, P.Hp1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_375,(0,1):C.GC_376}) 
 
 
V_295 = Vertex(name = 'V_295', 
	 particles = [P.u2bar, P.d1, P.Hp2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_377,(0,1):C.GC_378}) 
 
 
V_296 = Vertex(name = 'V_296', 
	 particles = [P.u2bar, P.d1, P.Hp3], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_379,(0,1):C.GC_380}) 
 
 
V_297 = Vertex(name = 'V_297', 
	 particles = [P.u2bar, P.d2, P.Hp1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_381,(0,1):C.GC_382}) 
 
 
V_298 = Vertex(name = 'V_298', 
	 particles = [P.u2bar, P.d2, P.Hp2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_383,(0,1):C.GC_384}) 
 
 
V_299 = Vertex(name = 'V_299', 
	 particles = [P.u2bar, P.d2, P.Hp3], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_385,(0,1):C.GC_386}) 
 
 
V_300 = Vertex(name = 'V_300', 
	 particles = [P.u2bar, P.d3, P.Hp1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_387,(0,1):C.GC_388}) 
 
 
V_301 = Vertex(name = 'V_301', 
	 particles = [P.u2bar, P.d3, P.Hp2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_389,(0,1):C.GC_390}) 
 
 
V_302 = Vertex(name = 'V_302', 
	 particles = [P.u2bar, P.d3, P.Hp3], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_391,(0,1):C.GC_392}) 
 
 
V_303 = Vertex(name = 'V_303', 
	 particles = [P.u3bar, P.d1, P.Hp1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_393,(0,1):C.GC_394}) 
 
 
V_304 = Vertex(name = 'V_304', 
	 particles = [P.u3bar, P.d1, P.Hp2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_395,(0,1):C.GC_396}) 
 
 
V_305 = Vertex(name = 'V_305', 
	 particles = [P.u3bar, P.d1, P.Hp3], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_397,(0,1):C.GC_398}) 
 
 
V_306 = Vertex(name = 'V_306', 
	 particles = [P.u3bar, P.d2, P.Hp1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_399,(0,1):C.GC_400}) 
 
 
V_307 = Vertex(name = 'V_307', 
	 particles = [P.u3bar, P.d2, P.Hp2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_401,(0,1):C.GC_402}) 
 
 
V_308 = Vertex(name = 'V_308', 
	 particles = [P.u3bar, P.d2, P.Hp3], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_403,(0,1):C.GC_404}) 
 
 
V_309 = Vertex(name = 'V_309', 
	 particles = [P.u3bar, P.d3, P.Hp1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_405,(0,1):C.GC_406}) 
 
 
V_310 = Vertex(name = 'V_310', 
	 particles = [P.u3bar, P.d3, P.Hp2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_407,(0,1):C.GC_408}) 
 
 
V_311 = Vertex(name = 'V_311', 
	 particles = [P.u3bar, P.d3, P.Hp3], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_409,(0,1):C.GC_410}) 
 
 
V_312 = Vertex(name = 'V_312', 
	 particles = [P.nu1, P.e1, P.Hp1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_411,(0,1):C.GC_412}) 
 
 
V_313 = Vertex(name = 'V_313', 
	 particles = [P.nu1, P.e1, P.Hp2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_413,(0,1):C.GC_414}) 
 
 
V_314 = Vertex(name = 'V_314', 
	 particles = [P.nu1, P.e1, P.Hp3], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_415,(0,1):C.GC_416}) 
 
 
V_315 = Vertex(name = 'V_315', 
	 particles = [P.nu1, P.e2, P.Hp1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_417,(0,1):C.GC_418}) 
 
 
V_316 = Vertex(name = 'V_316', 
	 particles = [P.nu1, P.e2, P.Hp2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_419,(0,1):C.GC_420}) 
 
 
V_317 = Vertex(name = 'V_317', 
	 particles = [P.nu1, P.e2, P.Hp3], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_421,(0,1):C.GC_422}) 
 
 
V_318 = Vertex(name = 'V_318', 
	 particles = [P.nu1, P.e3, P.Hp1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_423,(0,1):C.GC_424}) 
 
 
V_319 = Vertex(name = 'V_319', 
	 particles = [P.nu1, P.e3, P.Hp2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_425,(0,1):C.GC_426}) 
 
 
V_320 = Vertex(name = 'V_320', 
	 particles = [P.nu1, P.e3, P.Hp3], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_427,(0,1):C.GC_428}) 
 
 
V_321 = Vertex(name = 'V_321', 
	 particles = [P.nu2, P.e1, P.Hp1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_429,(0,1):C.GC_430}) 
 
 
V_322 = Vertex(name = 'V_322', 
	 particles = [P.nu2, P.e1, P.Hp2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_431,(0,1):C.GC_432}) 
 
 
V_323 = Vertex(name = 'V_323', 
	 particles = [P.nu2, P.e1, P.Hp3], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_433,(0,1):C.GC_434}) 
 
 
V_324 = Vertex(name = 'V_324', 
	 particles = [P.nu2, P.e2, P.Hp1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_435,(0,1):C.GC_436}) 
 
 
V_325 = Vertex(name = 'V_325', 
	 particles = [P.nu2, P.e2, P.Hp2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_437,(0,1):C.GC_438}) 
 
 
V_326 = Vertex(name = 'V_326', 
	 particles = [P.nu2, P.e2, P.Hp3], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_439,(0,1):C.GC_440}) 
 
 
V_327 = Vertex(name = 'V_327', 
	 particles = [P.nu2, P.e3, P.Hp1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_441,(0,1):C.GC_442}) 
 
 
V_328 = Vertex(name = 'V_328', 
	 particles = [P.nu2, P.e3, P.Hp2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_443,(0,1):C.GC_444}) 
 
 
V_329 = Vertex(name = 'V_329', 
	 particles = [P.nu2, P.e3, P.Hp3], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_445,(0,1):C.GC_446}) 
 
 
V_330 = Vertex(name = 'V_330', 
	 particles = [P.nu3, P.e1, P.Hp1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_447,(0,1):C.GC_448}) 
 
 
V_331 = Vertex(name = 'V_331', 
	 particles = [P.nu3, P.e1, P.Hp2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_449,(0,1):C.GC_450}) 
 
 
V_332 = Vertex(name = 'V_332', 
	 particles = [P.nu3, P.e1, P.Hp3], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_451,(0,1):C.GC_452}) 
 
 
V_333 = Vertex(name = 'V_333', 
	 particles = [P.nu3, P.e2, P.Hp1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_453,(0,1):C.GC_454}) 
 
 
V_334 = Vertex(name = 'V_334', 
	 particles = [P.nu3, P.e2, P.Hp2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_455,(0,1):C.GC_456}) 
 
 
V_335 = Vertex(name = 'V_335', 
	 particles = [P.nu3, P.e2, P.Hp3], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_457,(0,1):C.GC_458}) 
 
 
V_336 = Vertex(name = 'V_336', 
	 particles = [P.nu3, P.e3, P.Hp1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_459,(0,1):C.GC_460}) 
 
 
V_337 = Vertex(name = 'V_337', 
	 particles = [P.nu3, P.e3, P.Hp2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_461,(0,1):C.GC_462}) 
 
 
V_338 = Vertex(name = 'V_338', 
	 particles = [P.nu3, P.e3, P.Hp3], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_463,(0,1):C.GC_464}) 
 
 
V_339 = Vertex(name = 'V_339', 
	 particles = [P.e1bar, P.e1, P.h1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_465,(0,1):C.GC_466}) 
 
 
V_340 = Vertex(name = 'V_340', 
	 particles = [P.e1bar, P.e1, P.h2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_467,(0,1):C.GC_468}) 
 
 
V_341 = Vertex(name = 'V_341', 
	 particles = [P.e1bar, P.e2, P.h1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_469,(0,1):C.GC_470}) 
 
 
V_342 = Vertex(name = 'V_342', 
	 particles = [P.e1bar, P.e2, P.h2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_471,(0,1):C.GC_472}) 
 
 
V_343 = Vertex(name = 'V_343', 
	 particles = [P.e1bar, P.e3, P.h1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_473,(0,1):C.GC_474}) 
 
 
V_344 = Vertex(name = 'V_344', 
	 particles = [P.e1bar, P.e3, P.h2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_475,(0,1):C.GC_476}) 
 
 
V_345 = Vertex(name = 'V_345', 
	 particles = [P.e2bar, P.e1, P.h1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_477,(0,1):C.GC_478}) 
 
 
V_346 = Vertex(name = 'V_346', 
	 particles = [P.e2bar, P.e1, P.h2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_479,(0,1):C.GC_480}) 
 
 
V_347 = Vertex(name = 'V_347', 
	 particles = [P.e2bar, P.e2, P.h1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_481,(0,1):C.GC_482}) 
 
 
V_348 = Vertex(name = 'V_348', 
	 particles = [P.e2bar, P.e2, P.h2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_483,(0,1):C.GC_484}) 
 
 
V_349 = Vertex(name = 'V_349', 
	 particles = [P.e2bar, P.e3, P.h1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_485,(0,1):C.GC_486}) 
 
 
V_350 = Vertex(name = 'V_350', 
	 particles = [P.e2bar, P.e3, P.h2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_487,(0,1):C.GC_488}) 
 
 
V_351 = Vertex(name = 'V_351', 
	 particles = [P.e3bar, P.e1, P.h1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_489,(0,1):C.GC_490}) 
 
 
V_352 = Vertex(name = 'V_352', 
	 particles = [P.e3bar, P.e1, P.h2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_491,(0,1):C.GC_492}) 
 
 
V_353 = Vertex(name = 'V_353', 
	 particles = [P.e3bar, P.e2, P.h1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_493,(0,1):C.GC_494}) 
 
 
V_354 = Vertex(name = 'V_354', 
	 particles = [P.e3bar, P.e2, P.h2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_495,(0,1):C.GC_496}) 
 
 
V_355 = Vertex(name = 'V_355', 
	 particles = [P.e3bar, P.e3, P.h1], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_497,(0,1):C.GC_498}) 
 
 
V_356 = Vertex(name = 'V_356', 
	 particles = [P.e3bar, P.e3, P.h2], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_499,(0,1):C.GC_500}) 
 
 
V_357 = Vertex(name = 'V_357', 
	 particles = [P.u1bar, P.u1, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_501,(0,1):C.GC_502}) 
 
 
V_358 = Vertex(name = 'V_358', 
	 particles = [P.u1bar, P.u1, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_503,(0,1):C.GC_504}) 
 
 
V_359 = Vertex(name = 'V_359', 
	 particles = [P.u1bar, P.u2, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_505,(0,1):C.GC_506}) 
 
 
V_360 = Vertex(name = 'V_360', 
	 particles = [P.u1bar, P.u2, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_507,(0,1):C.GC_508}) 
 
 
V_361 = Vertex(name = 'V_361', 
	 particles = [P.u1bar, P.u3, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_509,(0,1):C.GC_510}) 
 
 
V_362 = Vertex(name = 'V_362', 
	 particles = [P.u1bar, P.u3, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_511,(0,1):C.GC_512}) 
 
 
V_363 = Vertex(name = 'V_363', 
	 particles = [P.u2bar, P.u1, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_513,(0,1):C.GC_514}) 
 
 
V_364 = Vertex(name = 'V_364', 
	 particles = [P.u2bar, P.u1, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_515,(0,1):C.GC_516}) 
 
 
V_365 = Vertex(name = 'V_365', 
	 particles = [P.u2bar, P.u2, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_517,(0,1):C.GC_518}) 
 
 
V_366 = Vertex(name = 'V_366', 
	 particles = [P.u2bar, P.u2, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_519,(0,1):C.GC_520}) 
 
 
V_367 = Vertex(name = 'V_367', 
	 particles = [P.u2bar, P.u3, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_521,(0,1):C.GC_522}) 
 
 
V_368 = Vertex(name = 'V_368', 
	 particles = [P.u2bar, P.u3, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_523,(0,1):C.GC_524}) 
 
 
V_369 = Vertex(name = 'V_369', 
	 particles = [P.u3bar, P.u1, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_525,(0,1):C.GC_526}) 
 
 
V_370 = Vertex(name = 'V_370', 
	 particles = [P.u3bar, P.u1, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_527,(0,1):C.GC_528}) 
 
 
V_371 = Vertex(name = 'V_371', 
	 particles = [P.u3bar, P.u2, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_529,(0,1):C.GC_530}) 
 
 
V_372 = Vertex(name = 'V_372', 
	 particles = [P.u3bar, P.u2, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_531,(0,1):C.GC_532}) 
 
 
V_373 = Vertex(name = 'V_373', 
	 particles = [P.u3bar, P.u3, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_533,(0,1):C.GC_534}) 
 
 
V_374 = Vertex(name = 'V_374', 
	 particles = [P.u3bar, P.u3, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_535,(0,1):C.GC_536}) 
 
 
V_375 = Vertex(name = 'V_375', 
	 particles = [P.d1bar, P.u1, P.Hp1c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_537,(0,1):C.GC_538}) 
 
 
V_376 = Vertex(name = 'V_376', 
	 particles = [P.d1bar, P.u1, P.Hp2c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_539,(0,1):C.GC_540}) 
 
 
V_377 = Vertex(name = 'V_377', 
	 particles = [P.d1bar, P.u1, P.Hp3c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_541,(0,1):C.GC_542}) 
 
 
V_378 = Vertex(name = 'V_378', 
	 particles = [P.d1bar, P.u2, P.Hp1c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_543,(0,1):C.GC_544}) 
 
 
V_379 = Vertex(name = 'V_379', 
	 particles = [P.d1bar, P.u2, P.Hp2c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_545,(0,1):C.GC_546}) 
 
 
V_380 = Vertex(name = 'V_380', 
	 particles = [P.d1bar, P.u2, P.Hp3c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_547,(0,1):C.GC_548}) 
 
 
V_381 = Vertex(name = 'V_381', 
	 particles = [P.d1bar, P.u3, P.Hp1c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_549,(0,1):C.GC_550}) 
 
 
V_382 = Vertex(name = 'V_382', 
	 particles = [P.d1bar, P.u3, P.Hp2c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_551,(0,1):C.GC_552}) 
 
 
V_383 = Vertex(name = 'V_383', 
	 particles = [P.d1bar, P.u3, P.Hp3c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_553,(0,1):C.GC_554}) 
 
 
V_384 = Vertex(name = 'V_384', 
	 particles = [P.d2bar, P.u1, P.Hp1c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_555,(0,1):C.GC_556}) 
 
 
V_385 = Vertex(name = 'V_385', 
	 particles = [P.d2bar, P.u1, P.Hp2c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_557,(0,1):C.GC_558}) 
 
 
V_386 = Vertex(name = 'V_386', 
	 particles = [P.d2bar, P.u1, P.Hp3c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_559,(0,1):C.GC_560}) 
 
 
V_387 = Vertex(name = 'V_387', 
	 particles = [P.d2bar, P.u2, P.Hp1c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_561,(0,1):C.GC_562}) 
 
 
V_388 = Vertex(name = 'V_388', 
	 particles = [P.d2bar, P.u2, P.Hp2c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_563,(0,1):C.GC_564}) 
 
 
V_389 = Vertex(name = 'V_389', 
	 particles = [P.d2bar, P.u2, P.Hp3c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_565,(0,1):C.GC_566}) 
 
 
V_390 = Vertex(name = 'V_390', 
	 particles = [P.d2bar, P.u3, P.Hp1c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_567,(0,1):C.GC_568}) 
 
 
V_391 = Vertex(name = 'V_391', 
	 particles = [P.d2bar, P.u3, P.Hp2c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_569,(0,1):C.GC_570}) 
 
 
V_392 = Vertex(name = 'V_392', 
	 particles = [P.d2bar, P.u3, P.Hp3c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_571,(0,1):C.GC_572}) 
 
 
V_393 = Vertex(name = 'V_393', 
	 particles = [P.d3bar, P.u1, P.Hp1c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_573,(0,1):C.GC_574}) 
 
 
V_394 = Vertex(name = 'V_394', 
	 particles = [P.d3bar, P.u1, P.Hp2c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_575,(0,1):C.GC_576}) 
 
 
V_395 = Vertex(name = 'V_395', 
	 particles = [P.d3bar, P.u1, P.Hp3c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_577,(0,1):C.GC_578}) 
 
 
V_396 = Vertex(name = 'V_396', 
	 particles = [P.d3bar, P.u2, P.Hp1c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_579,(0,1):C.GC_580}) 
 
 
V_397 = Vertex(name = 'V_397', 
	 particles = [P.d3bar, P.u2, P.Hp2c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_581,(0,1):C.GC_582}) 
 
 
V_398 = Vertex(name = 'V_398', 
	 particles = [P.d3bar, P.u2, P.Hp3c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_583,(0,1):C.GC_584}) 
 
 
V_399 = Vertex(name = 'V_399', 
	 particles = [P.d3bar, P.u3, P.Hp1c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_585,(0,1):C.GC_586}) 
 
 
V_400 = Vertex(name = 'V_400', 
	 particles = [P.d3bar, P.u3, P.Hp2c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_587,(0,1):C.GC_588}) 
 
 
V_401 = Vertex(name = 'V_401', 
	 particles = [P.d3bar, P.u3, P.Hp3c], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_589,(0,1):C.GC_590}) 
 
 
V_402 = Vertex(name = 'V_402', 
	 particles = [P.e1bar, P.nu1, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_591,(0,1):C.GC_592}) 
 
 
V_403 = Vertex(name = 'V_403', 
	 particles = [P.e1bar, P.nu1, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_593,(0,1):C.GC_594}) 
 
 
V_404 = Vertex(name = 'V_404', 
	 particles = [P.e1bar, P.nu1, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_595,(0,1):C.GC_596}) 
 
 
V_405 = Vertex(name = 'V_405', 
	 particles = [P.e1bar, P.nu2, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_597,(0,1):C.GC_598}) 
 
 
V_406 = Vertex(name = 'V_406', 
	 particles = [P.e1bar, P.nu2, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_599,(0,1):C.GC_600}) 
 
 
V_407 = Vertex(name = 'V_407', 
	 particles = [P.e1bar, P.nu2, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_601,(0,1):C.GC_602}) 
 
 
V_408 = Vertex(name = 'V_408', 
	 particles = [P.e1bar, P.nu3, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_603,(0,1):C.GC_604}) 
 
 
V_409 = Vertex(name = 'V_409', 
	 particles = [P.e1bar, P.nu3, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_605,(0,1):C.GC_606}) 
 
 
V_410 = Vertex(name = 'V_410', 
	 particles = [P.e1bar, P.nu3, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_607,(0,1):C.GC_608}) 
 
 
V_411 = Vertex(name = 'V_411', 
	 particles = [P.e2bar, P.nu1, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_609,(0,1):C.GC_610}) 
 
 
V_412 = Vertex(name = 'V_412', 
	 particles = [P.e2bar, P.nu1, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_611,(0,1):C.GC_612}) 
 
 
V_413 = Vertex(name = 'V_413', 
	 particles = [P.e2bar, P.nu1, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_613,(0,1):C.GC_614}) 
 
 
V_414 = Vertex(name = 'V_414', 
	 particles = [P.e2bar, P.nu2, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_615,(0,1):C.GC_616}) 
 
 
V_415 = Vertex(name = 'V_415', 
	 particles = [P.e2bar, P.nu2, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_617,(0,1):C.GC_618}) 
 
 
V_416 = Vertex(name = 'V_416', 
	 particles = [P.e2bar, P.nu2, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_619,(0,1):C.GC_620}) 
 
 
V_417 = Vertex(name = 'V_417', 
	 particles = [P.e2bar, P.nu3, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_621,(0,1):C.GC_622}) 
 
 
V_418 = Vertex(name = 'V_418', 
	 particles = [P.e2bar, P.nu3, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_623,(0,1):C.GC_624}) 
 
 
V_419 = Vertex(name = 'V_419', 
	 particles = [P.e2bar, P.nu3, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_625,(0,1):C.GC_626}) 
 
 
V_420 = Vertex(name = 'V_420', 
	 particles = [P.e3bar, P.nu1, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_627,(0,1):C.GC_628}) 
 
 
V_421 = Vertex(name = 'V_421', 
	 particles = [P.e3bar, P.nu1, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_629,(0,1):C.GC_630}) 
 
 
V_422 = Vertex(name = 'V_422', 
	 particles = [P.e3bar, P.nu1, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_631,(0,1):C.GC_632}) 
 
 
V_423 = Vertex(name = 'V_423', 
	 particles = [P.e3bar, P.nu2, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_633,(0,1):C.GC_634}) 
 
 
V_424 = Vertex(name = 'V_424', 
	 particles = [P.e3bar, P.nu2, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_635,(0,1):C.GC_636}) 
 
 
V_425 = Vertex(name = 'V_425', 
	 particles = [P.e3bar, P.nu2, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_637,(0,1):C.GC_638}) 
 
 
V_426 = Vertex(name = 'V_426', 
	 particles = [P.e3bar, P.nu3, P.Hp1c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_639,(0,1):C.GC_640}) 
 
 
V_427 = Vertex(name = 'V_427', 
	 particles = [P.e3bar, P.nu3, P.Hp2c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_641,(0,1):C.GC_642}) 
 
 
V_428 = Vertex(name = 'V_428', 
	 particles = [P.e3bar, P.nu3, P.Hp3c], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_643,(0,1):C.GC_644}) 
 
 
V_429 = Vertex(name = 'V_429', 
	 particles = [P.d1bar, P.d1, P.g], 
	 color = ['T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_645,(0,0):C.GC_646}) 
 
 
V_430 = Vertex(name = 'V_430', 
	 particles = [P.d2bar, P.d2, P.g], 
	 color = ['T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_647,(0,0):C.GC_648}) 
 
 
V_431 = Vertex(name = 'V_431', 
	 particles = [P.d3bar, P.d3, P.g], 
	 color = ['T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_649,(0,0):C.GC_650}) 
 
 
V_432 = Vertex(name = 'V_432', 
	 particles = [P.d1bar, P.d1, P.A], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_651,(0,0):C.GC_652}) 
 
 
V_433 = Vertex(name = 'V_433', 
	 particles = [P.d2bar, P.d2, P.A], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_653,(0,0):C.GC_654}) 
 
 
V_434 = Vertex(name = 'V_434', 
	 particles = [P.d3bar, P.d3, P.A], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_655,(0,0):C.GC_656}) 
 
 
V_435 = Vertex(name = 'V_435', 
	 particles = [P.d1bar, P.d1, P.Z], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_657,(0,0):C.GC_658}) 
 
 
V_436 = Vertex(name = 'V_436', 
	 particles = [P.d2bar, P.d2, P.Z], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_659,(0,0):C.GC_660}) 
 
 
V_437 = Vertex(name = 'V_437', 
	 particles = [P.d3bar, P.d3, P.Z], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_661,(0,0):C.GC_662}) 
 
 
V_438 = Vertex(name = 'V_438', 
	 particles = [P.u1bar, P.d1, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_663}) 
 
 
V_439 = Vertex(name = 'V_439', 
	 particles = [P.u1bar, P.d2, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_664}) 
 
 
V_440 = Vertex(name = 'V_440', 
	 particles = [P.u1bar, P.d3, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_665}) 
 
 
V_441 = Vertex(name = 'V_441', 
	 particles = [P.u2bar, P.d1, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_666}) 
 
 
V_442 = Vertex(name = 'V_442', 
	 particles = [P.u2bar, P.d2, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_667}) 
 
 
V_443 = Vertex(name = 'V_443', 
	 particles = [P.u2bar, P.d3, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_668}) 
 
 
V_444 = Vertex(name = 'V_444', 
	 particles = [P.u3bar, P.d1, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_669}) 
 
 
V_445 = Vertex(name = 'V_445', 
	 particles = [P.u3bar, P.d2, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_670}) 
 
 
V_446 = Vertex(name = 'V_446', 
	 particles = [P.u3bar, P.d3, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_671}) 
 
 
V_447 = Vertex(name = 'V_447', 
	 particles = [P.nu1, P.e1, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_672}) 
 
 
V_448 = Vertex(name = 'V_448', 
	 particles = [P.nu1, P.e2, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_673}) 
 
 
V_449 = Vertex(name = 'V_449', 
	 particles = [P.nu1, P.e3, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_674}) 
 
 
V_450 = Vertex(name = 'V_450', 
	 particles = [P.nu2, P.e1, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_675}) 
 
 
V_451 = Vertex(name = 'V_451', 
	 particles = [P.nu2, P.e2, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_676}) 
 
 
V_452 = Vertex(name = 'V_452', 
	 particles = [P.nu2, P.e3, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_677}) 
 
 
V_453 = Vertex(name = 'V_453', 
	 particles = [P.nu3, P.e1, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_678}) 
 
 
V_454 = Vertex(name = 'V_454', 
	 particles = [P.nu3, P.e2, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_679}) 
 
 
V_455 = Vertex(name = 'V_455', 
	 particles = [P.nu3, P.e3, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_680}) 
 
 
V_456 = Vertex(name = 'V_456', 
	 particles = [P.e1bar, P.e1, P.A], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_681,(0,0):C.GC_682}) 
 
 
V_457 = Vertex(name = 'V_457', 
	 particles = [P.e2bar, P.e2, P.A], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_683,(0,0):C.GC_684}) 
 
 
V_458 = Vertex(name = 'V_458', 
	 particles = [P.e3bar, P.e3, P.A], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_685,(0,0):C.GC_686}) 
 
 
V_459 = Vertex(name = 'V_459', 
	 particles = [P.e1bar, P.e1, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_687,(0,0):C.GC_688}) 
 
 
V_460 = Vertex(name = 'V_460', 
	 particles = [P.e2bar, P.e2, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_689,(0,0):C.GC_690}) 
 
 
V_461 = Vertex(name = 'V_461', 
	 particles = [P.e3bar, P.e3, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_691,(0,0):C.GC_692}) 
 
 
V_462 = Vertex(name = 'V_462', 
	 particles = [P.u1bar, P.u1, P.g], 
	 color = ['T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_693,(0,0):C.GC_694}) 
 
 
V_463 = Vertex(name = 'V_463', 
	 particles = [P.u2bar, P.u2, P.g], 
	 color = ['T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_695,(0,0):C.GC_696}) 
 
 
V_464 = Vertex(name = 'V_464', 
	 particles = [P.u3bar, P.u3, P.g], 
	 color = ['T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_697,(0,0):C.GC_698}) 
 
 
V_465 = Vertex(name = 'V_465', 
	 particles = [P.u1bar, P.u1, P.A], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_699,(0,0):C.GC_700}) 
 
 
V_466 = Vertex(name = 'V_466', 
	 particles = [P.u2bar, P.u2, P.A], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_701,(0,0):C.GC_702}) 
 
 
V_467 = Vertex(name = 'V_467', 
	 particles = [P.u3bar, P.u3, P.A], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_703,(0,0):C.GC_704}) 
 
 
V_468 = Vertex(name = 'V_468', 
	 particles = [P.d1bar, P.u1, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_705}) 
 
 
V_469 = Vertex(name = 'V_469', 
	 particles = [P.d1bar, P.u2, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_706}) 
 
 
V_470 = Vertex(name = 'V_470', 
	 particles = [P.d1bar, P.u3, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_707}) 
 
 
V_471 = Vertex(name = 'V_471', 
	 particles = [P.d2bar, P.u1, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_708}) 
 
 
V_472 = Vertex(name = 'V_472', 
	 particles = [P.d2bar, P.u2, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_709}) 
 
 
V_473 = Vertex(name = 'V_473', 
	 particles = [P.d2bar, P.u3, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_710}) 
 
 
V_474 = Vertex(name = 'V_474', 
	 particles = [P.d3bar, P.u1, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_711}) 
 
 
V_475 = Vertex(name = 'V_475', 
	 particles = [P.d3bar, P.u2, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_712}) 
 
 
V_476 = Vertex(name = 'V_476', 
	 particles = [P.d3bar, P.u3, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_713}) 
 
 
V_477 = Vertex(name = 'V_477', 
	 particles = [P.u1bar, P.u1, P.Z], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_714,(0,0):C.GC_715}) 
 
 
V_478 = Vertex(name = 'V_478', 
	 particles = [P.u2bar, P.u2, P.Z], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_716,(0,0):C.GC_717}) 
 
 
V_479 = Vertex(name = 'V_479', 
	 particles = [P.u3bar, P.u3, P.Z], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_718,(0,0):C.GC_719}) 
 
 
V_480 = Vertex(name = 'V_480', 
	 particles = [P.nu1, P.nu1, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_720,(0,0):C.GC_721}) 
 
 
V_481 = Vertex(name = 'V_481', 
	 particles = [P.nu2, P.nu2, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_722,(0,0):C.GC_723}) 
 
 
V_482 = Vertex(name = 'V_482', 
	 particles = [P.nu3, P.nu3, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_724,(0,0):C.GC_725}) 
 
 
V_483 = Vertex(name = 'V_483', 
	 particles = [P.e1bar, P.nu1, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_726}) 
 
 
V_484 = Vertex(name = 'V_484', 
	 particles = [P.e1bar, P.nu2, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_727}) 
 
 
V_485 = Vertex(name = 'V_485', 
	 particles = [P.e1bar, P.nu3, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_728}) 
 
 
V_486 = Vertex(name = 'V_486', 
	 particles = [P.e2bar, P.nu1, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_729}) 
 
 
V_487 = Vertex(name = 'V_487', 
	 particles = [P.e2bar, P.nu2, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_730}) 
 
 
V_488 = Vertex(name = 'V_488', 
	 particles = [P.e2bar, P.nu3, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_731}) 
 
 
V_489 = Vertex(name = 'V_489', 
	 particles = [P.e3bar, P.nu1, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_732}) 
 
 
V_490 = Vertex(name = 'V_490', 
	 particles = [P.e3bar, P.nu2, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_733}) 
 
 
V_491 = Vertex(name = 'V_491', 
	 particles = [P.e3bar, P.nu3, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_734}) 
 
 
V_492 = Vertex(name = 'V_492', 
	 particles = [P.g, P.g, P.g], 
	 color = ['f(1,2,3)'], 
	 lorentz = [L.VVV1], 
	 couplings = {(0,0):C.GC_735}) 
 
 
V_493 = Vertex(name = 'V_493', 
	 particles = [P.Wpc, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.VVV1], 
	 couplings = {(0,0):C.GC_736}) 
 
 
V_494 = Vertex(name = 'V_494', 
	 particles = [P.Wpc, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.VVV1], 
	 couplings = {(0,0):C.GC_737}) 
 
 
V_495 = Vertex(name = 'V_495', 
	 particles = [P.g, P.g, P.g, P.g], 
	 color = ['f(-1,1,4)*f(-1,2,3)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,2)*f(-1,3,4)'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_738,(1,0):C.GC_739,(0,1):C.GC_740,(2,1):C.GC_741,(1,2):C.GC_742,(2,2):C.GC_743}) 
 
 
V_496 = Vertex(name = 'V_496', 
	 particles = [P.Wpc, P.A, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_744,(0,1):C.GC_745,(0,2):C.GC_746}) 
 
 
V_497 = Vertex(name = 'V_497', 
	 particles = [P.Wpc, P.A, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_747,(0,1):C.GC_748,(0,2):C.GC_749}) 
 
 
V_498 = Vertex(name = 'V_498', 
	 particles = [P.Wpc, P.Wpc, P.Wp, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_750,(0,1):C.GC_751,(0,2):C.GC_752}) 
 
 
V_499 = Vertex(name = 'V_499', 
	 particles = [P.Wpc, P.Wp, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_753,(0,1):C.GC_754,(0,2):C.GC_755}) 
 
 
V_500 = Vertex(name = 'V_500', 
	 particles = [P.A, P.A, P.h1], 
	 color = ['1'], 
	 lorentz = [L.VVS99], 
	 couplings = {(0,0):C.GC_756}) 
 
 
V_501 = Vertex(name = 'V_501', 
	 particles = [P.g, P.g, P.h1], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.VVS99], 
	 couplings = {(0,0):C.GC_757}) 
 
 
V_502 = Vertex(name = 'V_502', 
	 particles = [P.A, P.A, P.h2], 
	 color = ['1'], 
	 lorentz = [L.VVS99], 
	 couplings = {(0,0):C.GC_758}) 
 
 
V_503 = Vertex(name = 'V_503', 
	 particles = [P.g, P.g, P.h2], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.VVS99], 
	 couplings = {(0,0):C.GC_759}) 
 
 
