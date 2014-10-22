#encoding:utf-8
from math import *

print 'Algoritmo Congruencial No Lineal \n'
x= int(raw_input('Valor de la raiz: ')) #impar debe ser este num
a= int(raw_input('Ingrese el valor de a: '))#entero par
b= int(raw_input('Ingrese el valor de b: '))
c= int(raw_input('Ingrese el valor de c: '))# debe ser impar
g= int(raw_input('Ingrese el valor de g: '))
n = int(raw_input('numero de raices:'))

m=2**g

x=[x]
i=0
r=[0]

while i <=n-1 :
	x=x+[(a*(x[i]**2)+b*x[i]+c)%m]
		
	#x=x+[(a*x[i]+c)%m]
	i=i+1
	r=r+[float(x[i])/(m-1)]
	print 'numero que se encontro',str(i)+'--- >>:',str(x[i])
	print 'raiz',str(i)+ '--->>  :',str(round(r[i],5))
	print '\n-----------------***---------------------\n'
