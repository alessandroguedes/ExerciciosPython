n = int(input('Quanto dinheiro vc tem na carteira? R$ '))
print(type(n))
d = n/2
print(type(d))
print('Com R${} você pode comprar US${:.2f}'.format(n, d))
