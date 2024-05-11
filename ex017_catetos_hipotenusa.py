import math

co = float(input('Digite o cateo oposto: '))
ca = float(input('Digite o cateto adjascente: '))
hip = math.sqrt(co**2+ ca**2)
print('A hipotenusa é: {:.2f}'.format(hip))

