#encoding:utf-8
from math import *

print 'Algoritmo de Blum,Blum Shub \n'
x= int(raw_input('Valor de la raiz: ')) #impar debe ser este num
#g= int(raw_input('Ingrese el valor de g: '))
m = int(raw_input('Escriba su m :'))

#m=2**g

x=[x]
i=0
r=[0]
b=0
while i <=m-1 and b==0:
	x=x+[(x[i]**2)%m]
		
	#x=x+[(a*x[i]+c)%m]
	i=i+1
	r=r+[float(x[i])/(m-1)]
	if x[0]==x[i]:
		ban=1
		print 'aqui se de genera :D'
	print 'numero que se encontro',str(i)+'--- >>:',str(x[i])
	print 'raiz',str(i)+ '--->>  :',str(round(r[i],5))
	print '\n-----------------***---------------------\n'
