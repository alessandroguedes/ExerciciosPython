n = float(input('Qual é o preço do produto? R$: '))
nv = n - n*0.05
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(n, nv))