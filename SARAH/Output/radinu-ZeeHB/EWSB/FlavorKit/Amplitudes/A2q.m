(* ----------------------------------------------------------------------------- *) 
(* This model was automatically created by SARAH version4.9.1  *) 
(* SARAH References: arXiv:0806.0538, 0909.2863, 1002.0840, 1207.0906, 1309.7223 *) 
(* (c) Florian Staub, 2013  *) 
(* ----------------------------------------------------------------------------- *) 
(* File created at 15:59 on 18.1.2017  *) 
(* ---------------------------------------------------------------------- *) 
 
 
LoopContributions[A2q]={
chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, Ah][L][gt2,gt1],coup1R -> Cp[bar[Fd], Fd, Ah][R][gt2,gt1]},}
(* Ah,Fd, Internal:bar[Fd]*) 
{{Ah,Fd,Internal->bar[Fd]},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, Ah][L][i2,gt1],coup1R -> Cp[bar[Fd], Fd, Ah][R][i2,gt1],coup2L -> Cp[bar[Fd], Fd, Ah][L][i3,i2],coup2R -> Cp[bar[Fd], Fd, Ah][R][i3,i2],coup3L -> Cp[bar[Fd], Fd, Ah][L][gt2,i3],coup3R -> Cp[bar[Fd], Fd, Ah][R][gt2,i3]},{mS1 -> M[Ah],mF1 -> M[Fd][i2],MFin -> M[Fd][i3]-M[Fd][gt1]}},
(* etI,Fd, Internal:bar[Fd]*) 
{{etI,Fd,Internal->bar[Fd]},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, etI][L][i2,gt1],coup1R -> Cp[bar[Fd], Fd, etI][R][i2,gt1],coup2L -> Cp[bar[Fd], Fd, etI][L][i3,i2],coup2R -> Cp[bar[Fd], Fd, etI][R][i3,i2],coup3L -> Cp[bar[Fd], Fd, Ah][L][gt2,i3],coup3R -> Cp[bar[Fd], Fd, Ah][R][gt2,i3]},{mS1 -> M[etI],mF1 -> M[Fd][i2],MFin -> M[Fd][i3]-M[Fd][gt1]}},
(* hh,Fd, Internal:bar[Fd]*) 
{{hh,Fd,Internal->bar[Fd]},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, hh][L][i2,gt1,i1],coup1R -> Cp[bar[Fd], Fd, hh][R][i2,gt1,i1],coup2L -> Cp[bar[Fd], Fd, hh][L][i3,i2,i1],coup2R -> Cp[bar[Fd], Fd, hh][R][i3,i2,i1],coup3L -> Cp[bar[Fd], Fd, Ah][L][gt2,i3],coup3R -> Cp[bar[Fd], Fd, Ah][R][gt2,i3]},{mS1 -> M[hh][i1],mF1 -> M[Fd][i2],MFin -> M[Fd][i3]-M[Fd][gt1]}},
(* Hm,Fu, Internal:bar[Fd]*) 
{{Hm,Fu,Internal->bar[Fd]},chargefactor -> 1,{coup1L -> Cp[bar[Fu], Fd, Hm][L][i2,gt1,i1],coup1R -> Cp[bar[Fu], Fd, Hm][R][i2,gt1,i1],coup2L -> Cp[bar[Fd], Fu, conj[Hm]][L][i3,i2,i1],coup2R -> Cp[bar[Fd], Fu, conj[Hm]][R][i3,i2,i1],coup3L -> Cp[bar[Fd], Fd, Ah][L][gt2,i3],coup3R -> Cp[bar[Fd], Fd, Ah][R][gt2,i3]},{mS1 -> M[Hm][i1],mF1 -> M[Fu][i2],MFin -> M[Fd][i3]-M[Fd][gt1]}},
(* VG,Fd, Internal:bar[Fd]*) 
{{VG,Fd,Internal->bar[Fd]},chargefactor -> 4/3,{coup1L -> Cp[bar[Fd], Fd, VG][L][i2,gt1],coup1R -> Cp[bar[Fd], Fd, VG][R][i2,gt1],coup2L -> Cp[bar[Fd], Fd, VG][L][i3,i2],coup2R -> Cp[bar[Fd], Fd, VG][R][i3,i2],coup3L -> Cp[bar[Fd], Fd, Ah][L][gt2,i3],coup3R -> Cp[bar[Fd], Fd, Ah][R][gt2,i3]},{mV1 -> 0,mF1 -> M[Fd][i2],MFin -> M[Fd][i3]-M[Fd][gt1]}},
(* VP,Fd, Internal:bar[Fd]*) 
{{VP,Fd,Internal->bar[Fd]},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, VP][L][i2,gt1],coup1R -> Cp[bar[Fd], Fd, VP][R][i2,gt1],coup2L -> Cp[bar[Fd], Fd, VP][L][i3,i2],coup2R -> Cp[bar[Fd], Fd, VP][R][i3,i2],coup3L -> Cp[bar[Fd], Fd, Ah][L][gt2,i3],coup3R -> Cp[bar[Fd], Fd, Ah][R][gt2,i3]},{mV1 -> 0,mF1 -> M[Fd][i2],MFin -> M[Fd][i3]-M[Fd][gt1]}},
(* VZ,Fd, Internal:bar[Fd]*) 
{{VZ,Fd,Internal->bar[Fd]},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, VZ][L][i2,gt1],coup1R -> Cp[bar[Fd], Fd, VZ][R][i2,gt1],coup2L -> Cp[bar[Fd], Fd, VZ][L][i3,i2],coup2R -> Cp[bar[Fd], Fd, VZ][R][i3,i2],coup3L -> Cp[bar[Fd], Fd, Ah][L][gt2,i3],coup3R -> Cp[bar[Fd], Fd, Ah][R][gt2,i3]},{mV1 -> M[VZ],mF1 -> M[Fd][i2],MFin -> M[Fd][i3]-M[Fd][gt1]}},
(* bar[Fu],VWp, Internal:bar[Fd]*) 
{{bar[Fu],VWp,Internal->bar[Fd]},chargefactor -> 1,{coup1L -> Cp[bar[Fu], Fd, conj[VWp]][L][i1,gt1],coup1R -> Cp[bar[Fu], Fd, conj[VWp]][R][i1,gt1],coup2L -> Cp[bar[Fd], Fu, VWp][L][i3,i1],coup2R -> Cp[bar[Fd], Fu, VWp][R][i3,i1],coup3L -> Cp[bar[Fd], Fd, Ah][L][gt2,i3],coup3R -> Cp[bar[Fd], Fd, Ah][R][gt2,i3]},{mF1 -> M[Fu][i1],mV1 -> M[VWp],MFin -> M[Fd][i3]-M[Fd][gt1]}},
(* Fd,Ah, Internal:Fd*) 
{{Fd,Ah,Internal->Fd},chargefactor -> 1,{coup3L -> Cp[bar[Fd], Fd, Ah][L][i3,gt1],coup3R -> Cp[bar[Fd], Fd, Ah][R][i3,gt1],coup2L -> Cp[bar[Fd], Fd, Ah][L][i1,i3],coup2R -> Cp[bar[Fd], Fd, Ah][R][i1,i3],coup1L -> Cp[bar[Fd], Fd, Ah][L][gt2,i1],coup1R -> Cp[bar[Fd], Fd, Ah][R][gt2,i1]},{mF1 -> M[Fd][i1],mS1 -> M[Ah],MFin -> M[Fd][i3]-M[Fd][gt2]}},
(* Fd,etI, Internal:Fd*) 
{{Fd,etI,Internal->Fd},chargefactor -> 1,{coup3L -> Cp[bar[Fd], Fd, Ah][L][i3,gt1],coup3R -> Cp[bar[Fd], Fd, Ah][R][i3,gt1],coup2L -> Cp[bar[Fd], Fd, etI][L][i1,i3],coup2R -> Cp[bar[Fd], Fd, etI][R][i1,i3],coup1L -> Cp[bar[Fd], Fd, etI][L][gt2,i1],coup1R -> Cp[bar[Fd], Fd, etI][R][gt2,i1]},{mF1 -> M[Fd][i1],mS1 -> M[etI],MFin -> M[Fd][i3]-M[Fd][gt2]}},
(* Fd,hh, Internal:Fd*) 
{{Fd,hh,Internal->Fd},chargefactor -> 1,{coup3L -> Cp[bar[Fd], Fd, Ah][L][i3,gt1],coup3R -> Cp[bar[Fd], Fd, Ah][R][i3,gt1],coup2L -> Cp[bar[Fd], Fd, hh][L][i1,i3,i2],coup2R -> Cp[bar[Fd], Fd, hh][R][i1,i3,i2],coup1L -> Cp[bar[Fd], Fd, hh][L][gt2,i1,i2],coup1R -> Cp[bar[Fd], Fd, hh][R][gt2,i1,i2]},{mF1 -> M[Fd][i1],mS1 -> M[hh][i2],MFin -> M[Fd][i3]-M[Fd][gt2]}},
(* Fu,Hm, Internal:Fd*) 
{{Fu,Hm,Internal->Fd},chargefactor -> 1,{coup3L -> Cp[bar[Fd], Fd, Ah][L][i3,gt1],coup3R -> Cp[bar[Fd], Fd, Ah][R][i3,gt1],coup2L -> Cp[bar[Fu], Fd, Hm][L][i1,i3,i2],coup2R -> Cp[bar[Fu], Fd, Hm][R][i1,i3,i2],coup1L -> Cp[bar[Fd], Fu, conj[Hm]][L][gt2,i1,i2],coup1R -> Cp[bar[Fd], Fu, conj[Hm]][R][gt2,i1,i2]},{mF1 -> M[Fu][i1],mS1 -> M[Hm][i2],MFin -> M[Fd][i3]-M[Fd][gt2]}},
(* Fd,VG, Internal:Fd*) 
{{Fd,VG,Internal->Fd},chargefactor -> 4/3,{coup3L -> Cp[bar[Fd], Fd, Ah][L][i3,gt1],coup3R -> Cp[bar[Fd], Fd, Ah][R][i3,gt1],coup2L -> Cp[bar[Fd], Fd, VG][L][i1,i3],coup2R -> Cp[bar[Fd], Fd, VG][R][i1,i3],coup1L -> Cp[bar[Fd], Fd, VG][L][gt2,i1],coup1R -> Cp[bar[Fd], Fd, VG][R][gt2,i1]},{mF1 -> M[Fd][i1],mV1 -> 0,MFin -> M[Fd][i3]-M[Fd][gt2]}},
(* Fd,VP, Internal:Fd*) 
{{Fd,VP,Internal->Fd},chargefactor -> 1,{coup3L -> Cp[bar[Fd], Fd, Ah][L][i3,gt1],coup3R -> Cp[bar[Fd], Fd, Ah][R][i3,gt1],coup2L -> Cp[bar[Fd], Fd, VP][L][i1,i3],coup2R -> Cp[bar[Fd], Fd, VP][R][i1,i3],coup1L -> Cp[bar[Fd], Fd, VP][L][gt2,i1],coup1R -> Cp[bar[Fd], Fd, VP][R][gt2,i1]},{mF1 -> M[Fd][i1],mV1 -> 0,MFin -> M[Fd][i3]-M[Fd][gt2]}},
(* Fd,VZ, Internal:Fd*) 
{{Fd,VZ,Internal->Fd},chargefactor -> 1,{coup3L -> Cp[bar[Fd], Fd, Ah][L][i3,gt1],coup3R -> Cp[bar[Fd], Fd, Ah][R][i3,gt1],coup2L -> Cp[bar[Fd], Fd, VZ][L][i1,i3],coup2R -> Cp[bar[Fd], Fd, VZ][R][i1,i3],coup1L -> Cp[bar[Fd], Fd, VZ][L][gt2,i1],coup1R -> Cp[bar[Fd], Fd, VZ][R][gt2,i1]},{mF1 -> M[Fd][i1],mV1 -> M[VZ],MFin -> M[Fd][i3]-M[Fd][gt2]}},
(* VWp,bar[Fu], Internal:Fd*) 
{{VWp,bar[Fu],Internal->Fd},chargefactor -> 1,{coup3L -> Cp[bar[Fd], Fd, Ah][L][i3,gt1],coup3R -> Cp[bar[Fd], Fd, Ah][R][i3,gt1],coup2L -> Cp[bar[Fu], Fd, conj[VWp]][L][i2,i3],coup2R -> Cp[bar[Fu], Fd, conj[VWp]][R][i2,i3],coup1L -> Cp[bar[Fd], Fu, VWp][L][gt2,i2],coup1R -> Cp[bar[Fd], Fu, VWp][R][gt2,i2]},{mV1 -> M[VWp],mF1 -> M[Fu][i2],MFin -> M[Fd][i3]-M[Fd][gt2]}}
(* Ah,Fd,Fd*) 
{{Ah,Fd,Fd},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, Ah][L][i2,gt1],coup1R -> Cp[bar[Fd], Fd, Ah][R][i2,gt1],coup2L -> Cp[bar[Fd], Fd, Ah][L][gt2,i3],coup2R -> Cp[bar[Fd], Fd, Ah][R][gt2,i3],coup3L -> Cp[bar[Fd], Fd, Ah][L][i3,i2],coup3R -> Cp[bar[Fd], Fd, Ah][R][i3,i2]},},
(* etI,Fd,Fd*) 
{{etI,Fd,Fd},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, etI][L][i2,gt1],coup1R -> Cp[bar[Fd], Fd, etI][R][i2,gt1],coup2L -> Cp[bar[Fd], Fd, etI][L][gt2,i3],coup2R -> Cp[bar[Fd], Fd, etI][R][gt2,i3],coup3L -> Cp[bar[Fd], Fd, Ah][L][i3,i2],coup3R -> Cp[bar[Fd], Fd, Ah][R][i3,i2]},},
(* hh,Fd,Fd*) 
{{hh,Fd,Fd},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, hh][L][i2,gt1,i1],coup1R -> Cp[bar[Fd], Fd, hh][R][i2,gt1,i1],coup2L -> Cp[bar[Fd], Fd, hh][L][gt2,i3,i1],coup2R -> Cp[bar[Fd], Fd, hh][R][gt2,i3,i1],coup3L -> Cp[bar[Fd], Fd, Ah][L][i3,i2],coup3R -> Cp[bar[Fd], Fd, Ah][R][i3,i2]},},
(* Hm,Fu,Fu*) 
{{Hm,Fu,Fu},chargefactor -> 1,{coup1L -> Cp[bar[Fu], Fd, Hm][L][i2,gt1,i1],coup1R -> Cp[bar[Fu], Fd, Hm][R][i2,gt1,i1],coup2L -> Cp[bar[Fd], Fu, conj[Hm]][L][gt2,i3,i1],coup2R -> Cp[bar[Fd], Fu, conj[Hm]][R][gt2,i3,i1],coup3L -> Cp[bar[Fu], Fu, Ah][L][i3,i2],coup3R -> Cp[bar[Fu], Fu, Ah][R][i3,i2]},},
(* VZ,Fd,Fd*) 
{{VZ,Fd,Fd},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, VZ][L][i2,gt1],coup1R -> Cp[bar[Fd], Fd, VZ][R][i2,gt1],coup2L -> Cp[bar[Fd], Fd, VZ][L][gt2,i3],coup2R -> Cp[bar[Fd], Fd, VZ][R][gt2,i3],coup3L -> Cp[bar[Fd], Fd, Ah][L][i3,i2],coup3R -> Cp[bar[Fd], Fd, Ah][R][i3,i2]},},
(* bar[Fd],Ah,Ah*) 
{{bar[Fd],Ah,Ah},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, Ah][L][i1,gt1],coup1R -> Cp[bar[Fd], Fd, Ah][R][i1,gt1],coup2L -> Cp[bar[Fd], Fd, Ah][L][gt2,i1],coup2R -> Cp[bar[Fd], Fd, Ah][R][gt2,i1],coup3 -> Cp[Ah, Ah, Ah]},},
(* bar[Fd],etI,Ah*) 
{{bar[Fd],etI,Ah},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, etI][L][i1,gt1],coup1R -> Cp[bar[Fd], Fd, etI][R][i1,gt1],coup2L -> Cp[bar[Fd], Fd, Ah][L][gt2,i1],coup2R -> Cp[bar[Fd], Fd, Ah][R][gt2,i1],coup3 -> Cp[Ah, Ah, etI]},},
(* bar[Fd],hh,Ah*) 
{{bar[Fd],hh,Ah},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, hh][L][i1,gt1,i2],coup1R -> Cp[bar[Fd], Fd, hh][R][i1,gt1,i2],coup2L -> Cp[bar[Fd], Fd, Ah][L][gt2,i1],coup2R -> Cp[bar[Fd], Fd, Ah][R][gt2,i1],coup3 -> Cp[Ah, Ah, hh][i2]},},
(* bar[Fd],Ah,etI*) 
{{bar[Fd],Ah,etI},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, Ah][L][i1,gt1],coup1R -> Cp[bar[Fd], Fd, Ah][R][i1,gt1],coup2L -> Cp[bar[Fd], Fd, etI][L][gt2,i1],coup2R -> Cp[bar[Fd], Fd, etI][R][gt2,i1],coup3 -> Cp[Ah, Ah, etI]},},
(* bar[Fd],etI,etI*) 
{{bar[Fd],etI,etI},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, etI][L][i1,gt1],coup1R -> Cp[bar[Fd], Fd, etI][R][i1,gt1],coup2L -> Cp[bar[Fd], Fd, etI][L][gt2,i1],coup2R -> Cp[bar[Fd], Fd, etI][R][gt2,i1],coup3 -> Cp[Ah, etI, etI]},},
(* bar[Fd],hh,etI*) 
{{bar[Fd],hh,etI},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, hh][L][i1,gt1,i2],coup1R -> Cp[bar[Fd], Fd, hh][R][i1,gt1,i2],coup2L -> Cp[bar[Fd], Fd, etI][L][gt2,i1],coup2R -> Cp[bar[Fd], Fd, etI][R][gt2,i1],coup3 -> Cp[Ah, etI, hh][i2]},},
(* bar[Fd],Ah,hh*) 
{{bar[Fd],Ah,hh},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, Ah][L][i1,gt1],coup1R -> Cp[bar[Fd], Fd, Ah][R][i1,gt1],coup2L -> Cp[bar[Fd], Fd, hh][L][gt2,i1,i3],coup2R -> Cp[bar[Fd], Fd, hh][R][gt2,i1,i3],coup3 -> Cp[Ah, Ah, hh][i3]},},
(* bar[Fd],etI,hh*) 
{{bar[Fd],etI,hh},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, etI][L][i1,gt1],coup1R -> Cp[bar[Fd], Fd, etI][R][i1,gt1],coup2L -> Cp[bar[Fd], Fd, hh][L][gt2,i1,i3],coup2R -> Cp[bar[Fd], Fd, hh][R][gt2,i1,i3],coup3 -> Cp[Ah, etI, hh][i3]},},
(* bar[Fd],hh,hh*) 
{{bar[Fd],hh,hh},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, hh][L][i1,gt1,i2],coup1R -> Cp[bar[Fd], Fd, hh][R][i1,gt1,i2],coup2L -> Cp[bar[Fd], Fd, hh][L][gt2,i1,i3],coup2R -> Cp[bar[Fd], Fd, hh][R][gt2,i1,i3],coup3 -> Cp[Ah, hh, hh][i3,i2]},},
(* bar[Fd],VZ,hh*) 
{{bar[Fd],VZ,hh},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, VZ][L][i1,gt1],coup1R -> Cp[bar[Fd], Fd, VZ][R][i1,gt1],coup2L -> Cp[bar[Fd], Fd, hh][L][gt2,i1,i3],coup2R -> Cp[bar[Fd], Fd, hh][R][gt2,i1,i3],coup3 -> Cp[Ah, hh, VZ][i3]},},
(* bar[Fd],hh,VZ*) 
{{bar[Fd],hh,VZ},chargefactor -> 1,{coup1L -> Cp[bar[Fd], Fd, hh][L][i1,gt1,i2],coup1R -> Cp[bar[Fd], Fd, hh][R][i1,gt1,i2],coup2L -> Cp[bar[Fd], Fd, VZ][L][gt2,i1],coup2R -> Cp[bar[Fd], Fd, VZ][R][gt2,i1],coup3 -> Cp[Ah, hh, VZ][i2]},},
(* bar[Fu],conj[Hm],VWp*) 
{{bar[Fu],conj[Hm],VWp},chargefactor -> 1,{coup1L -> Cp[bar[Fu], Fd, Hm][L][i1,gt1,i2],coup1R -> Cp[bar[Fu], Fd, Hm][R][i1,gt1,i2],coup2L -> Cp[bar[Fd], Fu, VWp][L][gt2,i1],coup2R -> Cp[bar[Fd], Fu, VWp][R][gt2,i1],coup3 -> Cp[Ah, conj[Hm], conj[VWp]][i2]},},
(* bar[Fu],VWp,conj[Hm]*) 
{{bar[Fu],VWp,conj[Hm]},chargefactor -> 1,{coup1L -> Cp[bar[Fu], Fd, conj[VWp]][L][i1,gt1],coup1R -> Cp[bar[Fu], Fd, conj[VWp]][R][i1,gt1],coup2L -> Cp[bar[Fd], Fu, conj[Hm]][L][gt2,i1,i3],coup2R -> Cp[bar[Fd], Fu, conj[Hm]][R][gt2,i1,i3],coup3 -> Cp[Ah, Hm, VWp][i3]},},
(* bar[Fu],conj[Hm],conj[Hm]*) 
{{bar[Fu],conj[Hm],conj[Hm]},chargefactor -> 1,{coup1L -> Cp[bar[Fu], Fd, Hm][L][i1,gt1,i2],coup1R -> Cp[bar[Fu], Fd, Hm][R][i1,gt1,i2],coup2L -> Cp[bar[Fd], Fu, conj[Hm]][L][gt2,i1,i3],coup2R -> Cp[bar[Fd], Fu, conj[Hm]][R][gt2,i1,i3],coup3 -> Cp[Ah, Hm, conj[Hm]][i3,i2]},},
(* conj[VWp],Fu,Fu*) 
{{conj[VWp],Fu,Fu},chargefactor -> 1,{coup1L -> Cp[bar[Fu], Fd, conj[VWp]][L][i2,gt1],coup1R -> Cp[bar[Fu], Fd, conj[VWp]][R][i2,gt1],coup2L -> Cp[bar[Fd], Fu, VWp][L][gt2,i3],coup2R -> Cp[bar[Fd], Fu, VWp][R][gt2,i3],coup3L -> Cp[bar[Fu], Fu, Ah][L][i3,i2],coup3R -> Cp[bar[Fu], Fu, Ah][R][i3,i2]},}
};