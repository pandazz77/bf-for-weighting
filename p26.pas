program p26; 
var 
fi1,Tok,sigma,k1,k2,a11,a12,a21,a22,b11,b12,wy,fi,t,dt,dtp,tp,wy1,fiZ,kt,km,Tg,Tgpu,Mgpu,vz,vz1,vx0,ngpu,ngpu1,r,S,S1,e,T1,tpr: real; 
f: text; 
begin
  vx0:=1.62; 
  a11:=-0.115*vx0; 
  a12:=0.416*vx0; 
  a21:=0.1*vx0; 
  a22:=-0.56*vx0; 
  b11:=1; 
  b12:=1; 
  vz:=0; 
  wy:=0; 
  fi:=0; 
  tp:=0; 
  sigma:=-0.1; 
  Tok:=20; 
  dtp:=0.5; 
  t:=0; 
  dt:=0.01; 
  k2:=3992; 
  k1:=3992; 
  fiZ:=0.2; 
  Tg:=2; 
  kt:= 0.0001685; 
  km:=0.000138; 
  r:=0.2; 
  T1:=1; 
  tpr:=0; 
  ngpu:=0; 
  assign (f, 'test.txt'); 
  rewrite(f); 
  while t<Tok do 
    begin
      if t>=tpr then
        begin
          sigma:=k1*(fiZ-fi)+k2*wy;
          tpr:=tpr+T1; 
        end; 
      e:=fiZ-fi; 
      S1:=(e*e+r*ngpu*ngpu); 
      Tgpu:=kt*ngpu; 
      Mgpu:=km*ngpu; 
      ngpu1:=(sigma-ngpu)/Tg; 
      vz1:=a11*vz+a12*wy+b11*Tgpu; 
      wy1:=a21*vz+a22*wy+b12*Mgpu; 
      fi1:=wy; 
      vz:=vz+vz1*dt; 
      wy:=wy+wy1*dt; 
      fi:=fi+fi1*dt; 
      ngpu:=ngpu+ngpu1*dt; 
      S:=S+S1*dt; 
      t:=t+dt; 
      if t>=tp then 
      begin 
        writeln(t,' ',fi,' ',vz,' ',wy,' ',ngpu); 
        writeln(f, t,' ',fi,' ',vz,' ',wy,' ',ngpu); 
        tp:=tp+dtp; 
      end; 
    end; 
  writeln(' S=',S); 
  close(f); 
end.