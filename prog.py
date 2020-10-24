from multiprocessing import Process
from math import trunc
import sys
def mainproc(x,y):
	with open('output.txt','w') as file:
		file.write('')
	for k2 in range(x,y):
		for k1 in range(x,y):
			vx0=1.62
			a11=-0.115*vx0
			a12=0.416*vx0
			a21=0.1*vx0
			a22=-0.56*vx0
			b11=1
			b12=1
			vz=0
			wy=0
			fi=0
			tp=0
			sigma=-0.1
			Tok=20
			dtp=0.5
			dt=0.01
			fiZ=0.2
			Tg=2
			kt=0.0001685
			km=0.000138
			r=0.2
			T1=1
			tpr=0
			ngpu=0
			S=0
			t=0
			while t<Tok:
				if t>=tpr:
					sigma=k1*(fiZ-fi)+k2*wy
					tpr=tpr+T1
				e=fiZ-fi
				S1=(e*e+r*ngpu*ngpu)
				Tgpu=kt*ngpu
				Mgpu=km*ngpu
				ngpu1=(sigma-ngpu)/Tg
				vz1=a11*vz+a12*wy+b11*Tgpu
				wy1=a21*vz+a22*wy+b12*Mgpu
				fi1=wy
				vz=vz+vz1*dt
				wy=wy+wy1*dt
				fi=fi+fi1*dt
				ngpu=ngpu+ngpu1*dt
				S=S+S1*dt
				ngpu=ngpu+ngpu1*dt
				S=S+S1*dt
				t=t+dt
				if fi>0.1:
					print(round(fi,1))
				if trunc(fi)==1:
					print('K2: '+str(k2)+'|K1: '+str(k1)+'\n'+str(t)+' '+str(fi)+' '+str(vz)+' '+str(wy)+' '+str(ngpu))
					with open('output.txt','a') as file:
						file.write('t:'+str(t)+' '+'fi:'+str(fi)+' '+'vz:'+str(vz)+' '+'wy:'+str(wy)+' '+'ngpu:'+str(ngpu)+' '+'k2:'+str(k2)+' '+'k1:'+str(k1)+'\n')
					tp=tp+dtp
					try:
						print(' S='+str(S))
					except:
						pass
					sys.exit()
if __name__ == '__main__':
	procs = []
	value = int(input('Кол-во потоков: '))
	x = int(input('X: '))
	y = int(input('Y: '))
	yxrange=y-x
	yxvalue=yxrange/value
	for i in range(1,value+1):
		proc = Process(target=mainproc, args=(int(x+(yxvalue*(i-1))),(int(x+(yxvalue*i)))))
		#print(str(x)+'+'+str(yxvalue)+'*('+str(i)+'-1)   '+str(x)+'+'+str(yxvalue)+'*'+str(i)) 
		#print((int(x+(yxvalue*(i-1))),(int(x+(yxvalue*i)))))
		procs.append(proc)
		proc.start()
	for proc in procs:
		proc.join()
	input()