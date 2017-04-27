{(B0[p^2, Mass2[Ah], Mass2[Ah]]*conj[Cp[Ah, Ah, Ah]]*Cp[Ah, Ah, Ah])/2 + 
  B0[p^2, Mass2[etI], Mass2[Ah]]*conj[Cp[Ah, etI, Ah]]*Cp[Ah, etI, Ah] + 
  (B0[p^2, Mass2[etI], Mass2[etI]]*conj[Cp[Ah, etI, etI]]*Cp[Ah, etI, etI])/
   2 - B0[p^2, Mass2[gWp], Mass2[gWp]]*Cp[Ah, bar[gWp], gWp]^2 - 
  B0[p^2, Mass2[gWpC], Mass2[gWpC]]*Cp[Ah, bar[gWpC], gWpC]^2 - 
  (A0[Mass2[Ah]]*Cp[Ah, Ah, Ah, Ah])/2 - 
  (A0[Mass2[etI]]*Cp[Ah, Ah, etI, etI])/2 + 4*Cp[Ah, Ah, conj[VWp], VWp]*
   (A0[Mass2[VWp]] - (rMS*Mass2[VWp])/2) + 2*Cp[Ah, Ah, VZ, VZ]*
   (A0[Mass2[VZ]] - (rMS*Mass2[VZ])/2) + 
  sum[gI1, 1, 2, B0[p^2, Mass2[hh[{gI1}]], Mass2[Ah]]*
    conj[Cp[Ah, hh[{gI1}], Ah]]*Cp[Ah, hh[{gI1}], Ah]] + 
  sum[gI1, 1, 2, B0[p^2, Mass2[hh[{gI1}]], Mass2[etI]]*
    conj[Cp[Ah, hh[{gI1}], etI]]*Cp[Ah, hh[{gI1}], etI]] - 
  sum[gI1, 1, 2, A0[Mass2[hh[{gI1}]]]*Cp[Ah, Ah, hh[{gI1}], hh[{gI1}]]]/2 + 
  sum[gI1, 1, 2, sum[gI2, 1, 2, B0[p^2, Mass2[hh[{gI1}]], Mass2[hh[{gI2}]]]*
      conj[Cp[Ah, hh[{gI1}], hh[{gI2}]]]*Cp[Ah, hh[{gI1}], hh[{gI2}]]]]/2 - 
  sum[gI1, 1, 3, A0[Mass2[Hm[{gI1}]]]*Cp[Ah, Ah, conj[Hm[{gI1}]], 
     Hm[{gI1}]]] + sum[gI1, 1, 3, sum[gI2, 1, 3, 
    B0[p^2, Mass2[Hm[{gI1}]], Mass2[Hm[{gI2}]]]*
     conj[Cp[Ah, conj[Hm[{gI1}]], Hm[{gI2}]]]*Cp[Ah, conj[Hm[{gI1}]], 
      Hm[{gI2}]]]] - 6*sum[gI1, 1, 3, Mass[Fd[{gI1}]]*
     sum[gI2, 1, 3, B0[p^2, Mass2[Fd[{gI1}]], Mass2[Fd[{gI2}]]]*
       Mass[Fd[{gI2}]]*(conj[Cp[Ah, bar[Fd[{gI1}]], Fd[{gI2}]][PR]]*
         Cp[Ah, bar[Fd[{gI1}]], Fd[{gI2}]][PL] + 
        conj[Cp[Ah, bar[Fd[{gI1}]], Fd[{gI2}]][PL]]*
         Cp[Ah, bar[Fd[{gI1}]], Fd[{gI2}]][PR])]] + 
  3*sum[gI1, 1, 3, sum[gI2, 1, 3, G0[p^2, Mass2[Fd[{gI1}]], Mass2[Fd[{gI2}]]]*
      (conj[Cp[Ah, bar[Fd[{gI1}]], Fd[{gI2}]][PL]]*
        Cp[Ah, bar[Fd[{gI1}]], Fd[{gI2}]][PL] + 
       conj[Cp[Ah, bar[Fd[{gI1}]], Fd[{gI2}]][PR]]*
        Cp[Ah, bar[Fd[{gI1}]], Fd[{gI2}]][PR])]] - 
  2*sum[gI1, 1, 3, Mass[Fe[{gI1}]]*sum[gI2, 1, 3, 
      B0[p^2, Mass2[Fe[{gI1}]], Mass2[Fe[{gI2}]]]*Mass[Fe[{gI2}]]*
       (conj[Cp[Ah, bar[Fe[{gI1}]], Fe[{gI2}]][PR]]*
         Cp[Ah, bar[Fe[{gI1}]], Fe[{gI2}]][PL] + 
        conj[Cp[Ah, bar[Fe[{gI1}]], Fe[{gI2}]][PL]]*
         Cp[Ah, bar[Fe[{gI1}]], Fe[{gI2}]][PR])]] + 
  sum[gI1, 1, 3, sum[gI2, 1, 3, G0[p^2, Mass2[Fe[{gI1}]], Mass2[Fe[{gI2}]]]*
     (conj[Cp[Ah, bar[Fe[{gI1}]], Fe[{gI2}]][PL]]*
       Cp[Ah, bar[Fe[{gI1}]], Fe[{gI2}]][PL] + 
      conj[Cp[Ah, bar[Fe[{gI1}]], Fe[{gI2}]][PR]]*
       Cp[Ah, bar[Fe[{gI1}]], Fe[{gI2}]][PR])]] - 
  6*sum[gI1, 1, 3, Mass[Fu[{gI1}]]*sum[gI2, 1, 3, 
      B0[p^2, Mass2[Fu[{gI1}]], Mass2[Fu[{gI2}]]]*Mass[Fu[{gI2}]]*
       (conj[Cp[Ah, bar[Fu[{gI1}]], Fu[{gI2}]][PR]]*
         Cp[Ah, bar[Fu[{gI1}]], Fu[{gI2}]][PL] + 
        conj[Cp[Ah, bar[Fu[{gI1}]], Fu[{gI2}]][PL]]*
         Cp[Ah, bar[Fu[{gI1}]], Fu[{gI2}]][PR])]] + 
  3*sum[gI1, 1, 3, sum[gI2, 1, 3, G0[p^2, Mass2[Fu[{gI1}]], Mass2[Fu[{gI2}]]]*
      (conj[Cp[Ah, bar[Fu[{gI1}]], Fu[{gI2}]][PL]]*
        Cp[Ah, bar[Fu[{gI1}]], Fu[{gI2}]][PL] + 
       conj[Cp[Ah, bar[Fu[{gI1}]], Fu[{gI2}]][PR]]*
        Cp[Ah, bar[Fu[{gI1}]], Fu[{gI2}]][PR])]] + 
  sum[gI2, 1, 2, conj[Cp[Ah, VZ, hh[{gI2}]]]*Cp[Ah, VZ, hh[{gI2}]]*
    F0[p^2, Mass2[hh[{gI2}]], Mass2[VZ]]] + 
  2*sum[gI2, 1, 3, conj[Cp[Ah, VWp, Hm[{gI2}]]]*Cp[Ah, VWp, Hm[{gI2}]]*
     F0[p^2, Mass2[Hm[{gI2}]], Mass2[VWp]]], 
 (B0[p^2, Mass2[Ah], Mass2[Ah]]*conj[Cp[etI, Ah, Ah]]*Cp[etI, Ah, Ah])/2 + 
  B0[p^2, Mass2[etI], Mass2[Ah]]*conj[Cp[etI, etI, Ah]]*Cp[etI, etI, Ah] + 
  (B0[p^2, Mass2[etI], Mass2[etI]]*conj[Cp[etI, etI, etI]]*Cp[etI, etI, etI])/
   2 - B0[p^2, Mass2[gWp], Mass2[gWp]]*Cp[etI, bar[gWp], gWp]^2 - 
  B0[p^2, Mass2[gWpC], Mass2[gWpC]]*Cp[etI, bar[gWpC], gWpC]^2 - 
  (A0[Mass2[Ah]]*Cp[etI, etI, Ah, Ah])/2 - 
  (A0[Mass2[etI]]*Cp[etI, etI, etI, etI])/2 + 4*Cp[etI, etI, conj[VWp], VWp]*
   (A0[Mass2[VWp]] - (rMS*Mass2[VWp])/2) + 2*Cp[etI, etI, VZ, VZ]*
   (A0[Mass2[VZ]] - (rMS*Mass2[VZ])/2) + 
  sum[gI1, 1, 2, B0[p^2, Mass2[hh[{gI1}]], Mass2[Ah]]*
    conj[Cp[etI, hh[{gI1}], Ah]]*Cp[etI, hh[{gI1}], Ah]] + 
  sum[gI1, 1, 2, B0[p^2, Mass2[hh[{gI1}]], Mass2[etI]]*
    conj[Cp[etI, hh[{gI1}], etI]]*Cp[etI, hh[{gI1}], etI]] - 
  sum[gI1, 1, 2, A0[Mass2[hh[{gI1}]]]*Cp[etI, etI, hh[{gI1}], hh[{gI1}]]]/2 + 
  sum[gI1, 1, 2, sum[gI2, 1, 2, B0[p^2, Mass2[hh[{gI1}]], Mass2[hh[{gI2}]]]*
      conj[Cp[etI, hh[{gI1}], hh[{gI2}]]]*Cp[etI, hh[{gI1}], hh[{gI2}]]]]/2 - 
  sum[gI1, 1, 3, A0[Mass2[Hm[{gI1}]]]*Cp[etI, etI, conj[Hm[{gI1}]], 
     Hm[{gI1}]]] + sum[gI1, 1, 3, sum[gI2, 1, 3, 
    B0[p^2, Mass2[Hm[{gI1}]], Mass2[Hm[{gI2}]]]*
     conj[Cp[etI, conj[Hm[{gI1}]], Hm[{gI2}]]]*Cp[etI, conj[Hm[{gI1}]], 
      Hm[{gI2}]]]] - 6*sum[gI1, 1, 3, Mass[Fd[{gI1}]]*
     sum[gI2, 1, 3, B0[p^2, Mass2[Fd[{gI1}]], Mass2[Fd[{gI2}]]]*
       Mass[Fd[{gI2}]]*(conj[Cp[etI, bar[Fd[{gI1}]], Fd[{gI2}]][PR]]*
         Cp[etI, bar[Fd[{gI1}]], Fd[{gI2}]][PL] + 
        conj[Cp[etI, bar[Fd[{gI1}]], Fd[{gI2}]][PL]]*
         Cp[etI, bar[Fd[{gI1}]], Fd[{gI2}]][PR])]] + 
  3*sum[gI1, 1, 3, sum[gI2, 1, 3, G0[p^2, Mass2[Fd[{gI1}]], Mass2[Fd[{gI2}]]]*
      (conj[Cp[etI, bar[Fd[{gI1}]], Fd[{gI2}]][PL]]*
        Cp[etI, bar[Fd[{gI1}]], Fd[{gI2}]][PL] + 
       conj[Cp[etI, bar[Fd[{gI1}]], Fd[{gI2}]][PR]]*
        Cp[etI, bar[Fd[{gI1}]], Fd[{gI2}]][PR])]] - 
  2*sum[gI1, 1, 3, Mass[Fe[{gI1}]]*sum[gI2, 1, 3, 
      B0[p^2, Mass2[Fe[{gI1}]], Mass2[Fe[{gI2}]]]*Mass[Fe[{gI2}]]*
       (conj[Cp[etI, bar[Fe[{gI1}]], Fe[{gI2}]][PR]]*
         Cp[etI, bar[Fe[{gI1}]], Fe[{gI2}]][PL] + 
        conj[Cp[etI, bar[Fe[{gI1}]], Fe[{gI2}]][PL]]*
         Cp[etI, bar[Fe[{gI1}]], Fe[{gI2}]][PR])]] + 
  sum[gI1, 1, 3, sum[gI2, 1, 3, G0[p^2, Mass2[Fe[{gI1}]], Mass2[Fe[{gI2}]]]*
     (conj[Cp[etI, bar[Fe[{gI1}]], Fe[{gI2}]][PL]]*
       Cp[etI, bar[Fe[{gI1}]], Fe[{gI2}]][PL] + 
      conj[Cp[etI, bar[Fe[{gI1}]], Fe[{gI2}]][PR]]*
       Cp[etI, bar[Fe[{gI1}]], Fe[{gI2}]][PR])]] - 
  6*sum[gI1, 1, 3, Mass[Fu[{gI1}]]*sum[gI2, 1, 3, 
      B0[p^2, Mass2[Fu[{gI1}]], Mass2[Fu[{gI2}]]]*Mass[Fu[{gI2}]]*
       (conj[Cp[etI, bar[Fu[{gI1}]], Fu[{gI2}]][PR]]*
         Cp[etI, bar[Fu[{gI1}]], Fu[{gI2}]][PL] + 
        conj[Cp[etI, bar[Fu[{gI1}]], Fu[{gI2}]][PL]]*
         Cp[etI, bar[Fu[{gI1}]], Fu[{gI2}]][PR])]] + 
  3*sum[gI1, 1, 3, sum[gI2, 1, 3, G0[p^2, Mass2[Fu[{gI1}]], Mass2[Fu[{gI2}]]]*
      (conj[Cp[etI, bar[Fu[{gI1}]], Fu[{gI2}]][PL]]*
        Cp[etI, bar[Fu[{gI1}]], Fu[{gI2}]][PL] + 
       conj[Cp[etI, bar[Fu[{gI1}]], Fu[{gI2}]][PR]]*
        Cp[etI, bar[Fu[{gI1}]], Fu[{gI2}]][PR])]] + 
  sum[gI2, 1, 2, conj[Cp[etI, VZ, hh[{gI2}]]]*Cp[etI, VZ, hh[{gI2}]]*
    F0[p^2, Mass2[hh[{gI2}]], Mass2[VZ]]] + 
  2*sum[gI2, 1, 3, conj[Cp[etI, VWp, Hm[{gI2}]]]*Cp[etI, VWp, Hm[{gI2}]]*
     F0[p^2, Mass2[Hm[{gI2}]], Mass2[VWp]]], 0, 0, 
 B00[p^2, Mass2[gWp], Mass2[gWp]]*conj[Cp[VZ, bar[gWp], gWp]]*
   Cp[VZ, bar[gWp], gWp] + B00[p^2, Mass2[gWpC], Mass2[gWpC]]*
   conj[Cp[VZ, bar[gWpC], gWpC]]*Cp[VZ, bar[gWpC], gWpC] + 
  (A0[Mass2[Ah]]*Cp[VZ, VZ, Ah, Ah])/2 + 
  (A0[Mass2[etI]]*Cp[VZ, VZ, etI, etI])/2 - conj[Cp[VZ, conj[VWp], VWp]]*
   Cp[VZ, conj[VWp], VWp]*(2*A0[Mass2[VWp]] + 
    10*B00[p^2, Mass2[VWp], Mass2[VWp]] - 2*rMS*(-p^2/3 + 2*Mass2[VWp]) + 
    B0[p^2, Mass2[VWp], Mass2[VWp]]*(4*p^2 + 2*Mass2[VWp])) - 
  4*sum[gI1, 1, 2, B00[p^2, Mass2[Ah], Mass2[hh[{gI1}]]]*
     conj[Cp[VZ, hh[{gI1}], Ah]]*Cp[VZ, hh[{gI1}], Ah]] - 
  4*sum[gI1, 1, 2, B00[p^2, Mass2[etI], Mass2[hh[{gI1}]]]*
     conj[Cp[VZ, hh[{gI1}], etI]]*Cp[VZ, hh[{gI1}], etI]] + 
  sum[gI1, 1, 2, A0[Mass2[hh[{gI1}]]]*Cp[VZ, VZ, hh[{gI1}], hh[{gI1}]]]/2 + 
  sum[gI1, 1, 3, A0[Mass2[Hm[{gI1}]]]*Cp[VZ, VZ, conj[Hm[{gI1}]], 
     Hm[{gI1}]]] - 4*sum[gI1, 1, 3, sum[gI2, 1, 3, 
     B00[p^2, Mass2[Hm[{gI1}]], Mass2[Hm[{gI2}]]]*
      conj[Cp[VZ, conj[Hm[{gI1}]], Hm[{gI2}]]]*Cp[VZ, conj[Hm[{gI1}]], 
       Hm[{gI2}]]]] + 3*sum[gI1, 1, 3, sum[gI2, 1, 3, 
     4*B0[p^2, Mass2[Fd[{gI1}]], Mass2[Fd[{gI2}]]]*Mass[Fd[{gI1}]]*
       Mass[Fd[{gI2}]]*Re[conj[Cp[VZ, bar[Fd[{gI1}]], Fd[{gI2}]][PL]]*
         Cp[VZ, bar[Fd[{gI1}]], Fd[{gI2}]][PR]] + 
      H0[p^2, Mass2[Fd[{gI1}]], Mass2[Fd[{gI2}]]]*
       (conj[Cp[VZ, bar[Fd[{gI1}]], Fd[{gI2}]][PL]]*
         Cp[VZ, bar[Fd[{gI1}]], Fd[{gI2}]][PL] + 
        conj[Cp[VZ, bar[Fd[{gI1}]], Fd[{gI2}]][PR]]*
         Cp[VZ, bar[Fd[{gI1}]], Fd[{gI2}]][PR])]] + 
  sum[gI1, 1, 3, sum[gI2, 1, 3, 4*B0[p^2, Mass2[Fe[{gI1}]], Mass2[Fe[{gI2}]]]*
      Mass[Fe[{gI1}]]*Mass[Fe[{gI2}]]*
      Re[conj[Cp[VZ, bar[Fe[{gI1}]], Fe[{gI2}]][PL]]*
        Cp[VZ, bar[Fe[{gI1}]], Fe[{gI2}]][PR]] + 
     H0[p^2, Mass2[Fe[{gI1}]], Mass2[Fe[{gI2}]]]*
      (conj[Cp[VZ, bar[Fe[{gI1}]], Fe[{gI2}]][PL]]*
        Cp[VZ, bar[Fe[{gI1}]], Fe[{gI2}]][PL] + 
       conj[Cp[VZ, bar[Fe[{gI1}]], Fe[{gI2}]][PR]]*
        Cp[VZ, bar[Fe[{gI1}]], Fe[{gI2}]][PR])]] + 
  3*sum[gI1, 1, 3, sum[gI2, 1, 3, 
     4*B0[p^2, Mass2[Fu[{gI1}]], Mass2[Fu[{gI2}]]]*Mass[Fu[{gI1}]]*
       Mass[Fu[{gI2}]]*Re[conj[Cp[VZ, bar[Fu[{gI1}]], Fu[{gI2}]][PL]]*
         Cp[VZ, bar[Fu[{gI1}]], Fu[{gI2}]][PR]] + 
      H0[p^2, Mass2[Fu[{gI1}]], Mass2[Fu[{gI2}]]]*
       (conj[Cp[VZ, bar[Fu[{gI1}]], Fu[{gI2}]][PL]]*
         Cp[VZ, bar[Fu[{gI1}]], Fu[{gI2}]][PL] + 
        conj[Cp[VZ, bar[Fu[{gI1}]], Fu[{gI2}]][PR]]*
         Cp[VZ, bar[Fu[{gI1}]], Fu[{gI2}]][PR])]] + 
  sum[gI1, 1, 3, sum[gI2, 1, 3, 4*B0[p^2, Mass2[Fv[{gI1}]], Mass2[Fv[{gI2}]]]*
       Mass[Fv[{gI1}]]*Mass[Fv[{gI2}]]*
       Re[conj[Cp[VZ, Fv[{gI1}], Fv[{gI2}]][PL]]*Cp[VZ, Fv[{gI1}], Fv[{gI2}]][
          PR]] + H0[p^2, Mass2[Fv[{gI1}]], Mass2[Fv[{gI2}]]]*
       (conj[Cp[VZ, Fv[{gI1}], Fv[{gI2}]][PL]]*Cp[VZ, Fv[{gI1}], Fv[{gI2}]][
          PL] + conj[Cp[VZ, Fv[{gI1}], Fv[{gI2}]][PR]]*
         Cp[VZ, Fv[{gI1}], Fv[{gI2}]][PR])]]/2 + 
  sum[gI2, 1, 2, B0[p^2, Mass2[VZ], Mass2[hh[{gI2}]]]*
    conj[Cp[VZ, VZ, hh[{gI2}]]]*Cp[VZ, VZ, hh[{gI2}]]] + 
  2*sum[gI2, 1, 3, B0[p^2, Mass2[VWp], Mass2[Hm[{gI2}]]]*
     conj[Cp[VZ, VWp, Hm[{gI2}]]]*Cp[VZ, VWp, Hm[{gI2}]]] + 
  2*rMS*Mass2[VWp]*Cp[VZ, VZ, conj[VWp], VWp][1] - 
  A0[Mass2[VWp]]*(4*Cp[VZ, VZ, conj[VWp], VWp][1] + 
    Cp[VZ, VZ, conj[VWp], VWp][2] + Cp[VZ, VZ, conj[VWp], VWp][3]), 
 B00[p^2, Mass2[gWp], Mass2[gP]]*conj[Cp[conj[VWp], bar[gP], gWp]]*
   Cp[conj[VWp], bar[gP], gWp] + B00[p^2, Mass2[gP], Mass2[gWpC]]*
   conj[Cp[conj[VWp], bar[gWpC], gP]]*Cp[conj[VWp], bar[gWpC], gP] + 
  B00[p^2, Mass2[gZ], Mass2[gWpC]]*conj[Cp[conj[VWp], bar[gWpC], gZ]]*
   Cp[conj[VWp], bar[gWpC], gZ] + B00[p^2, Mass2[gWp], Mass2[gZ]]*
   conj[Cp[conj[VWp], bar[gZ], gWp]]*Cp[conj[VWp], bar[gZ], gWp] + 
  (A0[Mass2[Ah]]*Cp[VWp, conj[VWp], Ah, Ah])/2 + 
  (A0[Mass2[etI]]*Cp[VWp, conj[VWp], etI, etI])/2 - 
  conj[Cp[conj[VWp], VWp, VP]]*Cp[conj[VWp], VWp, VP]*
   (A0[0] + A0[Mass2[VWp]] + 10*B00[p^2, Mass2[VWp], 0] - 
    2*rMS*(-p^2/3 + Mass2[VWp]) + B0[p^2, Mass2[VWp], 0]*
     (4*p^2 + Mass2[VWp])) - conj[Cp[conj[VWp], VZ, VWp]]*
   Cp[conj[VWp], VZ, VWp]*(A0[Mass2[VWp]] + A0[Mass2[VZ]] + 
    10*B00[p^2, Mass2[VZ], Mass2[VWp]] - 
    2*rMS*(-p^2/3 + Mass2[VWp] + Mass2[VZ]) + B0[p^2, Mass2[VZ], Mass2[VWp]]*
     (4*p^2 + Mass2[VWp] + Mass2[VZ])) + 
  sum[gI1, 1, 2, A0[Mass2[hh[{gI1}]]]*Cp[VWp, conj[VWp], hh[{gI1}], 
      hh[{gI1}]]]/2 - 4*sum[gI1, 1, 3, B00[p^2, Mass2[Ah], Mass2[Hm[{gI1}]]]*
     conj[Cp[conj[VWp], conj[Hm[{gI1}]], Ah]]*Cp[conj[VWp], conj[Hm[{gI1}]], 
      Ah]] - 4*sum[gI1, 1, 3, B00[p^2, Mass2[etI], Mass2[Hm[{gI1}]]]*
     conj[Cp[conj[VWp], conj[Hm[{gI1}]], etI]]*Cp[conj[VWp], conj[Hm[{gI1}]], 
      etI]] + sum[gI1, 1, 3, B0[p^2, 0, Mass2[Hm[{gI1}]]]*
    conj[Cp[conj[VWp], conj[Hm[{gI1}]], VP]]*Cp[conj[VWp], conj[Hm[{gI1}]], 
     VP]] + sum[gI1, 1, 3, B0[p^2, Mass2[VZ], Mass2[Hm[{gI1}]]]*
    conj[Cp[conj[VWp], conj[Hm[{gI1}]], VZ]]*Cp[conj[VWp], conj[Hm[{gI1}]], 
     VZ]] + sum[gI1, 1, 3, A0[Mass2[Hm[{gI1}]]]*Cp[VWp, conj[VWp], 
     conj[Hm[{gI1}]], Hm[{gI1}]]] - 
  4*sum[gI1, 1, 3, sum[gI2, 1, 2, B00[p^2, Mass2[hh[{gI2}]], 
       Mass2[Hm[{gI1}]]]*conj[Cp[conj[VWp], conj[Hm[{gI1}]], hh[{gI2}]]]*
      Cp[conj[VWp], conj[Hm[{gI1}]], hh[{gI2}]]]] + 
  3*sum[gI1, 1, 3, sum[gI2, 1, 3, 
     4*B0[p^2, Mass2[Fu[{gI1}]], Mass2[Fd[{gI2}]]]*Mass[Fd[{gI2}]]*
       Mass[Fu[{gI1}]]*Re[conj[Cp[conj[VWp], bar[Fu[{gI1}]], Fd[{gI2}]][PL]]*
         Cp[conj[VWp], bar[Fu[{gI1}]], Fd[{gI2}]][PR]] + 
      H0[p^2, Mass2[Fu[{gI1}]], Mass2[Fd[{gI2}]]]*
       (conj[Cp[conj[VWp], bar[Fu[{gI1}]], Fd[{gI2}]][PL]]*
         Cp[conj[VWp], bar[Fu[{gI1}]], Fd[{gI2}]][PL] + 
        conj[Cp[conj[VWp], bar[Fu[{gI1}]], Fd[{gI2}]][PR]]*
         Cp[conj[VWp], bar[Fu[{gI1}]], Fd[{gI2}]][PR])]] + 
  sum[gI1, 1, 3, sum[gI2, 1, 3, 4*B0[p^2, Mass2[Fv[{gI1}]], Mass2[Fe[{gI2}]]]*
      Mass[Fe[{gI2}]]*Mass[Fv[{gI1}]]*
      Re[conj[Cp[conj[VWp], Fv[{gI1}], Fe[{gI2}]][PL]]*
        Cp[conj[VWp], Fv[{gI1}], Fe[{gI2}]][PR]] + 
     H0[p^2, Mass2[Fv[{gI1}]], Mass2[Fe[{gI2}]]]*
      (conj[Cp[conj[VWp], Fv[{gI1}], Fe[{gI2}]][PL]]*
        Cp[conj[VWp], Fv[{gI1}], Fe[{gI2}]][PL] + 
       conj[Cp[conj[VWp], Fv[{gI1}], Fe[{gI2}]][PR]]*
        Cp[conj[VWp], Fv[{gI1}], Fe[{gI2}]][PR])]] + 
  sum[gI2, 1, 2, B0[p^2, Mass2[VWp], Mass2[hh[{gI2}]]]*
    conj[Cp[conj[VWp], VWp, hh[{gI2}]]]*Cp[conj[VWp], VWp, hh[{gI2}]]] - 
  (A0[0]*(4*Cp[VWp, conj[VWp], VP, VP][1] + Cp[VWp, conj[VWp], VP, VP][2] + 
     Cp[VWp, conj[VWp], VP, VP][3]))/2 + 
  (2*rMS*Mass2[VZ]*Cp[VWp, conj[VWp], VZ, VZ][1] - 
    A0[Mass2[VZ]]*(4*Cp[VWp, conj[VWp], VZ, VZ][1] + 
      Cp[VWp, conj[VWp], VZ, VZ][2] + Cp[VWp, conj[VWp], VZ, VZ][3]))/2 + 
  2*rMS*Mass2[VWp]*Cp[VWp, conj[VWp], conj[VWp], VWp][1] - 
  A0[Mass2[VWp]]*(4*Cp[VWp, conj[VWp], conj[VWp], VWp][1] + 
    Cp[VWp, conj[VWp], conj[VWp], VWp][2] + 
    Cp[VWp, conj[VWp], conj[VWp], VWp][3])}
