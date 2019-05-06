#Orbitas planetarias. A partir de la segunda ley de Kepler escriba un programa que calcule la posiciòn y velocidad en el afelio dada la posiciòn y velocidad en al perihelio

from math import pi

G=6.67e-11
m=1.989e30

r_p=float(input("Ingrese el radio del perihelio"))
v_p=float(input("Ingrese la velocidad del perihelio"))

v_a=(((2*G*m)/(v_p*r_p))+((((2*G*m)/(v_p*r_p))**(2))+4*((v_p**2-2*G*m)/r_p))**1/2)/2
print("La velocidad del afelio es:" ,v_a)
r_a=(r_p*v_p)/v_a
print("El radio del afelio:" ,r_a)
a=(r_p+r_a)/2
print("El semieje mayor es:" ,a)
b=(r_p*r_a)**(1/2)
print("El semieje menor es:" ,b)
T=(2*pi*a*b)/(r_p*v_p)
print("El periodo orbital es:", T)
e=(r_a-r_p)/(r_a+r_p)
print("La excentricidad Orbital es:" ,e)

